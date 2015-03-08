from django.conf.urls import patterns, url
from plexrequests import views


urlpatterns = patterns('',
                       url(r'^$', views.search, name='search'),
                       url(r'^results/$', views.results, name='results'),
                       url(r'^add/$', views.add, name='add')
                       )