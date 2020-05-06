from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='map-home'),
    path('deliverables/', views.about, name='map-deliverables'),
    path('results/', views.results, name='map-results'),
]
