from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='map-home'),
    path('results/', views.results, name='map-results'),
]
