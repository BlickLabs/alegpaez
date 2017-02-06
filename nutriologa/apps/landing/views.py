#!/usr/bin/env python
# -*- coding: utf-8 -*
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import View
from django.core.mail import EmailMultiAlternatives

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
            from_email="Contacto Desde Pagina Web <postmaster@alegpaez.com>",
            to=[settings.DEFAULT_EMAIL_TO],
        )

        msg.attach_alternative(body, "text/html")

        try:
            msg.send()
            response = 'Send'
        except:
            response = 'Not Send'

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
        metas = WpPostmeta.objects.all()
        for post in posts:
            for meta in metas:
                if meta.post_id == post.id and meta.meta_key == '_thumbnail_id':
                    thumbnail_id = meta.meta_value
                    thumb = WpPostmeta.objects.get(post_id=thumbnail_id, meta_key='_wp_attached_file')
                    thumbnails.append(Thumbnail(post.id, thumb.meta_value))
        context['posts'] = posts
        context['thumbnails'] = thumbnails
        context['metas'] = metas
        return context
