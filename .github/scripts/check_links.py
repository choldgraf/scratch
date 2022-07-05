from subprocess import run
from pathlib import Path
import os
import sys

# If there's an exception then there was a broken ref or link
warnings = Path("warnings.txt").read_text().strip().split("\n")

# GITHUB_REPOSITORY will be defined in the github workflow
repo = os.environ.get("GITHUB_REPOSITORY", "choldgraf/scratch")
here = Path().resolve()

out = ["### Link and reference warnings", ""]
for ii, iline in enumerate(warnings):
    file_path, warning = iline.split(": ", 1)
    file_path, lineno = file_path.rsplit(":")
    if str(here) in file_path:
        rel_path = file_path.replace(str(here), "").strip("/")
        out.append(f"[{rel_path}#{lineno}](https://github.com/{repo}/blob/main/{rel_path}?plain=1#L{lineno})\n- {warning}\n")
    else:
      out.append(iline)
Path("warnings.txt").write_text("\n".join(out))
