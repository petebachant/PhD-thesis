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


appendices:
	# Update wiki submodules
	git submodule update --remote appendices/turbine-test-bed.wiki

	git submodule update --remote appendices/RM2-tow-tank.wiki

	# Build LaTeX from Markdown
	pandoc appendices/turbine-test-bed.wiki/Operation.md -o appendices/operation.tex --chapters

    # Clean up automatically generated LaTeX
	python scripts/fix-appendix-latex.py
