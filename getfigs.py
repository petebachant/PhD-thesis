#!/usr/bin/env python
"""This script copies figures into the local figures directory."""

import os
import shutil
from os.path import join

homedir = os.path.expanduser("~")
expdir = join(homedir, "Research", "Experiments")
foamrun_23x = join(homedir, "OpenFOAM", "pete-2.3.x", "run")
foamrun_24x = foamrun_23x.replace("2.3.x", "2.4.x")
foamrun_ext1 = join("media", "pete", "Data1", "OpenFOAM", "pete-2.3.x", "run")
foamrun_ext2 = foamrun_ext1.replace("Data1", "Data2")
gdrive = join(homedir, "Google Drive")


figdirs = {"RVAT-baseline": join(expdir, "RVAT baseline", "Figures"),
           "RVAT-Re-dep": join(expdir, "RVAT Re dep", "Figures"),
           "AD": join(foamrun_24x, "actuatorSurface", "figures"),
           "CFD-pop": join(homedir, "Google Drive", "Research",
                           "CFD popularity", "figures"),
           "CFT-vectors": join(gdrive, "Research", "CFT-vectors", "figures"),
           "NACAXX20-XFOIL": join(gdrive, "Research", "Foils", "Data",
                                  "NACAXX20_QBlade", "figures")}

figlists = {"RVAT-baseline": ["perf.pdf", "meancontquiv.pdf", "kcont.pdf",
                              "meanu_2tsrs.pdf", "meanv_2tsrs.pdf",
                              "meanw_2tsrs.pdf", "xvorticitycont.pdf",
                              "meanupvpcont.pdf", "meanupwpcont.pdf",
                              "mean_vel_vs_tsr.pdf", "multispec.pdf",
                              "mombargraph.pdf", "Kbargraph.pdf",
                              "Kturbtranscont.pdf", "fpeak_vcont.pdf",
                              "fstrength_vcont.pdf", "k_2tsrs.pdf"],
            "RVAT-Re-dep": ["cp_curves.pdf", "cd_curves.pdf",
                            "perf_re_dep.pdf", "meancontquiv_10.pdf",
                            "k_contours_10.pdf", "mean_u_k_profiles.pdf"],
            "AD": ["streamwise.pdf", "meancontquiv.pdf"],
            "CFD-pop": ["cfd-online.pdf"],
            "CFT-vectors": ["cft-vectors.pdf", "alpha_deg_urel_geom.pdf"],
            "NACAXX20-XFOIL": ["all_foils_re_dep.pdf",
                               "foil_kinematics_ct.pdf",
                               "cft_re_dep_foils.pdf"]}


for name, figlist in figlists.items():
    figdir = figdirs[name]
    for fig in figlist:
        oldfigpath = join(figdir, fig)
        newfigpath = os.path.join("figures", name + "_" + fig)
        if os.path.isfile(oldfigpath):
            shutil.copy2(oldfigpath, newfigpath)
            print("[x] {}: {} copied".format(name, fig))
        else:
            print("[ ] {}: {} not found".format(name, fig))
