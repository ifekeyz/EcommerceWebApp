from django.shortcuts import render

# Create your views here.
def species_oil_page(request):
    return render(request, 'screens/species_oil/species_oil.html')

def species_oil(request):
    return render(request,'screens/species_oil/single_species_oil.html')