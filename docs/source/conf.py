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

# In conf.py:
html_theme = 'furo'
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#5B4B8A",
        "color-brand-content": "#5B4B8A",
    },
    "dark_css_variables": {
        "color-brand-primary": "#9B8DC9",
        "color-brand-content": "#9B8DC9",
    },
}
