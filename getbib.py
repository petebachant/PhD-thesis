#!/usr/bin/env python
"""This script copies my personal BibTeX file to the current directory."""

import os
import shutil

bibpath = os.path.join(os.path.expanduser("~"), "Google Drive",
                       "Library", "Library.bib")

shutil.copy2(bibpath, "library.bib")
