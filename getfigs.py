#!/usr/bin/env python
"""This script copies figures into the local figures directory."""

import os
import shutil
from os.path import join

homedir = os.path.expanduser("~")
expdir = join(homedir, "Research", "Experiments")
foamrun_23x = join(homedir, "OpenFOAM", "pete-2.3.x", "run")
foamrun_24x = foamrun_23x.replace("2.3.x", "2.4.x")
foamrun_ext1 = join("/media", "pete", "Data1", "OpenFOAM", "pete-2.3.x", "run")
foamrun_ext2 = join("/media", "Data2", "OpenFOAM", "pete-2.3.x", "run")
gdrive = join(homedir, "Google Drive")
foamrun_30x = foamrun_23x.replace("2.3.x", "3.0.x")
foamrun_dev_ext2 = foamrun_ext2.replace("2.3.x", "dev")


figdirs = {"RVAT-baseline": join(expdir, "RVAT baseline", "Figures"),
           "RVAT-Re-dep": join(expdir, "RVAT Re dep", "Figures"),
           "AD": join(foamrun_23x, "actuatorSurface", "figures"),
           "CFD-pop": join(homedir, "Google Drive", "Research",
                           "CFD popularity", "figures"),
           "CFT-vectors": join(gdrive, "Research", "CFT-vectors", "figures"),
           "NACAXX20-XFOIL": join(gdrive, "Research", "Foils", "Data",
                                  "NACAXX20_QBlade", "figures"),
           "BR-CFD": join(gdrive, "Research", "Papers", "CFT wake modeling",
                          "figures"),
           "RVAT-ALM": join(foamrun_30x, "UNH-RVAT-turbinesFoam", "figures"),
           "RM2-ALM": join(foamrun_30x, "RM2-turbinesFoam", "figures"),
           "RVAT-ALM-LES": join(foamrun_dev_ext2, "UNH-RVAT-turbinesFoam",
                                "figures"),
           "end-effects": join(gdrive, "Research", "OpenFOAM", "turbinesFoam",
                               "End effects", "figures"),
           "RM2-tow-tank": join(expdir, "RM2 tow tank", "Figures")}

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
                            "k_contours_10.pdf", "mean_u_k_profiles.pdf",
                            "wake_spectra.pdf", "mom_bar_graph.pdf",
                            "K_trans_bar_graph.pdf", "wake_trans_totals.pdf"],
            "AD": ["streamwise.pdf", "meancontquiv.pdf"],
            "CFT-vectors": ["cft-vectors.pdf", "alpha_deg_urel_geom.pdf"],
            "NACAXX20-XFOIL": ["all_foils_re_dep.pdf",
                               "foil_kinematics_ct.pdf",
                               "cft_re_dep_foils.pdf"],
            "BR-CFD": ["CAD.pdf", "2D_blade_mesh_closeup.png", "2D_mesh.png",
                       "2D_vorticity_SA_964.png",
                       "3D_vorticity_SA_964_10-threshold.png",
                       "kcont_kOmegaSST.pdf", "kcont_SpalartAllmaras.pdf",
                       "meancontquiv_kOmegaSST.pdf",
                       "meancontquiv_SpalartAllmaras.pdf", "mom_bar_graph.pdf",
                       "perf_bar_chart.pdf", "profiles.pdf",
                       "verification.pdf"],
            "RVAT-ALM": ["verification.pdf", "wake-profiles.pdf",
                         "perf-curves.pdf", "meancontquiv.pdf", "kcont.pdf",
                         "recovery-bar-chart.pdf"],
            "RM2-ALM": ["verification.pdf", "wake-profiles.pdf",
                        "perf-curves.pdf", "meancontquiv.pdf", "kcont.pdf",
                        "recovery-bar-chart.pdf"],
            "RVAT-ALM-LES": ["wake-profiles.pdf", "meancontquiv.pdf",
                             "kcont.pdf", "recovery-bar-chart.pdf",
                             "vorticity-snapshot.png"],
            "end-effects": ["rvat-20-deg.pdf"],
            "RM2-tow-tank": ["cp_curves.pdf", "cd_curves.pdf",
                             "perf_re_dep.pdf", "perf_covers.pdf",
                             "no_blades_all.pdf", "meancontquiv.pdf", "k_contours.pdf", "K_trans_bar_graph.pdf"]}


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
