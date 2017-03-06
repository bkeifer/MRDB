from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^car/list/$', views.car_list, name='car_list'),
    url(r'^car/create/$', views.car_create, name='car_create'),
    url(r'^car/(?P<car_id>[0-9]+)/edit/$', views.car_edit, name='car_edit'),
    url(r'^car/(?P<car_id>[0-9]+)/delete/$', views.car_delete, name='car_delete'),

    url(r'^carfeature/list/$', views.carfeature_list, name='carfeature_list'),
    url(r'^carfeature/create/$', views.carfeature_create, name='carfeature_create'),
    url(r'^carfeature/(?P<carfeature_id>[0-9]+)/edit/$', views.carfeature_edit, name='carfeature_edit'),
    url(r'^carfeature/(?P<carfeature_id>[0-9]+)/delete/$', views.carfeature_delete, name='carfeature_delete'),

    url(r'^cartype/list/$', views.cartype_list, name='cartype_list'),
    url(r'^cartype/create/$', views.cartype_create, name='cartype_create'),
    url(r'^cartype/(?P<cartype_id>[0-9]+)/edit/$', views.cartype_edit, name='cartype_edit'),
    url(r'^cartype/(?P<cartype_id>[0-9]+)/delete/$', views.cartype_delete, name='cartype_delete'),

    url(r'^coupler/list/$', views.coupler_list, name='coupler_list'),
    url(r'^coupler/create/$', views.coupler_create, name='coupler_create'),
    url(r'^coupler/(?P<coupler_id>[0-9]+)/edit/$', views.coupler_edit, name='coupler_edit'),
    url(r'^coupler/(?P<coupler_id>[0-9]+)/delete/$', views.coupler_delete, name='coupler_delete'),

    url(r'^locomotive/list/$', views.locomotive_list, name='locomotive_list'),
    url(r'^locomotive/create/$', views.locomotive_create, name='locomotive_create'),
    url(r'^locomotive/(?P<locomotive_id>[0-9]+)/edit/$', views.locomotive_edit, name='locomotive_edit'),
    url(r'^locomotive/(?P<locomotive_id>[0-9]+)/delete/$', views.locomotive_delete, name='locomotive_delete'),

    url(r'^make/list/$', views.make_list, name='make_list'),
    url(r'^make/create/$', views.make_create, name='make_create'),
    url(r'^make/(?P<make_id>[0-9]+)/edit/$', views.make_edit, name='make_edit'),
    url(r'^make/(?P<make_id>[0-9]+)/delete/$', views.make_delete, name='make_delete'),

    url(r'^manufacturer/list/$', views.manufacturer_list, name='manufacturer_list'),
    url(r'^manufacturer/create/$', views.manufacturer_create, name='manufacturer_create'),
    url(r'^manufacturer/(?P<manufacturer_id>[0-9]+)/edit/$', views.manufacturer_edit, name='manufacturer_edit'),
    url(r'^manufacturer/(?P<manufacturer_id>[0-9]+)/delete/$', views.manufacturer_delete, name='manufacturer_delete'),

    url(r'^model/list/$', views.model_list, name='model_list'),
    url(r'^model/create/$', views.model_create, name='model_create'),
    url(r'^model/(?P<model_id>[0-9]+)/edit/$', views.model_edit, name='model_edit'),
    url(r'^model/(?P<model_id>[0-9]+)/delete/$', views.model_delete, name='model_delete'),

    url(r'^power/list/$', views.power_list, name='power_list'),
    url(r'^power/create/$', views.power_create, name='power_create'),
    url(r'^power/(?P<power_id>[0-9]+)/edit/$', views.power_edit, name='power_edit'),
    url(r'^power/(?P<power_id>[0-9]+)/delete/$', views.power_delete, name='power_delete'),

    url(r'^railroad/list/$', views.railroad_list, name='railroad_list'),
    url(r'^railroad/create/$', views.railroad_create, name='railroad_create'),
    url(r'^railroad/(?P<railroad_id>[0-9]+)/edit/$', views.railroad_edit, name='railroad_edit'),
    url(r'^railroad/(?P<railroad_id>[0-9]+)/delete/$', views.railroad_delete, name='railroad_delete'),
]
