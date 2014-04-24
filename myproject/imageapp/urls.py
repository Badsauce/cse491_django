# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.imageapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^details/(\d+)/$', 'details', name='details'),
    url(r'^thumbnails/$', 'thumbnails', name='thumbnails')
)
