from django.urls import path

from .import views

urlpatterns = [
    path('',views.tuber_page, name='tuber_page'),
    path('<int:tuber_id>', views.tuber, name='tuber'),
]