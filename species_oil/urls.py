from django.urls import path

from .import views

urlpatterns = [
    path('',views.species_oil_page, name='species_oil_page'),
    path('<int:species_oil_id>', views.species_oil, name='species_oil'),
]