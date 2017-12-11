from django.conf.urls import url
from retrieve import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]