# Create your views here.
from subscription.models import SubscriptionMail
from django.shortcuts import  render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse

#def SubscriptionMailAdd(request):
#	formset = SubscriptionForm(request.POST)
#	newSubscriptionMail = formset.save()
#	return render_to_response('main.html', {'formset': formset})

@csrf_protect
def subscriptionAdd(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            message_status = "ok"
        else:
        	message_status = u"error e-mail"
    return render_to_response('subscription.html', {'message_status': c[message_status]}, RequestContext(request))