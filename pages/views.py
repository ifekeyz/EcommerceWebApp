from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'screens/index.html')


def checkout(request):
    return render(request, 'screens/checkout.html')


def register_login(request):
    return render(request, 'screens/register_login.html')


def cart(request):
    return render(request, 'screens/cart.html')