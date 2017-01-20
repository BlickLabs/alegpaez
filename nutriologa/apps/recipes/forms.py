#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from nutriologa.apps.recipes.models import Video

class VideoForm(forms.ModelForm):

    def save(self, commit=True):
        m = super(VideoForm, self).save(commit=False)
        m.youtube_video_id = m.youtube_video_url.split('/embed/')[1]
        if commit:
            m.save()
        return m

    def clean_youtube_video_url(self):
        cleaned_data = super(VideoForm, self).clean()
        url = cleaned_data.get('youtube_video_url')
        if 'embed' in url:
            embed_url = url
        elif url == '':
            embed_url = ''
        else:
            try:
                arg = url.split('=')[1]
                embed_url = 'https://www.youtube.com/embed/%s' % arg
            except:
                raise forms.ValidationError('Inserte un link de la forma https://www.youtube.com/watch?v=IVembed_url6ZlksMJw')
        return embed_url

    class Meta:
        model = Video
        fields = ['title', 'youtube_video_url', ]