from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^coupler/list/$', views.coupler_list, name='coupler_list'),
    url(r'^coupler/create/$', views.coupler_create, name='coupler_create'),
    url(r'^coupler/(?P<coupler_id>[0-9]+)/edit/$', views.coupler_edit, name='coupler_edit'),
    url(r'^coupler/(?P<coupler_id>[0-9]+)/delete/$', views.coupler_delete, name='coupler_delete'),

    url(r'^manufacturer/list/$', views.manufacturer_list, name='manufacturer_list'),
    url(r'^manufacturer/create/$', views.manufacturer_create, name='manufacturer_create'),
    url(r'^manufacturer/(?P<manufacturer_id>[0-9]+)/edit/$', views.manufacturer_edit, name='manufacturer_edit'),
    url(r'^manufacturer/(?P<manufacturer_id>[0-9]+)/delete/$', views.manufacturer_delete, name='manufacturer_delete'),

    url(r'^railroad/list/$', views.railroad_list, name='railroad_list'),
    url(r'^railroad/create/$', views.railroad_create, name='railroad_create'),
    url(r'^railroad/(?P<railroad_id>[0-9]+)/edit/$', views.railroad_edit, name='railroad_edit'),
    url(r'^railroad/(?P<railroad_id>[0-9]+)/delete/$', views.railroad_delete, name='railroad_delete'),
]
