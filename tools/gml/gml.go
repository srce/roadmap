package gml

import (
	"flag"
	"os"

	"github.com/dennwc/graphml"
)

var (
	Filename = flag.String("graphml", "", "GraphML filename")
)

func Load(filename string) (*graphml.Document, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}

	doc, err := graphml.Decode(file)
	if err != nil {
		return nil, err
	}
	return doc, nil
}

func getNodeByID(g *graphml.Graph, id string) graphml.Node {
	for _, n := range g.Nodes {
		if n.ID == id {
			return n
		}
	}
	return graphml.Node{}
}

func GetChildren(g *graphml.Graph, node graphml.Node) []graphml.Node {
	nodes := []graphml.Node{}
	for _, edge := range g.Edges {
		if edge.Source == node.ID {
			nodes = append(nodes, getNodeByID(g, edge.Target))
		}
	}
	return nodes
}

func GetLabel(node graphml.Node) string {
	for _, attr := range node.Unrecognized {
		if attr.Name.Local == "label" {
			return attr.Value
		}
	}
	return ""
}
