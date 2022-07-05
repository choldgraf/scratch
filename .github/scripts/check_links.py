from subprocess import run
from pathlib import Path
import os
import sys

SPHINX_CALL = "sphinx-build docs docs/_build -w warnings.txt -q -N -b linkcheck"
out = run(SPHINX_CALL.split())
if out.returncode == 0:
    print("Sphinx build had no errors so no links are broken!")
    sys.exit(0)

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
        out.append(f"- https://github.com/{repo}/blob/main/{rel_path}?plain=1#L{lineno}: {warning}")
    else:
      out.append(iline)
Path("warnings.txt").write_text("\n".join(out))
