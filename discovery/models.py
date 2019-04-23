# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

GENRE_TYPES = (
    ('RK', 'Rock'),
    ('JZ', 'Jazz'),
    ('MT', 'Metal'),
)


class Guitar(models.Model):
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=5, choices=GENRE_TYPES, default='Rock')
    price = models.FloatField()
    semi_acoustic = models.BooleanField(default=False)
    capt_num = models.IntegerField(default=1)