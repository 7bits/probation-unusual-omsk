# Create your views here.
from django.shortcuts import render
import operator
from django.db.models import Q
from street_faces.core.models import place, place_unchecked
from django.shortcuts import get_object_or_404, get_list_or_404
from street_faces.subscription.forms import subscription_form
from street_faces.core.forms import add_place_form
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt


def index(request):
    all_places = place.objects.all()
    return render(request, 'index.html', {
        'all_places': all_places,
        'subscription_form': subscription_form})


def place_one(request, place_id):
    one_place = get_object_or_404(place, id=place_id)
    return render(request, 'place.html', {
        'place': one_place,
        'subscription_form': subscription_form})


def search_place(request):
    if 'search_text' in request.GET and request.GET['search_text']:
        search_text = request.GET['search_text']
        search_text = search_text.split()
    else:
        search_text = ''
    if search_text == '':
        places = place.objects.all()
    else:
        places = place.objects.filter(reduce(operator.or_, (
                Q(title__icontains=search_word) for search_word in search_text)))
    return render(request, 'index.html', {
        'all_places': places,
        'subscription_form': subscription_form})


def places_map(request):
    all_places = place.objects.all()
    return render(request, 'map.html', {
        'all_places': all_places,
        'subscription_form': subscription_form})


def places_filter(request, filter_id):
    all_places = get_list_or_404(place, category=filter_id)
    return render(request, 'index.html', {
        'all_places': all_places,
        'subscription_form': subscription_form})


def places_filter_map(request, filter_id):
    all_places = get_list_or_404(place, category=filter_id)
    return render(request, 'map.html', {
        'all_places': all_places,
        'subscription_form': subscription_form})


@csrf_exempt
def add_place(request):
    if request.method == 'POST':
        form = add_place_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            raise Http404
    return render(request, 'add-place.html', {
        'add_place_form': add_place_form,
        'subscription_form': subscription_form})
