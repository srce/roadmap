.PHONY: all
all: gml2dot gml2md
	dot -Tpng roadmap.dot -o roadmap.png

.PHONY: gml2dot
gml2dot:
	GO111MODULE=off go run tools/gml2dot/main.go --dot=roadmap.generated.dot
	circo -Tpng roadmap.generated.dot -o roadmap.circle.png

.PHONY: gml2md
gml2md:
	GO111MODULE=off go run tools/gml2md/main.go --graphml=roadmap.graphml.xml --root="backend" > roadmap.md