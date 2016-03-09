'Debug settings'

import platform

from .base import *

DEBUG = True

SECRET_KEY = 'x86-64 (also known as x64, x86_64 and AMD64) is the 64-bit version of the x86 instruction set.'


# Debug toolbar
# http://django-debug-toolbar.readthedocs.org/en/1.4/installation.html

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/jquery/dist/jquery.min.js',
}


# Other settings

if platform.system() == 'Windows':
    NPM_EXECUTABLE_PATH = r'C:\Program Files\nodejs\node_modules\npm\bin\npm.cmd'
