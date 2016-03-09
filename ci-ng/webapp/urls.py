from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from chrysalis.views import index

urlpatterns = [
    url('^$', index, name='index'),
    url('^admin/', admin.site.urls),
]

if settings.DEBUG and not settings.DEBUG_TOOLBAR_PATCH_SETTINGS:
    import debug_toolbar

    urlpatterns.insert(0, url('^__debug__/', include(debug_toolbar.urls)))
