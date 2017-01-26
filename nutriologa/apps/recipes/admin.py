#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from nutriologa.apps.recipes.forms import VideoForm
from . import models


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    form = VideoForm


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)