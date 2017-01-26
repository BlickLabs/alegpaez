#!/usr/bin/env python
# -*- coding: utf-8 -*
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _



class Video(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=500,
        blank=False,
        null=False,
    )

    youtube_video_url = models.CharField(
        verbose_name=_('Youtube URL'),
        blank=False,
        null=False,
        max_length=100,
    )

    youtube_video_id = models.CharField(
        verbose_name=_('Youtube video ID'),
        blank=True,
        null=True,
        max_length=100,
    )

    date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('videos')

    def __str__(self):
        return self.title


class Recipe(models.Model):

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=500,
        blank=False,
        null=False,
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        blank=False,
        null=False,
        upload_to='recipes',
    )

    description = models.TextField(
        verbose_name=_('Description'),
        blank=False,
        null=False,
    )

    category = models.CharField(
        verbose_name=_('Category'),
        max_length=50,
        blank=False,
        null=False,
        choices=(
            ('breakfast', 'Desayuno'),
            ('collation', 'Colaciones'),
            ('meal', 'Comidas'),
            ('dinner', 'Cenas'),
        )
    )

    date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipes')

    def __str__(self):
        return self.title