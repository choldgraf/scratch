import nox
from pathlib import Path

nox.options.reuse_existing_virtualenvs = True


@nox.session
def docs(session):
    session.install("-r", "requirements.txt")
    session.run("sphinx-build", "-b=html", "docs/", "docs/_build/html", *session.posargs)


@nox.session(name="docs-live")
def docs_live(session):
    session.install("-r", "requirements.txt")
    session.install("sphinx-autobuild")
    session.run("sphinx-autobuild", "docs", "docs/_build/html", *session.posargs)
