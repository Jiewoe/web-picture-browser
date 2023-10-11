from django.urls import path
from picture_app import views

urlpatterns = [
    path('', views.page, name='page'),
    path('test/', views.test, name='test'),
    path('upload/', views.upload, name='upload'),
    path('time_sort/', views.time_sort, name='time_sort'),
    path('city_sort', views.city_sort, name='city_sort'),
]