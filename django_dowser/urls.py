try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from . import views

urlpatterns = [
    url(r'^trace/(?P<typename>[\.\-\w]+)$', views.trace, name='dowser_trace_type'),
    url(r'^trace/(?P<typename>[\.\-\w]+)/(?P<objid>\d+)$', views.trace, name='dowser_trace_object'),
    url(r'^tree/(?P<typename>[\.\-\w]+)/(?P<objid>\d+)$', views.tree, name='dowser_tree'),
    url(r'^$', views.index, name='dowser_index'),
]
