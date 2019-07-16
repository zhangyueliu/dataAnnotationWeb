from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r'^get_data/$', views.getAllData, name='get_article_specific'),
]