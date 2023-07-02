# Roadmap Core

Computer Science is a young and highly progressive field of study, characterized by a vast amount of knowledge that is constantly evolving. Due to its rapid development, roadmaps become outdated faster than young specialists can orient themselves with them. Not to mention that they can confuse even experienced engineers.

Attempts to tame and comprehend this swirling abyss of knowledge, practices, and tools only lead to panic.

This is why this project was created. It's not so much another completed roadmap as an attempt to create a tool that would help the entire community keep up with the advancements in the field and quickly adapt to its changes.

## Vision

For developers, Skill Matrix is a module that allows to create and collaborate on knowledge roadmaps. A roadmap is compiled from several subject areas, which are described in separate XML files. This allows to reuse components and to populate a change made in one subject into all roadmaps using it.
Skill Matrix allows to compile a roadmap in a XML syntax, visualize it in form of graph, and convert it to Markdown file and spreadsheet, thus covering all desirable representation formats. As a git project, it establishes an adaptable process for change and collaboration.

## Scope of Initial Release

### Skill Matrix includes

- A collection of Subject Roadmaps, described in custom XMLgraph notation.
- A collection of learning Materials for subjects, described in XMLgraph notation.
- A collection of Stack Roadmaps, which specify relevant subjects for the stacks:
  - [Go](#golang)
  - [Java](#java)
  - [Ruby](#ruby)
  - [PHP](#php)
  - [Python](#python)

### A collection of Tools

- [xmlg2dot](tools/xmlg2dot.py) is a tool for converting Roadmap.xml files to DOT syntax. Uses xmlgraph.py
- [xmlg2md](tools/xmlg2md.py) is a tool for converting Materials.xml files to DOT syntax. Uses xmlgraph.py and materials.py
- [Makefile](Makefile) is a major tool that generates Stack Roadmaps and saves them as PNG, SVG, DOT and generated Materials maps and saves them as MD. Uses all tools above.
- [xmlgraph.py](tools/xmlgraph.py) is a library for parsing Roadmap files
- [materials.py](tools/materials.py) is a library for parsing Materials files

## Scope of Future Releases

For future development of the project the following options are considered:
Elaboration on roadmaps structure, adding learning materials.
Creating a tool to check errors in files, such as invalid links in materials files.
Creating roadmaps for other stacks: Python, Ruby, Java Script, .NET C#, Scala, etc.
Adding sets of interview questions for subjects and skills (similar to materials).

## Roadmaps

### Golang

- [SVG](stacks/go/data/roadmap.svg) and [PNG](stacks/go/data/roadmap.png) maps
- [Materials](stacks/go/data/roadmap.md)
- [DOT](stacks/go/data/roadmap.dot) version
- [XML](stacks/go/roadmap.xml)

### Java

- [SVG](stacks/java/data/roadmap.svg) and [PNG](stacks/java/data/roadmap.png) maps
- [Materials](stacks/java/data/roadmap.md)
- [DOT](stacks/java/data/roadmap.dot) version
- [XML](stacks/java/roadmap.xml)

### Ruby

- [SVG](stacks/ruby/data/roadmap.svg) and [PNG](stacks/ruby/data/roadmap.png) maps
- [Materials](stacks/ruby/data/roadmap.md)
- [DOT](stacks/ruby/data/roadmap.dot) version
- [XML](stacks/ruby/roadmap.xml)

### PHP

- [SVG](stacks/php/data/roadmap.svg) and [PNG](stacks/php/data/roadmap.png) maps
- [Materials](stacks/php/data/roadmap.md)
- [DOT](stacks/php/data/roadmap.dot) version
- [XML](stacks/php/roadmap.xml)

### Python

- [SVG](stacks/python/data/roadmap.svg) and [PNG](stacks/python/data/roadmap.png) maps
- [Materials](stacks/python/data/roadmap.md)
- [DOT](stacks/php/python/roadmap.dot) version
- [XML](stacks/python/roadmap.xml)

## For developers

### Prerequisites

Before you continue, ensure you meet the following requirements:

- You have installed the latest version of [Python 3](https://www.python.org/downloads/)
- You also have installed [Graphviz](https://www.graphviz.org/download/)
- And you have a basic understanding of graph theory

### Work

All changes should be developed in your own feature branch and merge throw the merge request.
Also, you should update the project each time you change any XML file by:

```bash
make all
```

## Links

- [Programmer Competency Matrix](http://sijinjoseph.com/programmer-competency-matrix/)
- [Roadmaps for Developers: Backend Developer](https://roadmap.sh/backend)
- [Roadmap to becoming a Software Engineer 2018 Edition with Industry Insights: Back-end Roadmap](https://github.com/fauzanbaig/software-engineer-roadmap#-back-end-roadmap)
