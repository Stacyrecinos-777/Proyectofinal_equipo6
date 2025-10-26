# app/models.py (Ejemplo para Paciente)

from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Recuerda crear modelos similares para Medico y Cita