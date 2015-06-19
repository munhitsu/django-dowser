try:
    from django.conf.urls import *
except ImportError:
    from django.conf.urls.defaults import *


urlpatterns = patterns('django_dowser.views',
    url(r'^trace/(?P<typename>[\.\-\w]+)$', 'trace', name='dowser_trace_type'),
    url(r'^trace/(?P<typename>[\.\-\w]+)/(?P<objid>\d+)$', 'trace', name='dowser_trace_object'),
    url(r'^tree/(?P<typename>[\.\-\w]+)/(?P<objid>\d+)$', 'tree', name='dowser_tree'),
    url(r'^$', 'index', name='dowser_index'),
)
