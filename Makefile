GRAPHML_FILENAME=roadmap.xml
DOT_FILENAME=data/roadmap.dot
SVG_FILENAME=data/roadmap.svg
PNG_FILENAME=data/roadmap.png

.PHONY: all
all: xmlg2dot xmlg2md
	@echo "Done"

.PHONY: xmlg2dot
xmlg2dot:
	./tools/xmlg2dot.py --xmlg=$(GRAPHML_FILENAME) --dot=$(DOT_FILENAME)
	dot -Tsvg $(DOT_FILENAME) -o $(SVG_FILENAME)
	dot -Tpng $(DOT_FILENAME) -o $(PNG_FILENAME)

.PHONY: xmlg2md
xmlg2md:
	./tools/xmlg2md.py --xmlg=$(GRAPHML_FILENAME) --materials=materials.xml --root="backend" > data/roadmap.md