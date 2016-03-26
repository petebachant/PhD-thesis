#!/usr/bin/env bash

# Should be run from project root directory
if [[ "$PWD" == *scripts ]]
then
    cd ..
fi

jupyter nbconvert presentation.ipynb --to slides --post serve --config config/slides_config.py
