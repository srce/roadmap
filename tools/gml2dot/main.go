package main

import (
	"flag"
	"fmt"
	"io/ioutil"

	graphviz "github.com/awalterschulze/gographviz"
	"github.com/dzyanis/roadmap/tools/gml"
)

var (
	dotFilename = flag.String("dot", "", "filename of DOT file")
)

func checkErr(err error) {
	if err != nil {
		panic(err.Error())
	}
}

func main() {
	flag.Parse()

	doc, err := gml.Load(*gml.Filename)
	checkErr(err)

	for _, g := range doc.Graphs {
		gviz := graphviz.NewGraph()
		checkErr(gviz.SetName(g.ID))
		checkErr(gviz.SetDir(g.EdgeDefault == "directed"))
		checkErr(gviz.AddAttr(g.ID, "rankdir", "LR"))

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
		err = ioutil.WriteFile(*dotFilename, []byte(output), 0644)
		checkErr(err)
	}
}
