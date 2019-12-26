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
        self.edges = set()
        self.nodes = set()
        self.add_from_file(filepath)

    def add_from_file(self, filepath):
        tree = Et.parse(filepath)
        root = tree.getroot()
        for child in root:
            if child.tag == 'include':
                self.add_from_file(child.get('filepath'))
            for dotElem in child:
                if dotElem.tag == 'edge':
                    self.edges.add(Edge(dotElem.get('id'), dotElem.get('source'), dotElem.get('target')))
                elif dotElem.tag == 'node':
                    self.nodes.add(Node(dotElem.get('id'), dotElem.get('label')))
