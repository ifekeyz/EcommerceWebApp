from django.shortcuts import render

# Create your views here.
def meat_vegetable_page(request):
    return render(request, 'screens/meat_vegetable/meat_vegetable.html')

def meat_vegetable(request):
    return render(request,'screens/meat_vegetable/single_meat_vegetable.html')