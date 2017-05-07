from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nations$', views.nations, name='nations'),
    url(r'^rankings$', views.rankings, name='rankings'),
]