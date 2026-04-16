from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Asistencia
from .forms import AsistenciaForm

def formulario_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save()
            return redirect('confirmacion_asistencia', id=asistencia.id)
    else:
        form = AsistenciaForm()
    
    return render(request, 'asistencia/formulario_asistencia.html', {'form': form})

def confirmacion_asistencia(request, id):
    try:
        asistencia = Asistencia.objects.get(id=id)
        return render(request, 'asistencia/confirmacion_asistencia.html', {'asistencia': asistencia})
    except Asistencia.DoesNotExist:
        messages.error(request, 'El registro de asistencia no fue encontrado.')
        return redirect('formulario_asistencia')
