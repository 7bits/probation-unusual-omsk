# -*- coding: utf-8 -*-
# Create your views here.
from street_faces.subscription.models import subscription_mail
from street_faces.subscription.forms import subscription_form
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from django.utils import simplejson

@csrf_exempt
def subscription_add(request):
    if request.method == 'POST':
        form = subscription_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(simplejson.dumps({
                'result': 'success'
                }))
        else:
            return HttpResponse(simplejson.dumps({
                'result': 'error'
                }))
    raise Http404
