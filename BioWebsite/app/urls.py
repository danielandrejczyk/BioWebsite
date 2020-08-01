from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doc/', views.article_view, name='article_view'),
]
