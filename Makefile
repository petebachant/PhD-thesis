# Makefile for thesis text, slides, etc.

slides:
	jupyter nbconvert presentation.ipynb --to slides --config config/slides_config.py

	cp presentation.slides.html index.html


serve:
ifeq ($(shell uname -s),Linux)
	jupyter nbconvert presentation.ipynb --to slides --post serve --config config/slides_config.py
else
	start cmd //c "jupyter nbconvert presentation.ipynb --to slides --post serve --config config/slides_config.py"
endif


notebook:
ifeq ($(shell uname -s),Linux)
	jupyter notebook presentation.ipynb
else
	start cmd //c "jupyter notebook presentation.ipynb"
endif


png-figs:
	python scripts/convfigs.py


all-png-figs:
	python scripts/convfigs.py --overwrite


thesis: appendices
	latexmk -pdf thesis.tex


clean:
	latexmk -c thesis.tex


excerpt: thesis
	latexmk -pdf excerpt.tex


signatures:
	latexmk -pdf signatures.tex


wikis:
	# Update wiki submodules
	cd appendices/turbine-test-bed.wiki && git pull origin master
	cd appendices/RM2-tow-tank.wiki && git pull origin master


appendices:
	# Build LaTeX from Markdown
	pandoc appendices/turbine-test-bed.wiki/Operation.md -o appendices/test-bed-wiki-operation.tex --chapters --listings --wrap=preserve

	pandoc appendices/RM2-tow-tank.wiki/Home.md -o appendices/rm2-wiki-home.tex --chapters --listings --wrap=preserve

    # Clean up automatically generated LaTeX
	python scripts/fix-appendix-latex.py
