# Makefile for thesis text, slides, etc.

## thesis:          Use `latemk` to build PDF of the thesis
.PHONY: thesis
thesis: appendices
	latexmk -pdf thesis.tex


## view:            View `thesis.pdf`
.PHONY: view
view: thesis
ifeq ($(shell uname -s),MINGW64_NT-10.0)
	start "" thesis.pdf
else
	echo "Viewing only setup for Windows"
endif


## clean:           Use `latexmk` to clean all files from `thesis.tex`
.PHONY: clean
clean:
	latexmk -c thesis.tex


## slides:          Convert slides to HTML and copy to `index.html`
.PHONY: slides
slides:
	jupyter nbconvert presentation.ipynb --to slides --config config/slides_config.py

	cp presentation.slides.html index.html


## serve:           Convert slides to HTML and view locally in browser
.PHONY: serve
serve:
ifeq ($(shell uname -s),Linux)
	jupyter nbconvert presentation.ipynb --to slides --post serve --config config/slides_config.py
else
	start cmd //c "jupyter nbconvert presentation.ipynb --to slides --post serve --config config/slides_config.py"
endif


## notebook:        Open up slides with Jupyter Notebook
.PHONY: notebook
notebook:
ifeq ($(shell uname -s),Linux)
	jupyter notebook presentation.ipynb
else
	start cmd //c "jupyter notebook presentation.ipynb"
endif


## png-figs:        Convert PDF figures to PNG
.PHONY: png-figs
png-figs:
	python scripts/convfigs.py


## all-png-figs:    Convert PDF figures to PNG, overwriting all
.PHONY: all-png-figs
all-png-figs:
	python scripts/convfigs.py --overwrite


## excerpt:         Create excerpt PDF with title page and abstract
.PHONY: excerpt
excerpt: thesis
	latexmk -pdf excerpt.tex


## signatures:      Make committee signatures page
.PHONY: signatures
signatures:
	latexmk -pdf signatures.tex


## wikis:           Pull latest versions of wiki repos
.PHONY: wikis
wikis:
	# Update wiki submodules
	cd appendices/turbine-test-bed.wiki && git pull origin master
	cd appendices/RM2-tow-tank.wiki && git pull origin master
	cd appendices/TurbineDAQ.wiki && git pull origin master


## appendices:      Convert wiki Markdown to LaTeX and fix it up
.PHONY: appendices
appendices: appendices/turbine-test-bed.wiki/Operation.md appendices/RM2-tow-tank.wiki/Home.md appendices/TurbineDAQ.wiki/Home.md
	# Build LaTeX from Markdown
	pandoc appendices/turbine-test-bed.wiki/Operation.md -o appendices/test-bed-wiki-operation.tex --chapters --listings --wrap=preserve

	pandoc appendices/RM2-tow-tank.wiki/Home.md -o appendices/rm2-wiki-home.tex --chapters --listings --wrap=preserve

	pandoc appendices/TurbineDAQ.wiki/Home.md -o appendices/turbinedaq.tex --listings --wrap=preserve

	# Clean up automatically generated LaTeX
	python scripts/fix-appendix-latex.py


## bib:             Copy most up-to-date BibTeX database to this directory
.PHONY: bib
bib:
	python getbib.py


.PHONY: help
help: Makefile
	@sed -n "s/^##//p" $<
