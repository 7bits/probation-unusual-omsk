# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Plase(models.Model):
    title = models.CharField(max_length=128, verbose_name=u"Заголовок")
    #images = models.ImageField(upload_to="images/plases", verbose_name=u"Картинка")
    VISIT = 'VISIT'
    LOOK = 'LOOK'
    WALK = 'WALK'
    CATEGORY_CHOICES = (
        (VISIT, 'Посетить'),
        (LOOK, 'Посмотреть'),
        (WALK, 'Погулять'),
    )
    catagory = models.CharField(max_length=5, choices=CATEGORY_CHOICES, verbose_name=u"Категория")
    address = models.CharField(max_length=128, verbose_name=u"Адрес")
    description = models.TextField(verbose_name=u"Описание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата/время")

    def __unicode__(self):
        return unicode(self.title)