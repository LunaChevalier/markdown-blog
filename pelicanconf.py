#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'luna chevalier'
SITENAME = 'luna-chevalier-blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = '../../alexandrevicenzi/Flex/'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.nl2br': {},
        'markdown_del_ins':{},
    },
    'output_format': 'html5',
}

STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'images/favicon.png': {'path': 'favicon.png'}
}

TWITTER_USERNAME = 'Luna_Chevalier'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
