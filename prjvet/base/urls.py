from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paciente_form', views.paciente_form, name='paciente_form')

]

