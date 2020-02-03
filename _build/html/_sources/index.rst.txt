.. Showcuts documentation master file, created by
   sphinx-quickstart on Mon Dec 30 10:08:55 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the Showcuts documentation!
======================================

Welcome to the code behind `showcuts.app <https://showcuts.app/share/view>`_,
a web viewer for the `iOS Shortcuts App <https://apps.apple.com/us/app/shortcuts/id915249334>`_.

Showcuts is based on Python & Django.

.. toctree::
   :maxdepth: 2
   :caption: Action & Parameter Classes:

   actions
   parameters
   helpers

.. toctree::
   :maxdepth: 2
   :caption: Supported Actions:

   tracking

.. toctree::
   :maxdepth: 2
   :caption: Roadmap:

   roadmap

Showcuts Dependencies
=====================
* Python & Packages
    * Django 2.x
    * social-django `https://github.com/python-social-auth/social-app-django`
    * django-compressor `https://pypi.org/project/django-compressor/`
    * postgres, for some reason. https://pypi.org/project/psycopg2/
    * django-libsass
    * django_compressor
    * plistlib (Python)
* JS
    * jQuery
    * screenshot
    * save file

Docs Dependencies
=================
* sphinx
* recommonmark

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
