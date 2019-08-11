package main

import (
	"bytes"
	"encoding/xml"
	"flag"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"strings"

	"github.com/dennwc/graphml"
)

var (
	gmlfn  = flag.String("graphml", "", "GraphML filename")
	mfn    = flag.String("materials", "", "materials filename")
	rootID = flag.String("root", "", "Root ID")
)

type materialType struct {
	XMLName xml.Name
	Lang    string   `xml:"lang,attr"`
	Title   string   `xml:"title"`
	URL     string   `xml:"url"`
	Tags    []string `xml:"tags>tag"`
}

type materialsType struct {
	XMLName  xml.Name       `xml:"materials"`
	Courses  []materialType `xml:"course"`
	Articles []materialType `xml:"article"`
	Books    []materialType `xml:"book"`
}

func (m materialsType) Get(tag string) []materialType {
	list := []materialType{}
	ml := append(m.Courses, append(m.Articles, m.Books...)...)
	for _, item := range ml {
		for _, it := range item.Tags {
			if it == tag {
				list = append(list, item)
			}
		}
	}
	return list
}

var materials materialsType

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

func Walk(w io.Writer, g graphml.Graph, root graphml.Node, h int) {
	children := getChildren(g, root)
	for _, child := range children {
		line, err := mdHeader(getLabel(child), h)
		checkErr(err)

		w.Write([]byte(line))
		list := materials.Get(child.ID)
		for _, item := range list {
			line := mdLink(item.Title, item.URL)
			w.Write([]byte(fmt.Sprintf("- %s \"%s\" [%s]\n\n", item.XMLName.Local, line, item.Lang)))
		}
		Walk(w, g, child, h+1)
	}
}

func main() {
	flag.Parse()

	file, err := os.Open(*gmlfn)
	checkErr(err)

	doc, err := graphml.Decode(file)
	checkErr(err)

	mData, err := ioutil.ReadFile(*mfn)
	checkErr(err)

	err = xml.Unmarshal(mData, &materials)
	checkErr(err)

	md := bytes.NewBuffer([]byte{})
	for _, g := range doc.Graphs {
		for _, node := range g.Nodes {
			if node.ID == "backend" {
				md.Write([]byte(fmt.Sprintf("# %s\n", getLabel(node))))
				Walk(md, g, node, 1)
			}
		}
	}

	fmt.Print(md.String())
}
