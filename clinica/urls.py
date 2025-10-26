# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # READ
    path('pacientes/', views.paciente_list, name='paciente_list'),
    
    # CREATE
    path('pacientes/nuevo/', views.paciente_form, name='paciente_create'),
    
    # UPDATE
    path('pacientes/editar/<int:pk>/', views.paciente_form, name='paciente_update'),
    
    # DELETE
    path('pacientes/eliminar/<int:pk>/', views.paciente_delete, name='paciente_delete'),
]