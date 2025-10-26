# app/forms.py

from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono']
        # Añade aquí personalizaciones de widgets o validaciones específicas
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre...'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido...'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: +569...'}),
        }