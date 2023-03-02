# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'longhongc.github.io'
copyright = '2023, Chang-Hong Chen'
author = 'Chang-Hong Chen'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx_design',
  'myst_parser',
  'sphinx_new_tab_link',
  'sphinx.ext.mathjax',
  'sphinx-mathjax-offline'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'prev_next_buttons_location': 'None',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
}

# html_theme = 'otc_tcs_sphinx_theme'
# html_theme_path = ['_themes']
html_static_path = ['_static']

html_css_files = [
  'custom.css'
]

html_js_files = ['custom.js']

html_logo = 'images/eye_human.png'
html_favicon = 'images/eye.png'

html_show_sourcelink = False

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "longhongc", # Username
    "github_repo": "longhongc.github.io", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]
