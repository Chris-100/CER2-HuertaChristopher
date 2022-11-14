from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):
    busqueda = request.POST.get("buscar")
    casas = correspondencia.objects.all()

    if busqueda:
        casas=correspondencia.objects.filter(
            Q(residencia__residencia__icontains = busqueda)
        ).distinct()
    return render(request, 'home.html', {
        'casas': casas
    })

def detalles(request):
    busqueda = request.POST.get("buscar")
    detalle = correspondencia.objects.all()

    if busqueda:
        detalle=correspondencia.objects.filter(
            Q(residencia__residencia__icontains = busqueda)
        ).distinct()
    return render(request, 'detalles.html',{
        'detalle': detalle
    })