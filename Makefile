.PHONY: clean
clean:
	rm roadmap.png

.PHONY: build
build: clean
	dot -Tpng roadmap.dot -o roadmap.png