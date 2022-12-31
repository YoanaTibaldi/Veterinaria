from django.shortcuts import render
from django.http import HttpResponse
from .forms import PacienteAnimal, Dueno_Paciente
from . import models
from .models import Persona, Dueno


# import sqlite3


# Create your views here.


def index(request, template_name='entidad/index.html'):
    return render(request, template_name)


# def user_register(request, template_name='entidad/register.html'):
#     if request.method == 'POST':
#         form = RegistroForm()


def paciente_form(request, template_name='entidad/f_paciente.html'):
    if request.method == 'POST':
        form = models.Paciente()
        form.tipo_animal = request.POST.get('tipo_animal')
        form.raza = request.POST.get('raza')
        form.color = request.POST.get('color')
        form.edad = request.POST.get('edad')
        form.nombre_animal = request.POST.get('nombre_animal')
        form.save()

        f_dueno = Persona()
        f_dueno.nombre = request.POST.get('nombre')
        f_dueno.apellido = request.POST.get('apellido')
        f_dueno.telefono = request.POST.get('telefono')
        f_dueno.direccion = request.POST.get('direccion')
        # dni = request.POST.get('num_ident')
        # dueno = Dueno.objects.filter(num_ident=dni)
        # f_dueno = dueno

        f_dueno.num_dni = request.POST.get('num_dni')

        # f_dueno.num_dni = request.POST.get(field=f_dueno.num_dni['dni'])

        f_dueno.save()

        return HttpResponse('Exito!')
    else:
        # return HttpResponse('Exito!')
        form = PacienteAnimal()
        f_dueno = Dueno_Paciente()

    # este dato que contiene form es el form que se muestra en el html
    dato = {
        'form': form,
        'f_dueno': f_dueno
    }
    return render(request, template_name, dato)
