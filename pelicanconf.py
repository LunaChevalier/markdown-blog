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
LINKS = (
    ('Twitter', 'https://twitter.com/luna_chevalier/'),
    ('Youtube', 'https://www.youtube.com/channel/UC5Ptllp2bi1U7KMRLeVwjmw'),
    ('zenn', 'https://zenn.dev/luna_chevalier'),
)

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
        'markdown.extensions.toc':{},
    },
    'output_format': 'html5',
}

FAVICON = SITEURL + 'images/favicon.ico'
TWITTER_USERNAME = 'Luna_Chevalier'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PORT = 1234
