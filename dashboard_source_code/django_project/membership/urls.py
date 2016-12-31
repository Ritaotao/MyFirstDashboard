from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^download/$', views.download, name='download'),
    url(r'^insight/$', views.insight, name='insight'),
    url(r'^detail/$', views.detail, name='detail'),
    ]