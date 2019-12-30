#!/usr/bin/env python3
from collections import defaultdict
import xml.etree.ElementTree as Et


class Material:
    def __init__(self):
        self.type = ''
        self.title = ''
        self.url = ''
        self.translate_lang = ''
        self.translate_url = ''


def parsexml(filepath):
    tree = Et.parse(filepath)
    root = tree.getroot()
    materials = defaultdict(lambda: [])
    for mat_desc in root:
        if mat_desc.tag == 'include':
            materials.update(parsexml(mat_desc.attrib['filepath']))
            continue
        material = Material()
        material.type = mat_desc.tag
        for item in mat_desc:
            if item.tag == 'title':
                material.title = item.text
            if item.tag == 'url':
                material.url = item.text
            if item.tag == 'translate':
                material.translate_lang = item.attrib['lang']
                material.translate_url = item.attrib['url']
            if item.tag == 'tags':
                for tag in item:
                    materials[tag.text].append(material)
    return materials
