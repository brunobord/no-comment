#-*- coding: utf-8 -*-
from os import path
import json
from fabric.api import task, local

__version__ = "0.3"

ROOT_CONF = path.dirname(__file__)
CHROME_DIR = path.join(ROOT_CONF, 'chrome')
FIREFOX_DIR = path.join(ROOT_CONF, 'firefox')
manifest = {
    'name': "No Comment",
    'version': __version__,
}

CSS_PATTERN = """/* Remove comments from %s */
%s {
    display: none !important;
}
"""

FIREFOX_USER_SCRIPT = """// ==UserScript==
// @name No Comment
// @description Remove comments on news websites
// @version %s
%s
// ==/UserScript==

%s
"""

FIREFOX_DOMAIN_STYLE = """@-moz-document domain(%s) {
    %s
}
"""


@task
def build():
    # opening json file
    sites = json.load(open(path.join(ROOT_CONF, 'sites.json')))
    content_scripts = []
    matches = []
    firefox_styles = []
    for site, site_data in sites.items():
        css_path = 'css/%s.css' % site
        matches += site_data['matches']
        content_scripts.append({'matches': site_data['matches'], 'css': [css_path]})
        css_pattern = CSS_PATTERN % (site, ", ".join(site_data['selectors']))
        for domain in site_data['domain']:
            firefox_styles.append(FIREFOX_DOMAIN_STYLE % (domain, css_pattern))
        with open(path.join(CHROME_DIR, css_path), 'w') as css_file:
            # Writing down each css file
            css_file.write(css_pattern)

    manifest["content_scripts"] = content_scripts
    # Dumping to manifest for the Chrome extension
    json.dump(manifest, open(path.join(CHROME_DIR, 'manifest.json'), 'w'), indent=4)

    # firefox build
    with open(path.join(FIREFOX_DIR, 'no-comment.user.js'), 'w') as firefox_file:
        firefox_file.write(FIREFOX_USER_SCRIPT % (
            __version__,
            "\n".join(("// @match %s" % match for match in matches)),
            # It's easier to join the lines in the Greasemonkey script.
            "\n".join(['GM_addStyle("%s");' % style.replace("\n", " ") for style in firefox_styles])
            )
        )
    # Zip the stuff for Chrome
    destination_crx = path.join(ROOT_CONF, 'no-comment.crx')
    local('rm -f %s' % destination_crx)
    local("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --pack-extension=%s --pack-extension-key=%s  --no-message-box"
        % (CHROME_DIR, path.join(ROOT_CONF, 'no-comment.pem')))
    local('mv %s %s' % (path.join(ROOT_CONF, 'chrome.crx'), destination_crx))
