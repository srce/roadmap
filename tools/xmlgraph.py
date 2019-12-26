#!/usr/bin/env python3

import xml.etree.ElementTree as Et


class Edge:
    def __init__(self, edge_id, source, target):
        self.id = edge_id
        self.source = source
        self.target = target


class Node:
    def __init__(self, node_id, label):
        self.id = node_id
        self.label = label


class Roadmap:
    def __init__(self, filepath):
        self.edges = {}
        self.nodes = {}
        self.add_from_file(filepath)

    def add_from_file(self, filepath):
        tree = Et.parse(filepath)
        root = tree.getroot()
        for child in root:
            if child.tag == 'include':
                self.add_from_file(child.get('filepath'))
            for dotElem in child:
                if dotElem.tag == 'edge':
                    edge_id = dotElem.get('id')
                    source = dotElem.get('source')
                    target = dotElem.get('target')
                    self.edges[edge_id] = (Edge(edge_id, source, target))
                elif dotElem.tag == 'node':
                    node_id = dotElem.get('id')
                    label = dotElem.get('label')
                    self.nodes[node_id] = (Node(node_id, label))
