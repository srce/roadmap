XMLG_FILENAME=roadmap.xml
DOT_FILENAME=data/roadmap.dot
SVG_FILENAME=data/roadmap.svg
PNG_FILENAME=data/roadmap.png
MD_FILENAME=data/roadmap.md

define update_stack
	./tools/xmlg2dot.py --xmlg=stacks/$(1)/$(XMLG_FILENAME) --dot=stacks/$(1)/$(DOT_FILENAME)
	dot -Tsvg stacks/$(1)/$(DOT_FILENAME) -o stacks/$(1)/$(SVG_FILENAME) && dot -Tpng stacks/$(1)/$(DOT_FILENAME) -o stacks/$(1)/$(PNG_FILENAME)

	./tools/xmlg2md.py --xmlg=stacks/$(1)/$(XMLG_FILENAME) --materials=stacks/$(1)/materials.xml --root="backend" > stacks/$(1)/$(MD_FILENAME)
endef

.PHONY: all
all: golang java php
	@echo "Done"

.PHONY: golang
golang:
	@echo "start golang"
	$(call update_stack,go)
	@echo "finish golang"

.PHONY: java
java:
	@echo "start java"
	$(call update_stack,java)
	@echo "finish java"

.PHONY: php
php:
	@echo "start php"
	$(call update_stack,php)
	@echo "finish php"
