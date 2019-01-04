from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *

#url for app
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/wakaf_admin'}, name='logout'),
    url(r'^tables/', tables, name='tables'),
    url(r'^uploadFotoDonasi/', uploadFotoDonasi, name='uploadFotoDonasi'),
    url(r'^pageFotoDonasi/', pageFotoDonasi, name='pageFotoDonasi'),
    url(r'^pageCarouselHome/', pageCarouselHome, name='pageCarouselHome'),
    url(r'^deleteCarouselHome/(?P<image_id>[0-9]+)/$', deleteCarouselHome, name='deleteCarouselHome'),
    url(r'^addCarouselHome/', addCarouselHome, name='addCarouselHome'),
    url(r'^pageLayanan/', pageLayanan, name='pageLayanan'),
    url(r'^addLayanan/', addLayanan, name='addLayanan'),
    url(r'^deleteLayanan/(?P<layanan_id>[0-9]+)/$', deleteLayanan, name='deleteLayanan'),
    url(r'^pageEditTesti/', pageEditTesti, name='pageEditTesti'),
    url(r'^addTesti', addTesti, name='addTesti'),
    url(r'^deleteTesti1/(?P<testi_id>[0-9]+)/$', deleteTesti1, name='deleteTesti1'),
    url(r'^deleteTesti2/(?P<testi_id>[0-9]+)/$', deleteTesti2, name='deleteTesti2'),
    url(r'^deleteTesti3/(?P<testi_id>[0-9]+)/$', deleteTesti3, name='deleteTesti3'),
    url(r'^pageProgram/', pageProgram, name='pageProgram'),
    url(r'^addProgram/', addProgram, name='addProgram'),
    url(r'^deleteProgram/(?P<program_id>[0-9]+)/$', deleteProgram, name='deleteProgram')
]