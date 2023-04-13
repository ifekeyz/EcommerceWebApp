from django.urls import path

from .import views

urlpatterns = [
    path('',views.grain_flour_page, name='grain_flour_page'),
    path('<int:grain_flour_id>', views.grain_flour, name='grain_flour'),
]