# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from street_faces.core.models import Place


class AddPlaceForm(ModelForm):
    class Meta:
        model = Place
        exclude = ('is_visible',)
