# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.http import Http404

from core.models import Plase


def index(request):
    all_plases = Plase.objects.all()
    template = loader.get_template('index.html')
    context = Context({
        'all_plases': all_plases,
    })
    return HttpResponse(template.render(context))


def plase(request, plase_id):
    try:
        one_plase = Plase.objects.get(id=plase_id)
    except Plase.DoesNotExist:
        raise Http404
    return render(request, 'plase.html', {'plase': one_plase})