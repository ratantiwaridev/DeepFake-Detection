from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('upload/', views.upload_image, name='upload_image'),
]