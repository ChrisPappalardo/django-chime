# -*- coding: utf-8 -*-

'''
Top-level package for django-chime.
'''

import logging


__author__ = 'Chris Pappalardo'
__email__ = 'cpappala@gmail.com'
__version__ = '0.2.2'


# set penn_chime log level to something less chatty
logging.getLogger('penn_chime.models').setLevel(logging.WARNING)
