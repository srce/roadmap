#!/usr/bin/env python3

import argparse
from xmlgraph import Roadmap


def convert(graphml, dot):
    roadmap = Roadmap(graphml)

    file = open(dot, "w")
    file.write('digraph roadmap {\n\trankdir=LR;\n')
    for edge in roadmap.edges:
        file.write('\t' + edge.source + '->' + edge.target + ';\t\n')
    for node in roadmap.nodes:
        file.write('\t' + node.id + ' [ label="' + node.label + '" ];\n')
    file.write('}\n')
    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converting GraphML to DOT')
    parser.add_argument('--graphml', help='GraphML filename')
    parser.add_argument('--dot', help='DOT filename')
    args = parser.parse_args()

    convert(args.graphml, args.dot)
