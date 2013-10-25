# -*- coding: utf-8 -*-
# Create your views here.
import operator
import json

from django.db.models import Q
from street_faces.core.models import Place
from street_faces.core.forms import AddPlaceForm
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers


def paginator_place(place_list, page, number_of_places):
    paginator = Paginator(place_list, number_of_places)
    try:
        places = paginator.page(page)
    except PageNotAnInteger:
        places = paginator.page(1)
    except EmptyPage:
        places = paginator.page(paginator.num_pages)
    return places


def index(request):
    all_places = Place.objects.filter(is_visible=True)
    page = request.GET.get('page')
    places = paginator_place(all_places, page, 12)
    return render(request, 'index.html', {
        'all_places': places})


def place_one(request, place_id):
    one_place = get_object_or_404(Place, id=place_id, is_visible=True)
    if request.is_ajax():
        place_json = serializers.serialize("json", [one_place])
        json_data = json.dumps({'place': place_json})
        return HttpResponse(json_data, mimetype="application/javascript")
    else:
        return render(request, 'place.html', {
            'place': one_place})


def search_place(request):
    search_text = request.GET.get('search-text', '')
    if search_text == '':
        places = Place.objects.filter(is_visible=True)
        search_request = ''
    else:
        search_request = 'search-text=' + search_text + '&'
        search_text = search_text.split()
        places = Place.objects.filter(reduce(operator.or_, (
            Q(title__icontains=search_word)
            for search_word in search_text)), is_visible=True)
    page = request.GET.get('page')
    places = paginator_place(places, page, 12)
    return render(request, 'index.html', {
        'all_places': places,
        'search_request': search_request})


def places_map(request):
    all_places = Place.objects.filter(is_visible=True)
    if request.is_ajax():
        places_json = serializers.serialize("json", all_places)
        json_data = json.dumps({'all_places': places_json})
        return HttpResponse(json_data, mimetype="application/javascript")
    else:
        return render(request, 'map.html', dict(all_places=all_places))


def places_filter(request, filter_id):
    #if request.META['HTTP_REFERER'].find('/map/') != -1:
    #    return redirect('/map/filter/' + filter_id)
    all_places = Place.objects.filter(category__category_url=filter_id,
                                      is_visible=True)
    page = request.GET.get('page')
    places = paginator_place(all_places, page, 12)
    return render(request, 'index.html', {
        'all_places': places})


def places_filter_map(request, filter_id):
    all_places = Place.objects.filter(category__category_url=filter_id,
                                      is_visible=True)
    return render(request, 'map.html', {
        'all_places': all_places})


@csrf_exempt
def add_place(request):
    if request.method == 'POST':
        form = AddPlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Место успешно добавлено')
        else:
            messages.error(request, 'Не все поля заполнены верно')
    return render(request, 'add-place.html', {
        'add_place_form': AddPlaceForm})


@login_required
def moderation_list(request):
    if request.user.has_perm('core.can_moderate'):
        all_places = Place.objects.all()
        if request.is_ajax():
            places_json = serializers.serialize("json", all_places)
            json_data = json.dumps({'all_places': places_json})
            return HttpResponse(json_data, mimetype="application/javascript")
        else:
            return render(request, 'moderation.html', {
                'all_places': all_places})
    else:
        raise Http404  # добавить ошибку


@permission_required('core.can_moderate')
@csrf_exempt
def moderation(request, place_id):
    if request.method == 'POST':
        if request.POST.get('hide'):
            one_place = get_object_or_404(Place, id=place_id)
            one_place.is_visible = False
            one_place.save()
            return redirect('/moderation/')
        if request.POST.get('show'):
            one_place = get_object_or_404(Place, id=place_id)
            one_place.is_visible = True
            one_place.save()
            return redirect('/moderation/')
    return redirect('/')
