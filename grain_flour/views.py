from django.shortcuts import render

# Create your views here.
def grain_flour_page(request):
    return render(request, 'screens/grain_flour/grain_flour.html')

def grain_flour(request):
    return render(request,'screens/grain_flour/single_grain_flour.html')