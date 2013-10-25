# -*- coding: utf-8 -*-
import json

from street_faces.subscription.forms import subscription_form
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse


@csrf_exempt
def subscription_add(request):
    if request.method == 'POST':
        form = subscription_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({
                'result': 'success'
            }))
        else:
            return HttpResponse(json.dumps({
                'result': 'error'
            }))
    raise Http404
