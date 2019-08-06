package main

import (
	"bytes"
	"flag"
	"fmt"
	"github.com/dennwc/graphml"
	"io"
	"os"
	"strings"
)

var (
	gmlFilename = flag.String("filename", "roadmap.graphml.xml", "file name of GraphML")
	rootID = flag.String("root", "", "Root ID")
)

func checkErr(err error) {
	if err != nil {
		panic(err.Error())
	}
}

func getNodeByID(g graphml.Graph, id string) graphml.Node {
	for _, n := range g.Nodes {
		 if n.ID == id {
		 	return n
		 }
	}
	return graphml.Node{}
}

func getChildren(g graphml.Graph, node graphml.Node) []graphml.Node {
	nodes := []graphml.Node{}
	for _, edge := range g.Edges {
		if edge.Source == node.ID {
			nodes = append(nodes, getNodeByID(g, edge.Target))
		}
	}
	return nodes
}

func getLabel(node graphml.Node) string {
	for _, attr := range node.Unrecognized {
		if attr.Name.Local == "label" {
			return attr.Value
		}
	}
	return ""
}

func Walk(w io.Writer, g graphml.Graph, root graphml.Node, n int) {
	children := getChildren(g, root)
	for _, child := range children {
		line := strings.Repeat("#", n) + getLabel(child) + "\n"
		w.Write([]byte(line))
		Walk(w, g, child, n+1)
	}
}

func main() {
	flag.Parse()

	file, err := os.Open(*gmlFilename)
	checkErr(err)

	doc, err:= graphml.Decode(file)
	checkErr(err)

	md := bytes.NewBuffer([]byte{})
	for _, g := range doc.Graphs {
		for _, node := range g.Nodes {
			if node.ID == "backend" {
				md.Write([]byte(fmt.Sprintf("#%s\n", getLabel(node))))
				Walk(md, g, node, 1)
			}
		}
	}

	fmt.Print(md.String())
}