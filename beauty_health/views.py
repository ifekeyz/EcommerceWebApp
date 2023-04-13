from django.shortcuts import render
from .models import Beauty_Health

# Create your views here.
def beauty_health_page(request):
    beauty_healths = Beauty_Health.objects.order_by('-postingDate')


    context={
        'beauty_healths':beauty_healths
    }
    return render(request, 'screens/beauty_health/beauty_health.html', context)

def beauty_health(request):
    return render(request,'screens/beauty_health/single_beauty_health.html')