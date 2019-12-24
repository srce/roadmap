#!/usr/bin/env python3

class Edge:
    def __init__(self):
        self.id = ""
        self.source = ""
        self.target = ""

class Node:
    def __init__(self):
        self.id = ""
        self.label = ""

class Roadmap:
    def __init__(self, filepath):
        self.includes = {}
        self.edges = {}
        self.nodes = {}

    def get_label(self, id):
        return self.nodes[id].label