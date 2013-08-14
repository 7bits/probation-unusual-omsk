from django.conf.urls import patterns, url

from street_faces.subscription import views

urlpatterns = patterns('',
    url(r'^subscribe/', views.subscription_add, name='subscription'),
)
