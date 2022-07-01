# -- Project information -----------------------------------------------------

project = 'Scratch'
copyright = '2022, Chris Holdgraf'
author = 'Chris Holdgraf'


# -- General configuration ---------------------------------------------------

extensions = [
  "myst_parser",
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']