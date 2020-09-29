from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('papers/', views.papers, name = "papers"),
    path('news/', views.news, name = "news"),
    path('news/search/', views.searchArticles, name = "searchArticles"),
    path('news/articles/<str:art>', views.article, name = "article"),
    path('contact/', views.contact, name = "contact")
]