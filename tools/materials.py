#!/usr/bin/env python3

import xml.etree.ElementTree as Et


class Material:
    def __init__(self):
        self.type = ''
        self.title = ''
        self.url = ''
        self.translate = ''
        self.tags = []


def parsexml(filepath):
    tree = Et.parse(filepath)
    root = tree.getroot()
    materials = []
    for mat_desc in root:
        material = Material()
        material.type = mat_desc.tag
        for item in mat_desc:
            if item.tag == 'title':
                material.title = item.text
            if item.tag == 'url':
                material.url = item.text
            if item.tag == 'translate':
                material.translate = item.text
            if item.tag == 'tags':
                for tag in item:
                    material.tags.append(tag.text)
        materials.append(material)
    return materials

