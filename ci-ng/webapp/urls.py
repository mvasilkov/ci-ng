from django.conf.urls import url
from django.contrib import admin

from chrysalis.views import index

urlpatterns = [
    url('^$', index, name='index'),
    url('^admin/', admin.site.urls),
]
