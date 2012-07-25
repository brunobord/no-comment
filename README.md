# No comment

A collection of Userstyles to remove comments on various websites. My primary
target is French online newspapers, but I'm pretty sure you'll love to activate
it on your favorite website.

----

## Install

### On Chrome

#### Git clone

You may eventually clone this repository via the following command line::

    git clone https://github.com/brunobord/no-comment.git

Then you'll have to add the chrome extension via:

    Wrench Button -> Tools -> Extensions -> Load Unpacked Extension

Pick the "chrome" directory and there you are.

#### Online install

Or you can install it by pointing your webkit browser to:

    http://brunobord.github.com/no-comment/no-comment.crx

And proceed with the installation.

Please note that this archive may not be updated as frequently as you may want.

### On Firefox

As a prerequisite, you'll **need** to install [Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/)
first.

#### Git clone

Then you'll have to grab the custom userscript. Eventually, you can clone the
repository as indicated in the Chrome procedure, and in Firefox, do:

    File -> Open

And pick the no-comment.user.js available in the "firefox" directory.

#### Online script install

Alternatively, you can point your browser to this URL:
    
    http://brunobord.github.com/no-comment/no-comment.user.js

Please note that this archive may not be updated as frequently as you may want.


## Target websites

* sudouest.fr,
* lefigaro.fr,
* lemonde.fr,
* fr.news.yahoo.com,
* ladepeche.fr,
* humanite.fr,
* lesechos.fr,
* nouvelobs.com,
* leparisien.fr,
* lepoint.fr,
* francefootball.fr,
* lequipe.fr,
* rue89.com,
* youtube.com (yes, that'd mean an insane amount of rubbish out of your sight)

(to be continued)

----

## Contribute

If you want to contribute, you have several choices:

### Issue reporting

Something can go wrong... Something **will** go wrong. Please report it on the
appropriate [github issue tracker](https://github.com/brunobord/no-comment/issues).

If you're pissed off by some news website commenters,
[please report it](https://github.com/brunobord/no-comment/issues) and if
possible, we may zap the comment blocks and publish an updated version of the
Firefox / Chrome extension.

If you have a feature request, please submit an issue and we'll try to do our
best to help you out.

### Fork / Pull requests

If you want, you can fork this repository, and, according to the License (see
below), you can do whatever you want with it. Of course, we do accept legit 
pull requests, as long as they improve this extension.

#### Requisites

You'll have to install Fabric. In a virtualenv or globally:

    pip install fabric

#### Add a website

If you want to add a website, edit the ``sites.json`` file and add a block like
this:

```json
    "mywebsite": {
        "matches": ["http://*.example.com/*"],
        "domain": ["example.com"],
        "selectors": ["#comment"]
    }
```

When you're done, run:

    fab build

This will produce a ``mywebsite.css`` file in the ``chrome/css`` directory and
modify the other files (manifest.json and the GreaseMonkey userscript).

Test and double-check that your extension is working by installing the
GreaseMonkey userscript in your Firefox and/or loading the "unpacked" extension
in your Chrome browser. Once you're done, push everything with a nice commit
message, and call for a pull request.

#### Other "TODOs"

"No Comment" is only available for Chrome and Firefox. This needs to be extended
to other browsers. If you know how to (simply) implement this extension for other
browsers, please get in touch with us via the Github Issues and we'll try to
spread happiness and joy around us.

----

## License

This piece of Software is released under the terms of the WTFPL. See
http://sam.zoy.org/wtfpl/ for further details. But, basically:



    DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

    0. You just DO WHAT THE FUCK YOU WANT TO. 
    
    