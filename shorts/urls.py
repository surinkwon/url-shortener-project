from django.urls import path
from . import views


urlpatterns = [
    path('', views.shortening, name='random'),
    path('custom/', views.custom_shortening, name='custom'),
]
