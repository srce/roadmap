package materials

import (
	"encoding/xml"
	"flag"
	"io/ioutil"
)

var (
	Filename = flag.String("materials", "", "materials filename")
)

type Item struct {
	XMLName xml.Name
	Lang    string   `xml:"lang,attr"`
	Title   string   `xml:"title"`
	URL     string   `xml:"url"`
	Tags    []string `xml:"tags>tag"`
}

type List struct {
	XMLName  xml.Name `xml:"materials"`
	Courses  []Item   `xml:"course"`
	Articles []Item   `xml:"article"`
	Books    []Item   `xml:"book"`
}

func (m List) All() []Item {
	return append(m.Courses, append(m.Articles, m.Books...)...)
}

func (m List) Get(tag string) []Item {
	list := make([]Item, 0)
	for _, item := range m.All() {
		for _, it := range item.Tags {
			if it == tag {
				list = append(list, item)
			}
		}
	}
	return list
}

func Load(filename string) (*List, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	var materials List
	err = xml.Unmarshal(data, &materials)
	if err != nil {
		return nil, err
	}
	return &materials, nil
}
