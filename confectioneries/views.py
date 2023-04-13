from django.shortcuts import render,get_object_or_404
from .models import Confectioneries
# Create your views here.
def confectioneries_page(request):
    confectioneries = Confectioneries.objects.order_by('-postingDate')


    context={
        'confectioneries':confectioneries
    }
    return render(request, 'screens/confentioneries/confentioneries.html',context)


def confectioneries(request, confectioneries_id):
    confectionerie = get_object_or_404(Confectioneries, pk=confectioneries_id)

    context={
        'confectionerie':confectionerie
    }
    return render(request,'screens/confentioneries/single_confentioneries.html',context)