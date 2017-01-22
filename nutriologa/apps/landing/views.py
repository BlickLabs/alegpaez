#!/usr/bin/env python
# -*- coding: utf-8 -*
from django.views.generic import TemplateView

from nutriologa.apps.wordpress.models import WpPosts, WpPostmeta


class Thumbnail():
    def __init__(self, post_id, url):
        self.post_id = post_id
        self.url = url


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