# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.http import Http404

from core.models import Place

def index(request):
    all_places = zip(*[iter(Place.objects.all())] * 3)
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

#<a href="{% url 'place' place.id %}"><p>{{ place.title }}</p></a>