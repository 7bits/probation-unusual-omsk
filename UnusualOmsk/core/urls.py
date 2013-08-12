from django.conf.urls import patterns, url

from UnusualOmsk.core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^place/(?P<place_id>\d+)/$', views.place, name='place'),
	url(r'^place/(?P<place_id>\d+)$', views.place, name='place'),
	url(r'^place/', views.index, name='index'),
	url(r'^search/$', views.search_place, name='search'),
	url(r'^map/$',views.placesMap, name='map'),
	url(r'^map$',views.placesMap, name='map'),
	url(r'^about$',views.about, name='about'),
	url(r'^about/$',views.about, name='about'),
)