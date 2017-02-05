from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.entries, name='entries'),
    url(r'^$', views.profiles, name='profiles')
]
