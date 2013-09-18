from street_faces.subscription.forms import subscription_form
from django.template import RequestContext
from  django.http import HttpResponse
from django.shortcuts import render


class form_middleware(object):
    def process_request(self, request):
    	request.subscription_form = subscription_form
        #response = HttpResponse(response, {'subscription_form': subscription_form})
        #response['subscription_form'] = subscription_form
        #response.context += RequestContext(response, {'subscription_form': subscription_form})
        #response.content = response.content.replace({'subscription_form': subscription_form}) 
        #return response
