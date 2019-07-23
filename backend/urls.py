from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r'^get_data/$', views.get_all_data, name='get_article_specific'),
    url(r'^add_data/$', views.add_data, name='add_data')
]