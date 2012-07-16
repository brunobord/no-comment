#-*- coding: utf-8 -*-
from os import path
import json

__version__ = "0.1"

ROOT_CONF = path.dirname(__file__)
CHROME_DIR = path.join(ROOT_CONF, '..', 'chrome-extension')
manifest = {
    'name': "No Comment",
    'version': __version__,
}

CSS_PATTERN = """/* Remove comments from %s */
%s {
    display: none
}
"""

def build():
    sites = json.load(open(path.join(ROOT_CONF, 'sites.json')))
    content_scripts = []
    for site, site_data in sites.items():
        css_path = 'css/%s.css' % site
        content_scripts.append({'matches': site_data['matches'], 'css': [css_path]})
        with open(path.join(CHROME_DIR, css_path), 'w') as css_file:
            css_file.write(CSS_PATTERN % (site, ", ".join(site_data['selectors'])))

    manifest["content_scripts"] = content_scripts
    json.dump(manifest, open(path.join(CHROME_DIR, 'manifest.json'), 'w'), indent=4)
