#!/usr/bin/env bash
# This script downloads the latest version of the `unhthesis` LaTeX class
# from https://github.com/petebachant/unh-thesis-latex. It should be run from
# the project root directory.

# Should be run from project root directory
if [[ "$PWD" == *scripts ]]
then
    cd ..
fi

curl -O https://raw.githubusercontent.com/petebachant/unh-thesis-latex/master/unhthesis.cls

curl -O https://raw.githubusercontent.com/petebachant/unh-thesis-latex/master/unhth12pt.clo
