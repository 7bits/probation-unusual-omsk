# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
import operator
from django.db.models import Q

from UnusualOmsk.core.models import Place

def index(request):
    #all_places = zip(*[iter(Place.objects.all())] * 3)
    all_places = Place.objects.all()
    template = loader.get_template('index.html')
    context = Context({
        'all_places': all_places,
    })
    return HttpResponse(template.render(context))


def place(request, place_id):
    try:
        one_place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        raise Http404
    return render(request, 'place.html', {'place': one_place})


def search_place(request):
    #search_text = {}
    #search_text.update(csrf(request))
    if 'search_text' in request.GET and request.GET['search_text']:
        search_text = request.GET['search_text']
        search_text = search_text.split()
        places = Place.objects.filter(reduce(operator.or_, (Q(title__icontains=search_word) for search_word in search_text)))
    else:
        search_text = ''
    return render_to_response('search.html', {'places': places})

def placesMap(request):
    all_places = Place.objects.all()
    template = loader.get_template('map.html')
    context = Context({
        'all_places': all_places,
    })
    return HttpResponse(template.render(context))

def about(request):
    return render_to_response('about.html')