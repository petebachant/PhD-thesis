#!/usr/bin/env python
"""
This script copies figures from the RVAT Reynolds number dependence
experiment directory.
"""

import os
import sys
import shutil

figdir = os.path.join(os.path.expanduser("~"), "Research",
                      "Experiments", "2014", "RVAT Re dep", "Figures")

figlist = ["cp_vs_tsr.pdf",
           "mean_u.pdf",
           "mean_upvp.pdf"]

for fig in figlist:
    shutil.copy2(os.path.join(figdir, fig), os.path.join("figures", fig))
