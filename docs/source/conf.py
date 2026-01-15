# Configuration file for the Sphinx documentation builder.
# -- Project information -----------------------------------------------------
project = 'Neural Variability'
copyright = '2026, Fatih Onay, PhD'
author = 'Fatih Onay, PhD'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',           # Markdown support
    'nbsphinx',              # Jupyter notebooks
    'sphinx.ext.mathjax',    # LaTeX math
    'sphinx.ext.autodoc',    # API docs
    'sphinx.ext.napoleon',   # NumPy / Google docstrings
    'sphinx_design',         # Cards, grids, badges
]

templates_path = ['_templates']
exclude_patterns = []
language = 'en'

# -- MyST configuration -----------------------------------------------------
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

# -- HTML output -------------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
