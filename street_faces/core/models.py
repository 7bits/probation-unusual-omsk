# -*- coding: utf-8 -*-
from django.db import models
from django import forms
# Create your models here.


class place_category(models.Model):
    category = models.CharField(max_length=128, verbose_name=u"Категория")

    def __unicode__(self):
        return unicode(self.category)

class place(models.Model):
    title = models.CharField(max_length=128, verbose_name=u"Заголовок")
    image = models.ImageField(upload_to="./", verbose_name=u"Картинка")
    category = models.ForeignKey(place_category)
    address = models.CharField(max_length=128, verbose_name=u"Адрес")
    latitude = models.CharField(max_length=9, verbose_name=u"Широта")
    longitude = models.CharField(max_length=9, verbose_name=u"Долгота")
    description = models.TextField(verbose_name=u"Описание")
    pub_date = models.DateTimeField(auto_now_add=True,
        verbose_name=u"Дата/время")

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        abstract = True

class place_unchecked(place):
    class Meta:
        verbose_name_plural = u"не добавленные места"


class place_checked(place):
    class Meta:
        verbose_name_plural = u"добавленные места"