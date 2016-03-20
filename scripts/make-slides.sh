#!/usr/bin/env bash

jupyter nbconvert presentation.ipynb --to slides --config config/slides_config.py

cp presentation.slides.html index.html
