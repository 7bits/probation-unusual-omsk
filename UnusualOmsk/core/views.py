# Create your views here.
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
import operator
from django.db.models import Q
from UnusualOmsk.core.models import Place
from django.shortcuts import get_object_or_404


def index(request):
    all_places = Place.objects.all()
    return render(request, 'index.html', {
        'all_places': all_places})


def place(request, place_id):
    one_place = get_object_or_404(Place, id=place_id)
    return render(request, 'place.html', {
        'place': one_place})


def search_place(request):
    if 'search_text' in request.GET and request.GET['search_text']:
        search_text = request.GET['search_text']
        search_text = search_text.split()
        places = Place.objects.filter(reduce(operator.or_, (
            Q(title__icontains=search_word) for search_word in search_text)))
    else:
        search_text = ''
    return render_to_response('search.html', {'places': places})


def placesMap(request):
    all_places = Place.objects.all()
    return render(request, 'map.html', {
        'all_places': all_places})
