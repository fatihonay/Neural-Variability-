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
    'sphinx.ext.autodoc',    # API docs (optional but recommended)
    'sphinx.ext.napoleon',   # NumPy / Google docstrings
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- MyST configuration (for $$$ math) --------------------------------------

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

# -- HTML output -------------------------------------------------------------

html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']

html_theme_options = {
    "collapse_navigation": True,
    "show_prev_next": False,
    "show_toc_level": 1,
    "navbar_align": "content",
    "secondary_sidebar_items": [],
}

