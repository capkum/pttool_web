from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<membercode>[0-9]+)?$', views.index, name='tr_index'),
    url(r'^create/?$', views.create, name='tr_index'),
    url(r'^detail/(?P<seq>[0-9]+)?$', views.view, name='tr_view'),
    url(r'^delete/(?P<seq>[0-9]+)?$', views.delete, name='tr_delete'),
]
