from django.conf.urls import url
from retrieve import views

urlpatterns = [
    url(r'^search/', views.search_books, name='index'),
    url(r'^results/', views.results, name='results'),
    url(r'^$', views.search_books, name='index'),
]