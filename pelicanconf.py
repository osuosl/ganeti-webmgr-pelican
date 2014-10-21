#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = "content"
AUTHOR = u'OSU Open Source Lab'
SITENAME = u'Ganeti Web Manager'
SITEURL = '/home/lucyw/githubs/ganeti-webmgr-pelican'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Specify name of a theme installed via the pelican-themes tool
THEME = "projectsite-pelican-theme"

# Create navigation bar for theme
MENUITEMS = [('Home', '/index.html')]

SHORTDESC = "Ganeti Web Manager is a Django based web application that allows administrators and clients access to their Ganeti clusters."

HOME_IMAGE = 'images/computer.png'

STATIC_PATHS = ['images']

DOCSURL = 'https://ganeti-webmgr.readthedocs.org/en/latest/'

#Uncomment to include github ribbon
#GITHUB_URL = 

