#!/usr/bin/env python3

import argparse
import materials as mt
from xmlgraph import Roadmap


def walk(roadmap, nodeid, level, materials):
    node = roadmap.nodes[nodeid]

    if level > 6:
        level = 6
    print('#'*level + ' ' + node.label + '\n')

    node_mat = materials[nodeid]
    for m in node_mat:
        print("- {}: [{}]({})".format(m.type, m.title, m.url) +
              ('' if m.translate_url == '' else
               "[[{}]({})]".format(m.translate_lang, m.translate_url)))

    for childid in node.childrenids:
        walk(roadmap, childid, level+1, materials)


def convert_md(graphml, xmlmaterials, rootid):
    roadmap = Roadmap(graphml)
    materials = mt.parsexml(xmlmaterials)
    walk(roadmap, rootid, 1, materials)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Combining GraphML and materials into markdown')
    parser.add_argument('--graphml', default='roadmap.xml', help='GraphML filename')
    parser.add_argument('--materials', default='materials.xml', help='Materials XML filename')
    parser.add_argument('--root', default='backend', help='Root element id')
    args = parser.parse_args()

    convert_md(args.graphml, args.materials, args.root)
