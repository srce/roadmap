package main

import (
	"errors"
	"flag"
	"fmt"

	"github.com/dennwc/graphml"
	"github.com/dzyanis/roadmap/tools/gml"
	"github.com/dzyanis/roadmap/tools/materials"
)

func checkErr(err error) {
	if err != nil {
		panic(err.Error())
	}
}


func checkTags(graph *graphml.Graph, list *materials.List) error {
	tags := map[string]struct{}{}
	for _, node := range graph.Nodes {
		tags[node.ID] = struct{}{}
	}
	for _, item := range list.All() {
		for _, tag := range item.Tags {
			if _, ok := tags[tag]; !ok {
				return errors.New("Tag '" + tag + "' is not exist")
			}
		}
	}
	return nil
}

func main() {
	flag.Parse()

	doc, err := gml.Load(*gml.Filename)
	checkErr(err)

	m, err := materials.Load(*materials.Filename)
	checkErr(err)

	for _, graph := range doc.Graphs {
		checkErr(checkTags(&graph, m))
	}

	fmt.Print("Done")
}
