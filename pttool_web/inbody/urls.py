from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='inbody_index'),
    url(r'create/$', views.create, name='inbody_create'),
    url(r'read/$', views.read, name='inbody_read'),
    url(r'update/$', views.update, name='inbody_update'),
    url(r'delete/$', views.delete, name='inbody_delete'),
    url(r'measure/$', views.measure, name='inbody_measure'),
]
