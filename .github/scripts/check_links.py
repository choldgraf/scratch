"""Format a sphinx warnings file to be used in a GitHub issue.

This will:
- Parse a sphinx warnings file called `warnings.txt`
- Grab the relative file path + line number for each warning
- Build a GitHub link that points to this path/line
- It does this by assuming a GITHUB_REPOSITORY variable is defined like `ORG/REPO`
- Over-writes warnings.txt so that it can be inserted into a markdown file.
"""
from pathlib import Path
import os
import sys

warnings = Path("warnings.txt")
if not warnings.is_file():
    print("No warnings file found, assuming no errors.")
    sys.exit(0)

# GITHUB_REPOSITORY will be defined in the github workflow
repo = os.environ.get("GITHUB_REPOSITORY", "choldgraf/scratch")
here = Path().resolve()

# Parse each line for the file / line number and build GitHub links.
out = ["### Link and reference warnings", ""]
for iline in warnings.read_text().strip().split("\n"):
    file_path, warning = iline.split(": ", 1)
    file_path, lineno = file_path.rsplit(":")
    if str(here) in file_path:
        rel_path = file_path.replace(str(here), "").strip("/")
        out.append(f"[{rel_path}#{lineno}](https://github.com/{repo}/blob/main/{rel_path}?plain=1#L{lineno})\n- {warning}\n")
    else:
      out.append(iline + "\n")
warnings.write_text("\n".join(out))
