from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from UnusualOmsk.core import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^place/(?P<place_id>\d+)/$', views.place_one, name='place'),
    url(r'^place/', views.index, name='index'),
    url(r'^search/$', views.search_place, name='search'),
    url(r'^map/$', views.places_map, name='map'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
)
