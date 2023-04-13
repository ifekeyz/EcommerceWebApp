from django.shortcuts import render

# Create your views here.
def tuber_page(request):
    return render(request, 'screens/tuber/tuber.html')

def tuber(request):
    return render(request,'screens/tuber/single_tuber.html')