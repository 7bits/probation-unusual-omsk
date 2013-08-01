from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^place/(?P<place_id>\d+)/$', views.place, name='place'),
	url(r'^place/(?P<place_id>\d+)$', views.place, name='place'),
	url(r'^place/', views.index, name='index'),
	url(r'^search/$', views.search_place, name='search'),
)