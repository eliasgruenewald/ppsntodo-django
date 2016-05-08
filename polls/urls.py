from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^new/$', views.new, name='new'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^overEdit/$', views.overEdit, name='overEdit'),
    url(r'^update/$', views.update, name='update'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^imprint/$', views.imprint, name='imprint'),

)
