.PHONY: all
all: gml2dot gml2md
	@echo "Done"

.PHONY: gml2dot
gml2dot:
	GO111MODULE=off go run tools/gml2dot/main.go --filename=roadmap.xml --dot=data/roadmap.dot
	dot -Tsvg data/roadmap.dot -o data/roadmap.svg
	circo -Tsvg data/roadmap.dot -o data/roadmap.circle.svg

.PHONY: gml2md
gml2md:
	GO111MODULE=off go run tools/gml2md/main.go --graphml=roadmap.xml --materials=materials.xml --root="backend" > data/roadmap.md