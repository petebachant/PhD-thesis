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
import argparse


def convert(fpath_in, fpath_out):
    with Image(filename=fpath_in, resolution=300) as img:
        img.save(filename=fpath_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--overwrite", action="store_true",
                        default=False)
    args = parser.parse_args()

    figs = [f for f in os.listdir("figures") if f.endswith(".pdf") \
            or f.endswith(".PDF")]
    figs = [os.path.join("figures", f) for f in figs]

    for f in figs:
        fout = os.path.split(f)[-1].replace(".pdf", ".png")
        fout = fout.replace(".PDF", ".png")
        fout = os.path.join("figures", "converted", fout)
        if not os.path.isfile(fout) or args.overwrite:
            convert(f, fout)
