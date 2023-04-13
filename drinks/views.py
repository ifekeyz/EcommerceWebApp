from django.shortcuts import render

# Create your views here.
def drinks_page(request):
    return render(request, 'screens/drinks/drinks.html')

def drinks(request):
    return render(request,'screens/drinks/single_drinks.html')