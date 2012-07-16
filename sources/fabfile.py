#-*- coding: utf-8 -*-
from os import path
import json
from fabric.api import local

__version__ = "0.1"

ROOT_CONF = path.dirname(__file__)
CHROME_DIR = path.join(ROOT_CONF, '..', 'chrome-extension')
manifest = {
    'name': "No Comment",
    'version': __version__,
}


def build():
    sites = json.load(open(path.join(ROOT_CONF, 'sites.json')))
    content_scripts = []
    for site, site_data in sites.items():
        content_scripts.append({'matches': site_data['matches'], 'css': ['css/%s.css' % site]})
    manifest["content_scripts"] = content_scripts
    json.dump(manifest, open(path.join(CHROME_DIR, 'manifest.json'), 'w'), indent=4)
