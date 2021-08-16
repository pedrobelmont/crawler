from django.shortcuts import render
from .models import Galeria
from django.utils import timezone

def galeria(request):
    now = timezone.now()
    context = {
        'fotos': Galeria.objects.filter(publicate_on__lte=now)
    }
    return render(request, 'galeria/vitrine.html', context)