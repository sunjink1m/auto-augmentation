# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# this tells sphinx that our autoaug folder is two folder levels
# outside the /docs folder
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'auto_augmentation'
copyright = '2022, imperial_swe_grp15'
author = 'imperial_swe_grp15'

# The full version, including alpha/beta/rc tags
release = '0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage', 
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'sphinxcontrib.bibtex',
]

# turn on bibliography
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'plain'

# turn on sphinx.ext.autosummary
autosummary_generate = True

# turn on sphinx.ext.coverage
coverage_show_missing_items = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# settings for intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'torch': ('https://docs.python.org/3', None),
    'torchvision': ('https://docs.python.org/3', None),
    }

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme_path = ["_themes", ]
html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'logo_only': True,
    'analytics_anonymize_ip': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# logo
html_logo = "_static/newlogo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


latex_elements = {
    'preamble': r'''
\usepackage{algorithm2e}
\RestyleAlgo{ruled}
\SetKwComment{Comment}{/* }{ */}
''',
}

numfig = True