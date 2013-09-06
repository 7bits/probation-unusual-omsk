# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from street_faces.core.models import place_no_moderator


class add_place_form(ModelForm):
    class Meta:
        model = place_no_moderator
