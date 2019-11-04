from django.shortcuts import render, get_object_or_404
from .models import Notificacion, Medicina
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import auth


def lista(request):
    notificaciones = Notificacion.objects.filter(fecha_compra__isnull=True, paciente = auth.get_user(request).id).order_by('fecha_creacion')
    return render(request, 'proyecto/listar_not.html', {'notificaciones': notificaciones})

def lista_comprado(request):
    notificaciones = Notificacion.objects.filter(fecha_compra__lte=timezone.now()).order_by('fecha_compra')
    return render(request, 'proyecto/listar_not.html', {'notificaciones': notificaciones})

def detalle(request, pk):
    p = get_object_or_404(Notificacion, pk=pk, id=pk)
    q = Notificacion.medicinas.through.objects.filter(notificacion_id = pk)
    medicinafin = []

    for value in q:
        dato = value.medicina_id
        medi = get_object_or_404(Medicina, pk=dato)
        medicinafin.append(medi)
        pass
    return render(request, 'proyecto/detalle_not.html', {'notificacion':p, 'medicinas':medicinafin})

def comprar(request, pk):
    noti = get_object_or_404(Notificacion, pk=pk)
    noti.confirmado()
    return redirect('detalle', pk=pk)

def validarusuario(request):
    if request.user.is_authenticated:
      if request.user.groups.name  == "Pacientes":
        return redirect('/lista/')
      elif request.user.is_admin:
        return redirect('/admin/')
    return redirect('login')
