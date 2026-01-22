# conf.py
import os
import sys

# Add source directory to path if needed for autodoc
# sys.path.insert(0, os.path.abspath('.'))

# Basic project information
project = 'Neural Variability Research'
copyright = '2026, Fatih Onay, PhD'
author = 'Fatih Onay'
release = '1.0'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'myst_parser',  # for markdown support
    'sphinx_design',
    'nbsphinx',  # for Jupyter notebook support
    'sphinx_copybutton',  # copy code button
]

# Theme
html_theme = 'sphinx_book_theme'
html_css_files = ['custom.css']

# Logo and theme options
html_logo = "_static/logo.png"
html_theme_options = {
    "logo": {
        "text": "Neural Variability",
    },
    "github_url": "https://github.com/fatihonay/Neural-Variability-",
    "show_toc_level": 2,
    "navigation_with_keys": True,
    "navbar_align": "left",
}

# Source and build directories
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/.ipynb_checkpoints']
html_static_path = ['_static']

# MyST parser options (for markdown)
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

# nbsphinx options
nbsphinx_kernel_name = 'python3'
nbsphinx_timeout = 300
