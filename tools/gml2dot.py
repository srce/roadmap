#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import argparse

def convert(root, filename):
    edge_parameters = []
    node_parameters = []

    for child in root:
        for dotElem in child:
            if dotElem.tag == '{http://graphml.graphdrawing.org/xmlns}edge':
                edge_parameters.append('\t'+dotElem.get('source')+'->'+dotElem.get('target')+';\t\n')
            elif dotElem.tag == '{http://graphml.graphdrawing.org/xmlns}node':
                node_parameters.append('\t'+dotElem.get('id')+' [ label="'+dotElem.get('label')+'" ];\n')

    file = open(filename, "w")
    file.write('digraph roadmap {\n\trankdir=LR;\n')
    for edge in edge_parameters:
        file.write(edge)
    for node in node_parameters:
        file.write(node)
    file.write('}')
    file.close()

if (__name__ == '__main__'):
    parser = argparse.ArgumentParser(description='Converting GraphML to DOT')
    parser.add_argument('--graphml', help='GraphML filename')
    parser.add_argument('--dot', help='DOT filename')

    args = parser.parse_args()

    tree = ET.parse(args.graphml)
    root = tree.getroot()

    convert(root, args.dot)
