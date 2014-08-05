#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anthony Cassaigne'
SITENAME = u'Agilit\xe9 - Software Craftsmanship'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Are You Agile', 'http://www.areyouagile.com/'),
          ('Agilitateur ', 'http://agilitateur.azeau.com/'),
          ('Claude Aubry ', 'http://www.aubryconseil.com/'),
          ('Thierry Cros', 'http://thierrycros.net/'),
          ('Crafting Labs', 'https://blog.crafting-labs.fr/'),
          ('Jean-Baptiste Dusseaut', 'http://bodysplash.fr/'),
          ('Jérôme Avoustin', 'http://blog.avoustin.com/'),
          ('Fabrice Aimetti', 'http://www.fabrice-aimetti.fr/'),
          ('Bruno Sbille', 'http://brunosbille.com/'),
          ('Nicolas Deverge', 'https://twitter.com/ndeverge'),
          ('Laurent Morisseau', 'http://www.morisseauconsulting.com/'),
          ('Laurent Carbonnaux', 'http://lolcx.blogspot.fr/'),
          ('Alexis Monville', 'http://ayeba.fr/ayeba/equipe/alexis/'),
          ('Alexandre Boutin', 'http://www.agilex.fr/'),
          ('Romain Couturier', 'http://www.terredagile.com/'),
          ('Ron Jeffries', 'http://xprogramming.com/index.php'),
          ('Martin Fowler','http://martinfowler.com/'),
          ('Henrik Kniberg', 'http://blog.crisp.se/author/henrikkniberg'),
          )

# Social widget
SOCIAL = (('twitter acassaigne', 'https://twitter.com/acassaigne'),
          ('github acassaigne', 'https://github.com/acassaigne'),)

DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS='UA-53235336-1'

TWITTER_USERNAME = 'acassaigne'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 50
