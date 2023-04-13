from django.urls import path

from .import views

urlpatterns = [
    path('',views.drinks_page, name='drinks_page'),
    path('<int:drinks_id>', views.drinks, name='drinks'),
]