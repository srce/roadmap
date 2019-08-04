package main

import (
	"flag"
	"fmt"
	graphviz "github.com/awalterschulze/gographviz"
	"github.com/dennwc/graphml"
	"io/ioutil"
	"os"
)

var (
	graphmlFilename = flag.String("filename", "roadmap.graphml.xml", "file name of GraphML")
	dotFilename = flag.String("dot", "roadmap.g.dot", "filename of DOT file")
)

func checkErr(err error) {
	if err != nil {
		panic(err.Error())
	}
}

func main() {
	flag.Parse()

	file, err := os.Open(*graphmlFilename)
	checkErr(err)

	doc, err:= graphml.Decode(file)
	checkErr(err)

	for _, g := range doc.Graphs {
		gviz := graphviz.NewGraph()
		gviz.SetName(g.ID)
		gviz.SetDir(g.EdgeDefault == "directed")

		for _, node := range g.Nodes {
			label := ""
			for _, attr := range node.Unrecognized {
				if attr.Name.Local == "label" {
					label = attr.Value
				}
			}

			err := gviz.AddNode(g.ID, node.ID, map[string]string{
				"label": fmt.Sprintf("\"%s\"", label),
			})

			for _, subg := range node.Graphs {
				fmt.Println(subg.ID)
			}
			
			checkErr(err)
		}

		for _, edge := range g.Edges {
			gviz.AddEdge(edge.Source, edge.Target, true, nil)
		}

		output := gviz.String()
		err = ioutil.WriteFile(*dotFilename,  []byte(output),0644)
		checkErr(err)
	}
}