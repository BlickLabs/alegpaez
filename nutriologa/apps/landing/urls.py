#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex=r'^$',
        view=views.HomeTemplateView.as_view(),
        name='home'),

    url(regex=r'^videos/$',
        view=views.VideosTemplateView.as_view(),
        name='videos'),

    url(regex=r'^contacto/$',
        view=views.ContactTemplateView.as_view(),
        name='contacto'),


    url(regex=r'^send/$',
        view=views.ContactView.as_view(),
        name='email'),

    url(regex=r'^recetas/$',
        view=views.RecipesTemplateView.as_view(),
        name='recetas'),

    url(regex=r'^acerca/$',
        view=views.AboutTemplateView.as_view(),
        name='acerca'),

    url(regex=r'^servicios/$',
        view=views.ServicesTemplateView.as_view(),
        name='servicios'),

]
