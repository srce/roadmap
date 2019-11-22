import xml.etree.ElementTree as ET
tree = ET.parse('../../roadmap.xml')
root = tree.getroot()


def main() :
    edge_parameters = []
    node_parameters = []

    for child in root:
        for dotElem in child:
            if dotElem.tag == '{http://graphml.graphdrawing.org/xmlns}edge':
                edge_parameters.append('\t'+dotElem.get('source')+'->'+dotElem.get('target')+';\t\n')
            elif dotElem.tag == '{http://graphml.graphdrawing.org/xmlns}node':
                node_parameters.append('\t'+dotElem.get('id')+' [ label="'+dotElem.get('label')+'" ];\n')

    file = open("../../data/roadmap2.dot", "w")
    file.write('digraph roadmap {\n\trankdir=LR;\n')
    for edge in edge_parameters:
        file.write(edge)
    for node in node_parameters:
        file.write(node)
    file.write('}')
    file.close()

main()





