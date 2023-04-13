from django.shortcuts import render
from .models import Untensiles
# Create your views here.
def untensils_page(request):
    untensiles = Untensiles.objects.order_by('-postingDate')


    context={
        'untensiles':untensiles
    }
    return render(request, 'screens/utensiles/utensiles.html',context)

def untensils(request):
    return render(request,'screens/utensiles/single_utensiles.html')