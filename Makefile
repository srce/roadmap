.PHONY: all
all: linter gml2dot gml2md
	@echo "Done"

.PHONY: linter
linter:
	go run tools/linter/main.go --graphml=roadmap.xml --materials=materials.xml

.PHONY: gml2dot
gml2dot:
	go run tools/gml2dot/main.go --graphml=roadmap.xml --dot=data/roadmap.dot
	dot -Tsvg data/roadmap.dot -o data/roadmap.svg
	circo -Tsvg data/roadmap.dot -o data/roadmap.circle.svg

.PHONY: gml2md
gml2md:
	go run tools/gml2md/main.go --graphml=roadmap.xml --materials=materials.xml --root="backend" > data/roadmap.md