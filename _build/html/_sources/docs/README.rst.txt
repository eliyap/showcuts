.. image:: logo.png

Showcuts
########

Welcome to the code for `showcuts.app <https://showcuts.app/share/view>`_, a web viewer for the `iOS Shortcuts App <https://apps.apple.com/us/app/shortcuts/id915249334>`_.

Showcuts turns an iCloud link into a HTML + CSS approximation of the iOS Shortcuts viewer.
This takes a few steps, which developers may find useful:
 #. Download the shortcut's ``.plist`` file (and some details) via the iCloud API, as documented by `Sharecuts <https://github.com/sharecuts/website/blob/master/Docs/Download%20shortcut%20shared%20as%20a%20link.txt>`_
 #. Turn the ``.plist`` file into JSON using Python's `plistlib library <https://docs.python.org/2/library/plistlib.html>`_
 #. Parsing the shortcut's actions as Python objects
 #. Turning those objects into HTML via Django's templating engine

 * also, CSS styles that approximate the appearance of Shortcuts on iOS

**Characteristics**

Other Shortcuts projects and products exist. Showcuts is special because it:

 * shows the individual actions and parameters of shortcuts
 * aims to look like Shortcuts on iOS
 * allows others to embed it's viewer in their sites (`JS Fiddle <https://jsfiddle.net/7ok5xfgd/1/>`_)
 * supports Shortcuts for iOS 13 (not iOS 12)
 * is free and open source (premium tier / a tip jar is planned)

Showcuts does not:

 * have a native iOS app (it would be kind of pointless)
 * support iOS 12
 * allow users to edit Shortcuts (yet!)
 * have an installation, as I don't think anyone has a use for this code (happy to be proven wrong there!)

Status
######

Showcuts was in active development from November - December 2019. 

Development slowed as the author entered college, and may have ceased entirely.