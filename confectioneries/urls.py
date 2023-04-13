from django.urls import path

from .import views

urlpatterns = [
    path('',views.confectioneries_page, name='confectioneries_page'),
    path('<int:confectioneries_id>', views.confectioneries, name='confectioneries'),
]