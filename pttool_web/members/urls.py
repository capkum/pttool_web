from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list, name='mbr_list'),
    url(r'^read/(?P<membercode>[0-9]+)?$', views.read, name='mbr_read'),
    url(r'^create/$', views.create, name='mbr_create'),
]
