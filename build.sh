#!/usr/bin/env bash

set -e

STACK=$1
ROADMAPFILE="stacks/${STACK}/roadmap.xml"
MATERIALS="stacks/${STACK}/materials.xml"
DOTFILE="stacks/${STACK}/data/roadmap.dot"
SVGFILE="stacks/${STACK}/data/roadmap.svg"
PNGFILE="stacks/${STACK}/data/roadmap.png"
MDFILE="stacks/${STACK}/data/roadmap.md"

./tools/xmlg2dot.py --xmlg=${ROADMAPFILE} --dot=${DOTFILE} && \
  dot -Tsvg ${DOTFILE} -o ${SVGFILE} && \
  dot -Tpng ${DOTFILE} -o ${PNGFILE}

./tools/xmlg2md.py --xmlg=${ROADMAPFILE} --materials=${MATERIALS} --root="backend" > ${MDFILE}
