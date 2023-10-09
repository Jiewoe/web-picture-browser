from django.urls import path
from picture_app import views

urlpatterns = [
    path('', views.page, name='page'),
    path('test/', views.test, name='test'),
    path('upload/', views.upload, name='upload'),
]