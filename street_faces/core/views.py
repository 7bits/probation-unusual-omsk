# Create your views here.
import operator
from django.db.models import Q
from street_faces.core.models import place
from street_faces.core.forms import add_place_form
from street_faces.subscription.forms import subscription_form
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def index(request):
    all_places = place.objects.filter(is_visible=True)
    return render(request, 'index.html', {
        'all_places': all_places,
        'subscription_form': subscription_form})


def place_one(request, place_id):
    one_place = get_object_or_404(place, id=place_id, is_visible=True)
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
        places = place.objects.filter(is_visible=True)
    else:
        places = place.objects.filter(reduce(operator.or_, (
                Q(title__icontains=search_word) for search_word in search_text)), is_visible=True)
    return render(request, 'index.html', {
        'all_places': places,
        'subscription_form': subscription_form})


def places_map(request):
    all_places = place.objects.filter(is_visible=True)
    return render(request, 'map.html', {
        'all_places': all_places,
        'subscription_form': subscription_form})


def places_filter(request, filter_id):
    all_places = place.objects.filter(category__category=filter_id, is_visible=True)
    return render(request, 'index.html', {
        'all_places': all_places,
        'subscription_form': subscription_form})


def places_filter_map(request, filter_id):
    all_places = place.objects.filter(category__category=filter_id, is_visible=True)
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


@login_required
def moderation_list(request):
    all_places = place.objects.all()
    return render(request, 'moderation.html', {
        'all_places': all_places,
        'subscription_form': subscription_form,
        })


@csrf_exempt
def moderation(request, place_id):
    if request.method == 'POST':
        if request.POST.get('hide'):
            one_place = get_object_or_404(place, id=place_id)
            one_place.is_visible = False
            one_place.save()
            return redirect('/moderation/')
        if request.POST.get('show'):
            one_place = get_object_or_404(place, id=place_id)
            one_place.is_visible = True
            one_place.save()
            return redirect('/moderation/')
    return redirect('/')
