from django.conf.urls import url
from retrieve import views

urlpatterns = [
    url(r'^search-desc/', views.search_by_desc, name='search_desc'),
    url(r'^search/', views.search_by_title, name='index'),
    url(r'^results/', views.results, name='results'),
    url(r'^$', views.index, name='index'),
]