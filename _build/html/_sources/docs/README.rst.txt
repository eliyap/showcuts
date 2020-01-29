.. image:: logo.png

Showcuts
########

.. image:: https://readthedocs.org/projects/showcuts/badge/?version=latest
    :target: https://showcuts.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Welcome to the code behind `showcuts.app <https://showcuts.app/share/view>`_, a web viewer for the `iOS Shortcuts App <https://apps.apple.com/us/app/shortcuts/id915249334>`_.

Showcuts turns an iCloud link into a web approximation of the iOS viewer.
This takes a few steps, which developers may find useful:

   #. Download the shortcut's ``.plist`` file (and some details)
     via the iCloud API, as documented by `Sharecuts <https://github.com/sharecuts/website/blob/master/Docs/Download%20shortcut%20shared%20as%20a%20link.txt>`_
   #. Turn the ``.plist`` file into JSON using Python's
     `plistlib library <https://docs.python.org/2/library/plistlib.html>`_
   #. Parse the shortcut's actions as Python objects
   #. Turn those objects into HTML via Django's templating engine

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
   * have an installation, as I don't think anyone has
     a use for this code (happy to be proven wrong there!)

Status
######

Showcuts was in active development from November 2019 - January 2020.

Development slowed as the author entered college, and may have ceased entirely.
