#!/usr/bin/env python
"""
This script copies figures into the local figures directory.
"""

import os
import shutil
from os.path import join

homedir = os.path.expanduser("~")
expdir = join(homedir, "Research", "Experiments")
foamrun_23x = join(homedir, "OpenFOAM", "pete-2.3.x", "run")
foamrun_24x = foamrun_23x.replace("2.3.x", "2.4.x")
foamrun_ext1 = join("media", "pete", "Data1", "OpenFOAM", "pete-2.3.x", "run")
foamrun_ext2 = foamrun_ext1.replace("Data1", "Data2")

figdirs = {"RVAT-baseline": join(expdir, "RVAT baseline", "Figures"),
           "RVAT-Re-dep": join(expdir, "RVAT Re dep", "Figures"),
           "AD": join(foamrun_24x, "actuatorSurface", "figures")}

figlists = {"RVAT-baseline": [],
            "RVAT-Re-dep": ["cp_vs_tsr.pdf", "mean_u.pdf", "mean_upvp.pdf"],
            "AD": ["streamwise.pdf", "meancontquiv.pdf"]}

for name, figlist in figlists.items():
    figdir = figdirs[name]
    for fig in figlist:
        oldfigpath = join(figdir, fig)
        newfigpath = os.path.join("figures", name + "_" + fig)
        if os.path.isfile(oldfigpath):
            shutil.copy2(oldfigpath, newfigpath)
            print("Copied {}".format(oldfigpath))
        else:
            print("{} does not exist".format(oldfigpath))
