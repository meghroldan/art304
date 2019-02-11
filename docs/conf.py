#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# conf
# Yellowbrick documentation build config file, created by sphinx-quickstart
#
# Created: Tue Jul 05 19:45:43 2016 -0400
# Copyright (C) 2016-2019 The scikit-yb developers
# For license information, see LICENSE.txt
#
# ID: conf.py [] benjamin@bengfort.com $

"""
Yellowbrick documentation build config file, created by sphinx-quickstart.

This file is executed with the current directory set to its containing dir
by ``execfile()``, e.g. the working directory will be yellowbrick/docs.
Ensure that all specified paths relative to the docs directory are made
absolute by using ``os.path.abspath``.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.

See: https://www.sphinx-doc.org/en/master/usage/configuration.html
for more details on configuring the documentation build.
"""

##########################################################################
## Imports
##########################################################################

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# Set the backend of matplotlib to prevent build errors.
import matplotlib
matplotlib.use('agg')

# Import yellowbrick information.
import yellowbrick as yb

##########################################################################
## General configuration
##########################################################################

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.8'

# General information about the project.
project = 'Yellowbrick'
copyright = '2016-2019, The scikit-yb developers.'
author = 'The scikit-yb developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
version = yb.get_version(short=True)
# The full version, including alpha/beta/rc tags.
release = "v" + yb.get_version(short=False)

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'numpydoc',
    'matplotlib.sphinxext.plot_directive',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''

# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) for all docs.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

##########################################################################
## Extension Configuration
##########################################################################

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Auto-plot settings either as extension or (file format, dpi)
plot_formats = [
    'png',
    'pdf',
    # ('hires.png', 350),
]

# By default, include the source code generating plots in documentation
plot_include_source = True

# Whether to show a link to the source in HTML.
plot_html_show_source_link = True

# Code that should be executed before each plot.
plot_pre_code = (
    "import numpy as np\n"
    "import matplotlib.pyplot as plt\n"
    "from yellowbrick.datasets import *\n"
)

# Whether to show links to the files in HTML.
plot_html_show_formats = True

# A dictionary containing any non-standard rcParams that should be applied before each plot.
plot_rcparams = {
    "figure.figsize": (9,6),
    "figure.dpi": 128,
}

# Autodoc requires numpy to skip class members otherwise we get an exception:
# toctree contains reference to nonexisting document
# See: https://github.com/phn/pytpm/issues/3#issuecomment-12133978
numpydoc_show_class_members = False

# Locations of objects.inv files for intersphinx extension that auto-links
# to external api docs.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'matplotlib': ('http://matplotlib.org/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'cycler': ('http://matplotlib.org/cycler/', None),
    'sklearn': ('http://scikit-learn.org/stable/', None)
}

##########################################################################
## Options for HTML output
##########################################################################

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = 'yellowbrick v0.1'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = "images/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_stylesheet("theme_overrides.css")

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'yellowbrickdoc'

##########################################################################
## Options for LaTeX output
##########################################################################

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples.
latex_documents = [
    (
        master_doc, # source start file
        'yellowbrick.tex', # target name
        '{} Documentation'.format(project), # title
        author, # author
        'manual' # documentclass [howto,manual, or own class]
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# If false, no module index is generated.
#
# latex_domain_indices = True

##########################################################################
## Options for manual page output
##########################################################################

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        project,
        '{} Documentation'.format(project),
        [author],
        1
    )
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'yellowbrick',
        '{} Documentation'.format(project),
        author,
        'yellowbrick',
        'machine learning visualization',
        'scientific visualization',
    ),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False