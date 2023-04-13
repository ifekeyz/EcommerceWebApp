from django.urls import path

from .import views

urlpatterns = [
    path('',views.untensils_page, name='untensils_page'),
    path('<int:untensils_id>', views.untensils, name='untensils'),
]