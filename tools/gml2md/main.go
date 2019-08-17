package main

import (
	"bytes"
	"flag"
	"fmt"
	"io"
	"strings"

	"github.com/dennwc/graphml"
	"github.com/dzyanis/roadmap/tools/gml"
	"github.com/dzyanis/roadmap/tools/materials"
)

var (
	rootID = flag.String("root", "", "Root ID")
)

var icons = map[string]string{
	"book": "📖",
	"article": "📰",
	"course": "👩‍🏫",
	"video": "📺",
}

func checkErr(err error) {
	if err != nil {
		panic(err.Error())
	}
}

func mdHeader(text string, h int) (string, error) {
	if h > 6 {
		return "", fmt.Errorf("there is no header of %d level", h)
	}
	return strings.Repeat("#", h) + " " + text + "\n", nil
}

func mdLink(name, url string) string {
	return fmt.Sprintf("[%s](%s)", name, url)
}

func Walk(w io.Writer, g *graphml.Graph, root graphml.Node, m *materials.List, h int) {
	children := gml.GetChildren(g, root)
	for _, child := range children {
		line, err := mdHeader(gml.GetLabel(child), h)
		checkErr(err)

		w.Write([]byte(line))
		list := m.Get(child.ID)
		for _, item := range list {
			line := mdLink(item.Title, item.URL)
			w.Write([]byte(fmt.Sprintf("%s %s [%s]\n\n", icons[item.XMLName.Local], line, item.Lang)))
		}
		Walk(w, g, child, m, h+1)
	}
}

func main() {
	flag.Parse()

	doc, err := gml.Load(*gml.Filename)
	checkErr(err)

	m, err := materials.Load(*materials.Filename)
	checkErr(err)

	md := bytes.NewBuffer([]byte{})
	for _, g := range doc.Graphs {
		for _, node := range g.Nodes {
			if node.ID == *rootID {
				md.Write([]byte(fmt.Sprintf("# %s\n", gml.GetLabel(node))))
				Walk(md, &g, node, m, 1)
			}
		}
	}

	fmt.Print(md.String())
}
