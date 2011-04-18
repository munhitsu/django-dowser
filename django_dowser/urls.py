from django.conf.urls.defaults import *
from django.conf import settings

#TODO: remove - unused
urlpatterns = patterns('django_dowser.views',
    url(r'^chart/(?P<typename>[\.\-\w]+)$', 'chart'),
    url(r'^trace/(?P<typename>[\.\-\w]+)(/(?P<objid>\d+))?$', 'trace'),
    url(r'^tree/(?P<typename>[\.\-\w]+)/(?P<objid>\d+)$', 'tree'),
    url(r'^$', 'index'),
)
