# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from street_faces.subscription.models import subscription_mail


class subscription_form(ModelForm):
    class Meta:
        model = subscription_mail
        widgets = {
            'email': forms.TextInput(attrs={
                'placeholder': u'Введите свой e-mail'}),
        }
