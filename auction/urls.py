__author__ = 'animesh'
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from auction import auction_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/auctioneers/$',auction_views.AuctioneerUser.as_view()),
    url(r'^api/auction/(?P<id>[0-9]+)/$',auction_views.AuctionDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)