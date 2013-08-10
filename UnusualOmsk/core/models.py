# -*- coding: utf-8 -*-
from django.db import models
from django import forms
# Create your models here.

class Place(models.Model):
    title = models.CharField(max_length=128, verbose_name=u"Заголовок")
    image = models.ImageField(upload_to="./", verbose_name=u"Картинка")
    GRAFFITI = 'GRAFFITI'
    INTERIOR = 'LOOK'
    MONUMENTS = 'MONUMENTS'
    ARCHITECTURE = 'ARCHITECTURE'
    CATEGORY_CHOICES = (
        (GRAFFITI, 'Граффити'),
        (INTERIOR, 'Интерьер'),
        (MONUMENTS, 'Памятники'),
        (ARCHITECTURE, 'Архитектура'),
    )
    catagory = models.CharField(max_length=12, choices=CATEGORY_CHOICES, verbose_name=u"Категория")
    address = models.CharField(max_length=128, verbose_name=u"Адрес")
    latitude = models.CharField(max_length=9, verbose_name=u"Широта")
    longitude = models.CharField(max_length=9, verbose_name=u"Долгота")
    description = models.TextField(verbose_name=u"Описание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата/время")

    def __unicode__(self):
        return unicode(self.title)

#class PlaceImage(models.Model):
#    place = models.ForeignKey(Place)
#    image = models.ImageField(upload_to="./", verbose_name=u"Картинка")
#
#    def __unicode__(self):
#        return unicode(self.place)