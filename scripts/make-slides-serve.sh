#!/usr/bin/env bash

jupyter nbconvert presentation.ipynb --to slides --post serve --config config/slides_config.py
