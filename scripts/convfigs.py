#!/usr/bin/env python
"""Convert a list of figures from PDF to PNG.

Requires:
* ImageMagick
* Ghostscript
* Wand (`pip install wand`)

Could use straight ImageMagick:

    convert -density 300 -depth 8 -quality 85 $INPUT_FILE $OUTPUT_FILE
"""

from wand.image import Image
import os


def convert(fpath_in, fpath_out):
    with Image(filename=fpath_in, resolution=300) as img:
        img.save(filename=fpath_out)


if __name__ == "__main__":
    figs = ["unh-rvat-coord-sys.pdf",
            "BR-CFD_verification.pdf",
            "BR-CFD_perf_bar_chart.pdf",
            "RVAT-ALM_perf-curves.pdf",
            "RVAT-ALM_meancontquiv.pdf",
            "RVAT-ALM_kcont.pdf",
            "RVAT-ALM_recovery-bar-chart.pdf",
            "RVAT-baseline_meancontquiv.pdf",
            "RVAT-baseline_kcont.pdf",
            "BR-CFD_meancontquiv_kOmegaSST.pdf",
            "BR-CFD_meancontquiv_SpalartAllmaras.pdf",
            "BR-CFD_kcont_kOmegaSST.pdf",
            "BR-CFD_kcont_SpalartAllmaras.pdf",
            "BR-CFD_mom_bar_graph.pdf",
            "turbine-test-bed-drawing.pdf",
            "rm2-drawing.pdf",
            "RVAT-ALM_verification.pdf",
            "RM2-ALM_verification.pdf",
            "RM2-ALM_perf-curves.pdf",
            "alm-geometry.pdf"]
    figs = [os.path.join("figures", f) for f in figs]

    overwrite = False

    for f in figs:
        fout = os.path.split(f)[-1].replace(".pdf", ".png")
        fout = os.path.join("figures", "converted", fout)
        if not os.path.isfile(fout) or overwrite:
            convert(f, fout)
