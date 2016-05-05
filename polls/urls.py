from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^new/$', views.new, name='new'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^imprint/$', views.imprint, name='imprint'),
)
