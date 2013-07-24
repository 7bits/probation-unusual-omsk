from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^plase/(?P<plase_id>\d+)/$', views.plase, name='plase'),
	url(r'^plase/(?P<plase_id>\d+)$', views.plase, name='plase'),
	url(r'^plase/', views.index, name='index'),
)