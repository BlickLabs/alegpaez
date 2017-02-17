#!/usr/bin/env python
# -*- coding: utf-8 -*
import json
import requests

from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import View
from django.core.mail import EmailMultiAlternatives
import urlparse

from django.conf import settings
from nutriologa.apps.wordpress.models import WpPosts, WpPostmeta
from nutriologa.apps.recipes.models import Recipe, Video


class Thumbnail():
    def __init__(self, post_id, url):
        self.post_id = post_id
        self.url = url


class AboutTemplateView(TemplateView):
    template_name = 'acerca.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        return context


class ContactTemplateView(TemplateView):
    template_name = 'contacto.html'

    def get_context_data(self, **kwargs):
        context = super(ContactTemplateView, self).get_context_data(**kwargs)
        return context


class ContactView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ContactView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date = request.POST.get('date')

        ctx = {
            'name': name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'message': message,
            'date': date,
        }

        body = loader.render_to_string('email/contact.html', ctx)

        msg = EmailMultiAlternatives(
            subject="Notificacion de Contacto",
            body="Repleace with HTML",
            from_email="Contacto Desde Pagina Web <postmaster@mg.alegpaez.com>",
            to=[settings.DEFAULT_EMAIL_TO],
        )

        msg.attach_alternative(body, "text/html")

        msg.send()
        response = 'Send'

        return HttpResponse(response)


class ServicesTemplateView(TemplateView):
    template_name = 'servicios.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesTemplateView, self).get_context_data(**kwargs)
        return context


class RecipesTemplateView(ListView):
    template_name = 'recetas.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self, ):
        arg = self.request.GET.get('u')
        if arg:
            queryset = self.model.objects.filter(category=arg).order_by('-date')
        else:
            queryset = self.model.objects.all().order_by('-date')
        return queryset


class VideosTemplateView(TemplateView):
    template_name = 'videos.html'

    def get_context_data(self, **kwargs):
        context = super(VideosTemplateView, self).get_context_data(**kwargs)
        videos = Video.objects.all().order_by('-date')
        context['videos'] = videos
        return context


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        thumbnails = []
        posts = WpPosts.objects.filter(post_status='publish')[:5]
        recipes = Recipe.objects.all().order_by('-date')[:3]
        metas = WpPostmeta.objects.all()
        from datetime import datetime
        for post in posts:
            wp_date = post.post_date
            date_object = str(wp_date.date()).replace('-', '/')
            print date_object
            slug = slugify(post.post_title)
            print slug
            url = '%s/%s/' % (date_object, slug )
            print url
            post.link = url
            for meta in metas:
                if meta.post_id == post.id and meta.meta_key == '_thumbnail_id':
                    thumbnail_id = meta.meta_value
                    thumb = WpPostmeta.objects.get(post_id=thumbnail_id, meta_key='_wp_attached_file')
                    thumbnails.append(Thumbnail(post.id, thumb.meta_value))
        context['posts'] = posts
        context['recipes'] = recipes
        context['thumbnails'] = thumbnails
        context['metas'] = metas
        return context


class NewsletterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(NewsletterView, self)\
            .dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        list_id = settings.NEWSLETTER_LIST_ID
        endpoint = urlparse.urljoin(
            settings.MAILCHIMP_API_ROOT, 'lists/%s/members/' % list_id
        )
        data = {
            "email_address": email,
            "status": "subscribed",
        }
        data = json.dumps(data)
        response = requests.post(
            endpoint, auth=('apikey', settings.MAILCHIMP_API_KEY), data=data)
        return JsonResponse(response.json())
