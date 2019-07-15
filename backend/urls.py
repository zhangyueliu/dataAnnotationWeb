from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r'^get_article_specific/$', views.getArticleSpecific, name='get_article_specific'),
]