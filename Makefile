GRAPHML_FILENAME=roadmap.xml
DOT_FILENAME=data/roadmap.dot
SVG_FILENAME=data/roadmap.svg

.PHONY: all
all: linter gml2dot gml2md
	@echo "Done"

.PHONY: linter
linter:
	go run tools/linter/main.go --graphml=$(GRAPHML_FILENAME) --materials=materials.xml

.PHONY: gml2dot
gml2dot:
	./tools/gml2dot.py --graphml=$(GRAPHML_FILENAME) --dot=$(DOT_FILENAME)
	dot -Tsvg $(DOT_FILENAME) -o $(SVG_FILENAME)

.PHONY: gml2md
gml2md:
	go run tools/gml2md/main.go --graphml=$(GRAPHML_FILENAME) --materials=materials.xml --root="backend" > data/roadmap.md