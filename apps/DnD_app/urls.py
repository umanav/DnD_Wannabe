from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^new_Game$', views.new_Game),
    url(r'^restart$', views.restart),
    url(r'^continue$', views.keep_playing),
    url(r'^game$', views.game),
]
