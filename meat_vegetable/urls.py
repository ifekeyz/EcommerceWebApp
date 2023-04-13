from django.urls import path

from .import views

urlpatterns = [
    path('',views.meat_vegetable_page, name='meat_vegetable_page'),
    path('<int:meat_vegetable_id>', views.meat_vegetable, name='meat_vegetable'),
]