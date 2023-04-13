from django.urls import path

from .import views

urlpatterns = [
    path('',views.beauty_health_page, name='beauty_health_page'),
    path('<int:beauty_health_id>', views.beauty_health, name='beauty_health'),
]