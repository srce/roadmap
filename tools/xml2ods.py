#!/usr/bin/env python3

import argparse
from odf.opendocument import OpenDocumentSpreadsheet
from odf.style import Style, TextProperties, ParagraphProperties, TableColumnProperties
from odf.text import P
from odf.table import Table, TableColumn, TableRow, TableCell
from xmlgraph import Roadmap


def add_header(sheet):
    tablerow = TableRow()
    cell = TableCell()
    tablerow.addElement(cell)
    cell = TableCell()
    cell.addElement(P(text="Overview"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Employee"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Tech Interview Date "))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Before assessment level"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Project"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Project/Resource Manager"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Interviewer"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Level"))
    tablerow.addElement(cell)
    cell = TableCell()
    cell.addElement(P(text="Description"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="-"))
    tablerow.addElement(cell)
    cell = TableCell()
    cell.addElement(P(text="- опрос по этой теме во время интервью не производился"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="None"))
    tablerow.addElement(cell)
    cell = TableCell()
    cell.addElement(P(text="- нет знаний по теме"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Novice"))
    tablerow.addElement(cell)
    cell = TableCell()
    cell.addElement(P(text="- требуется понимание сути навыка, теоретичестие знания основных понятий и минимальное проявление в работе (Базовые неглубокие отрывочные знания хотябы по каким-то темам)"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Intermediate"))
    tablerow.addElement(cell)
    cell = TableCell()
    cell.addElement(P(text="- хорошие знания теории по большинству подтем из темы, представляет как это применять на практике и имеет опыт применения в работе (на субъективном уровне знает тему на уровне мидла)"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Advanced"))
    tablerow.addElement(cell)
    cell = TableCell()
    cell.addElement(P(text="- глубокие знания по большинству подтем, разбирается в тонкостях, понимает как это применять, и или применял на практике или без проблем сможет применить при неободимости (на субъективном уровне знает тему на уровне сеньера) "))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)


def add_footer(sheet):
    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Assessment Result"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="After assessment level"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Next level"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)

    tablerow = TableRow()
    cell = TableCell()
    cell.addElement(P(text="Next assessment date"))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)


def add_skill(sheet, skill_block, roadmap, level):
    tablerow = TableRow()
    for i in range(level):
        cell = TableCell()
        tablerow.addElement(cell)
    cell = TableCell()
    cell.addElement(P(text=skill_block.label))
    tablerow.addElement(cell)
    sheet.addElement(tablerow)
    for skill_id in skill_block.childrenids:
        skill = roadmap.nodes[skill_id]
        add_skill(tablerow, skill, roadmap, level + 1)


def draw_skills_block(sheet, roadmap, rootid):
    for block_id in roadmap.nodes[rootid].childrenids:
        block = roadmap.nodes[block_id]
        tablerow = TableRow()
        cell = TableCell()
        cell.addElement(P(text=block.label))
        tablerow.addElement(cell)
        sheet.addElement(tablerow)
        for skill_id in block.childrenids:
            skill = roadmap.nodes[skill_id]
            add_skill(sheet, skill, roadmap, 0)


def generate_ods(graphml, root_id):
    textdoc = OpenDocumentSpreadsheet()
    tablecontents = Style(name="Table Contents", family="paragraph")
    tablecontents.addElement(ParagraphProperties(numberlines="false", linenumber="0"))
    tablecontents.addElement(TextProperties(fontweight="bold"))
    textdoc.styles.addElement(tablecontents)
    sheet = Table(name="Sheet")

    add_header(sheet)

    roadmap = Roadmap(graphml)

    draw_skills_block(sheet, roadmap, root_id)

    add_footer(sheet)

    textdoc.spreadsheet.addElement(sheet)
    textdoc.save('roadmap.ods')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Combining GraphML and materials into markdown')
    parser.add_argument('--xmlg', default='roadmap.xml', help='XML Graph filename')
    parser.add_argument('--root', default='backend', help='Root element id')
    args = parser.parse_args()

    generate_ods(args.xmlg, args.root)
