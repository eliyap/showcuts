.. image:: logo.png

Showcuts
########

.. image:: https://readthedocs.org/projects/showcuts/badge/?version=latest
    :target: https://showcuts.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Welcome to the code behind `showcuts.app <https://showcuts.app/share/view>`_, a web viewer for the `iOS Shortcuts App <https://apps.apple.com/us/app/shortcuts/id915249334>`_.

Showcuts turns an iCloud link into a web approximation of the iOS viewer.
This takes a few steps, which developers may find interesting:

   #. Downloading the shortcut's ``.plist`` file (and some metadata) via the iCloud API, as documented by `Sharecuts <https://github.com/sharecuts/website/blob/master/Docs/Download%20shortcut%20shared%20as%20a%20link.txt>`_
   #. Turning the ``.plist`` file into JSON using Python's `plistlib library <https://docs.python.org/2/library/plistlib.html>`_
   #. Parsing the shortcut's actions as Python objects
   #. Displaying those objects as HTML via Django, with
      CSS styles that approximate the appearance of Shortcuts on iOS

**Characteristics**

Other Shortcuts projects and products exist. Showcuts is distinguished by:

   * shows individual actions and parameters of shortcuts
   * visual similarity to Shortcuts on iOS
   * allowing embeds of it's viewer (`JS Fiddle <https://jsfiddle.net/7ok5xfgd/1/>`_)
   * supports Shortcuts for iOS 13
   * is free and open source (premium tier / a tip jar is planned)

Showcuts does not:

   * have a native iOS app (kind of pointless)
   * support iOS 12
   * allow users to edit Shortcuts (this is planned)
   * have an installation / package. I don't think anyone has
     a use for this code, as far as I know.

Status
######

Showcuts was in active development from November 2019 - February 2020.

Development slowed as the author entered college, and may have ceased entirely.
