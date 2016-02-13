'Debug settings'

import platform

from .base import *

DEBUG = True

SECRET_KEY = 'x86-64 (also known as x64, x86_64 and AMD64) is the 64-bit version of the x86 instruction set.'

INSTALLED_APPS.append('debug_toolbar')

def debug_toolbar_callback(request):
    'Whether the toolbar should show or not'
    return not request.is_ajax() and not request.path.startswith('/admin/')

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/jquery/dist/jquery.min.js',
    'SHOW_TOOLBAR_CALLBACK': debug_toolbar_callback,
}

if platform.system() == 'Windows':
    NPM_EXECUTABLE_PATH = r'C:\Program Files (x86)\nodejs\node_modules\npm\bin\npm.cmd'
