from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list, name='mbr_list'),
    url(r'^members/create/$', views.create, name='mbr_create'),
    url(r'^members/read/(?P<membercode>[0-9]+)?$', views.read, name='mbr_read'),
    url(r'^members/update/(?P<membercode>[0-9]+)?$',
        views.update, name='mbr_update'),
]
