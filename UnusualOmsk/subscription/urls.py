from django.conf.urls import patterns, url

from UnusualOmsk.subscription import views

urlpatterns = patterns('',
	url(r'^subscribe/', views.subscriptionAdd, name='subscription'),
)