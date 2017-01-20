#!/usr/bin/env python
# -*- coding: utf-8 -*
from django.views.generic import TemplateView

from nutriologa.apps.wordpress.models import WpPosts


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        posts = WpPosts.objects.filter(post_status='publish')[:5]
        context['posts'] = posts
        return context