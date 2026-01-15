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
    "navigation_with_keys": True,
    "show_toc_level": 2,
    "navbar_align": "content",

    "navbar_end": ["theme-switcher", "navbar-icon-links"],

    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/yourusername/yourrepo",
            "icon": "fa-brands fa-github",
        },
    ],
}
