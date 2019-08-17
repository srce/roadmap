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

func printErr(err error) {
	if err != nil {
		fmt.Println("warning: "+err.Error())
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
				printErr(errors.New("Tag '" + tag + "' is not exist"))
			}
		}
	}
	return nil
}

func checkLabelDuplicate(graph *graphml.Graph, list *materials.List) error {
	tags := map[string]string{}
	for _, node := range graph.Nodes {
		label := gml.GetLabel(node)
		if _, ok := tags[label]; ok {
			printErr(errors.New("Title '" + label + "' duplicate tag '"+tags[label]+"' and '"+node.ID+"'"))
		}
		tags[label] = node.ID
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
		checkErr(checkLabelDuplicate(&graph, m))
	}

	fmt.Println("Linter: done")
}
