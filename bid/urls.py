__author__ = 'animesh'
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('bidder',
                       url(r'authenticate/$', 'views.authenticate'),
                       )