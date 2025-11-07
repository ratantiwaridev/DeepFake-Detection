from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('upload-image/', views.upload_image_ajax, name='upload_image_ajax'),
]