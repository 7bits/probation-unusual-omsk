from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^place/(?P<place_id>\d+)/$', views.place, name='plase'),
	url(r'^place/(?P<place_id>\d+)$', views.place, name='plase'),
	url(r'^place/', views.index, name='index'),
)