from django.conf.urls.defaults import *

urlpatterns = patterns('django_dowser.views',
    url(r'^trace/(?P<typename>[\.\-\w]+)(/(?P<objid>\d+))?$', 'trace'),
    url(r'^tree/(?P<typename>[\.\-\w]+)/(?P<objid>\d+)$', 'tree'),
    url(r'^$', 'index'),
)
