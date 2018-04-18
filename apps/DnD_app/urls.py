from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^profile$', views.profile),
    url(r'^game$', views.game),
    url(r'^save/(?P<id>\d+)$', views.save),
    url(r'^new_game/(?P<id>\d+)$', views.new_game),
    url(r'^restart$', views.restart),
    url(r'^continue$', views.keep_playing),
    url(r'^character$', views.character),
<<<<<<< HEAD
    url(r'^end$', views.end),
    url(r'^game_over$', views.game_over),
=======
    url(r'^first$', views.first),
    url(r'^second$', views.second),
    url(r'^third$', views.third),
>>>>>>> 628efc5d6d9776b7bae5089731ae536492752406
]
