# -*- coding: utf-8 -*-
from django.db import models


class PlaceCategory(models.Model):
    category = models.CharField(max_length=128, verbose_name=u"Категория")

    def __unicode__(self):
        return unicode(self.category)


class Place(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name=u"Заголовок")
    image = models.ImageField(upload_to="./",
                              verbose_name=u"Картинка")
    category = models.ForeignKey(PlaceCategory)
    address = models.CharField(max_length=128,
                               verbose_name=u"Адрес")
    latitude = models.CharField(max_length=9,
                                verbose_name=u"Широта")
    longitude = models.CharField(max_length=9,
                                 verbose_name=u"Долгота")
    description = models.TextField(
        verbose_name=u"Описание")
    is_visible = models.BooleanField(default=False,
                                     verbose_name=u"Опубликовано")
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u"Дата/время")

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        permissions = (
            ("can_moderate", "Может модерировать"),
        )
