from django.conf.urls import url
from . import views

urlpatterns = [
    url('^(?P<pk>[0-9]+)?$', views.index, name='cardio'),
]
