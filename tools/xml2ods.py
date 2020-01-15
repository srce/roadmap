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


def generate_ods(graphml):
    textdoc = OpenDocumentSpreadsheet()
    # Create a style for the table content. One we can modify
    # later in the word processor.
    tablecontents = Style(name="Table Contents", family="paragraph")
    tablecontents.addElement(ParagraphProperties(numberlines="false", linenumber="0"))
    tablecontents.addElement(TextProperties(fontweight="bold"))
    textdoc.styles.addElement(tablecontents)
    sheet = Table(name="Sheet")

    add_header(sheet)

    roadmap = Roadmap(graphml)

    add_footer(sheet)

    textdoc.spreadsheet.addElement(sheet)
    textdoc.save('roadmap.ods')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Combining GraphML and materials into markdown')
    parser.add_argument('--xmlg', default='roadmap.xml', help='XML Graph filename')
    args = parser.parse_args()

    generate_ods(args.xmlg)
