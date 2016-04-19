#!/usr/bin/env python
"""Fix automatically generated LaTeX appendices.

* Remove `\tightlist` commands
* Replace `\includegraphics` calls with URLs and automatically download images
"""

import os
import wget


def fix_image_url(line):
    """Download image if not present and replace with local path.

    The line will look something like this:
        \includegraphics{http://i.imgur.com/W5IycYU.jpg}
    """
    url = line.strip().split("\\includegraphics{")[-1].replace("}", "")
    if not os.path.isdir("figures/downloaded"):
        os.makedirs("figures/downloaded")
    fout = "figures/downloaded/" + url.strip().split("/")[-1]
    if not os.path.isfile(fout):
        wget.download(url=url, out=fout)
    line = line.replace(url, fout)
    line = line.replace("includegraphics{",
                        "includegraphics[width=0.9\\textwidth]{")
    return line


def fix_file(fname):
    """Apply rules to given file."""
    bad_kws = ["\\textbf{Figure", "Welcome", "\\tightlist"]
    with open(fname) as f:
        txt = ""
        for line in f.readlines():
            # line = "%r" % line
            if any(kw in line for kw in bad_kws):
                line = ""
            elif "\\includegraphics" in line:
                line = fix_image_url(line)
            txt += line
    with open(fname, "w") as f:
        f.write(txt)


if __name__ == "__main__":
    files = ["appendices/test-bed-wiki-operation.tex",
             "appendices/rm2-wiki-home.tex"]

    for f in files:
        fix_file(f)
