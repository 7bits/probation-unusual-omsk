# -*- coding: utf-8 -*-
# Create your views here.
from UnusualOmsk.subscription.models import subscription_mail
from UnusualOmsk.subscription.forms import subscription_form
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response


@csrf_exempt
def subscription_add(request):
    if request.POST:
        form = subscription_form(request.POST)
        if form.is_valid():
            form.save()
            message_response = u"Вы успешно подписались"
        else:
            message_response = u"Вы ввели некоректный e-mail"
    return render_to_response('subscription.html',
        {'message_response': message_response})
