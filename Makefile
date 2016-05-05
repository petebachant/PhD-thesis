# Makefile for thesis text, slides, etc.

thesis: appendices
	latexmk -pdf thesis.tex


view: thesis
ifeq ($(shell uname -s),MINGW64_NT-10.0)
	start "" thesis.pdf
else
	echo "Viewing only setup for Windows"
endif


clean:
	latexmk -c thesis.tex


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


excerpt: thesis
	latexmk -pdf excerpt.tex


signatures:
	latexmk -pdf signatures.tex


wikis:
	# Update wiki submodules
	cd appendices/turbine-test-bed.wiki && git pull origin master
	cd appendices/RM2-tow-tank.wiki && git pull origin master
	cd appendices/TurbineDAQ.wiki && git pull origin master


appendices: appendices/turbine-test-bed.wiki/Operation.md appendices/RM2-tow-tank.wiki/Home.md appendices/TurbineDAQ.wiki/Home.md
	# Build LaTeX from Markdown
	pandoc appendices/turbine-test-bed.wiki/Operation.md -o appendices/test-bed-wiki-operation.tex --chapters --listings --wrap=preserve

	pandoc appendices/RM2-tow-tank.wiki/Home.md -o appendices/rm2-wiki-home.tex --chapters --listings --wrap=preserve

	pandoc appendices/TurbineDAQ.wiki/Home.md -o appendices/turbinedaq.tex --listings --wrap=preserve

	# Clean up automatically generated LaTeX
	python scripts/fix-appendix-latex.py
