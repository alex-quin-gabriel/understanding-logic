# Documentation Instructions

This repository contains the source and configuration files used to generate
documentation for the CoreSense Understanding System.


## Dependencies
This website is built using the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
framework, which allows for easy documentation generation from markdown files.
While it is based on the [CommonMark](https://commonmark.org/) flavor of Markdown,
many extensions are supported which add extra features such as 
[Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/),
[Content Tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/), 
and [Math](https://squidfunk.github.io/mkdocs-material/reference/math/) to name a few.

Simply install Material for MkDocs (and a few plugins) with `pip`, ideally within a virtual environment.
```bash
pip install -r docs/requirements.txt
```

## Live preview
[MkDocs](https://www.mkdocs.org/) (which Material for MkDocs is built on)
provides a live preview server at `localhost:8000` that will automatically rebuild whenever you
save a source file. It can be started with:
```bash
mkdocs serve
```

## Build instructions
Change to the root directory of this repository then build the static site 
in the `build` directory using the `-d` flag (default build directory is `site`):
```bash
mkdocs build -d build
```

## Modifying documentation
The best way to modify the documentation is by directly editing the Markdown
source files in the `docs` directory in your favorite text editor. However, for
a quick fix you can click the :material-file-edit-outline: icon at the top of the page
you wish to edit and it will take you to the **Github** live editor window.

!!! info
    In this repository, quick fix edits will be make in the `documentation`
    branch. You will need to manually merge the changes into `rolling` according to
    the project [Contribution Guidelines](contributing.md).

!!! question "TODO"
    Create [Contribution Guidelines](contributing.md).

If there is an extension or plugin you would like to add for additional functionality,
feel free to edit the [mkdocs.yml](https://github.com/alex-quin-gabriel/understanding-logic/blob/documentation/mkdocs.yml) file.

### Adding new pages
If you want to add a whole new page to the documentation you can create a new
markdown `.md` file in the `docs` directory, or the appropriate sub-directory if the
page is part of a section.
