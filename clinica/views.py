# app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm # Se creará en el paso 2

# READ: Listar todos
def paciente_list(request):
    pacientes = Paciente.objects.all().order_by('apellido')
    return render(request, 'clinica/paciente_list.html', {'pacientes': pacientes})

# CREATE / UPDATE: Crear y Editar (Usan la misma vista y formulario)
def paciente_form(request, pk=None):
    if pk: # Si hay 'pk', estamos editando
        paciente = get_object_or_404(Paciente, pk=pk)
    else: # Si no hay 'pk', estamos creando
        paciente = None

    form = PacienteForm(request.POST or None, instance=paciente)

    if form.is_valid():
        form.save()
        return redirect('paciente_list') # Redirecciona a la lista

    return render(request, 'clinica/paciente_form.html', {'form': form})

# DELETE: Eliminar
def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_list')
    # Renderiza una plantilla de confirmación de eliminación
    return render(request, 'app/paciente_confirm_delete.html', {'paciente': paciente})