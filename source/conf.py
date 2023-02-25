# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'longhongc.github.io'
copyright = '2023, Chang-Hong Chen'
author = 'Chang-Hong Chen'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

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

html_css_files = ['custom.css']
html_js_files = ['custom.js']

html_logo = 'images/eye_human.png'
html_favicon = 'images/eye.png'


html_show_sourcelink = False
