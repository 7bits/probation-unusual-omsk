from django.conf.urls import patterns, url

from street_faces.subscription import ajax

urlpatterns = patterns('',
    url(r'^subscribe/', ajax.subscription_add, name='subscription'),
)
