# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from street_faces.subscription.models import SubscriptionMail


class subscription_form(ModelForm):
    class Meta:
        model = SubscriptionMail
        widgets = {
            'email': forms.TextInput(attrs={
                'placeholder': u'Введите свой e-mail'}),
        }
