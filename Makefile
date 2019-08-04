.PHONY: clean
clean:
	rm roadmap.png

.PHONY: build
build: clean
	dot -Tpng roadmap.dot -o roadmap.png

.PHONY: tool
tool:
	GO111MODULE=off go run tools/graphml2dot.go --dot=roadmap.g.dot && circo -Tsvg roadmap.g.dot -o roadmap.circle.svg