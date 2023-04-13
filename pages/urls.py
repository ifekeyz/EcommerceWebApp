from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('register_login/', views.register_login, name='register_login'),
    path('cart/', views.cart, name='cart'),
]
