from django.db import models
# from django import models

# Create your models here.
TIPO_ANIMAL_CHOICE = (
    (1, 'Perro'),
    (2, 'Gato'),
    (3, 'Pájaro'),
    (4, 'Pez'),
    (5, 'Vaca'),
    (6, 'Caballo'),
    (7, 'Oveja'),
    (8, 'Cabra'),
    (9, 'Cerdo')
)


class Diagnosticos(models.Model):
    tipo_diagnostico = models.CharField('Tipo de diagnóstico', max_length=150)
    tratamientos = models.CharField('Tratamientos', max_length=150)


class Vacunas(models.Model):
    cant_vacunas = models.CharField('Vacunas aplicadas', max_length=150)
    prox_vacunas = models.CharField('Proximas vacunas a aplicar', max_length=150)


class Dueno(models.Model):
    localidad = models.CharField('Localidad', max_length=150, null=True)
    # num_ident = models.BigIntegerField('Documento', null=True)


class Empleado(models.Model):
    matricula = models.CharField('Matrícula', max_length=8)


class Persona(models.Model):

    nombre = models.CharField('Nombre/s', max_length=150)
    apellido = models.CharField('Apellido/s', max_length=150)
    direccion = models.CharField('Dirección', max_length=150)
    telefono = models.IntegerField('Teléfono')
    num_matricula = models.ForeignKey(Empleado, on_delete=models.PROTECT, null=True)
    num_dni = models.ForeignKey(Dueno, on_delete=models.PROTECT, null=True)


class Paciente(models.Model):
    tipo_animal = models.CharField('Tipo de animal', choices=TIPO_ANIMAL_CHOICE, default='Perro', max_length=10)
    raza = models.CharField('Raza', max_length=150)
    nombre_animal = models.CharField('Nombre', max_length=150, null=True)
    edad = models.DateField('Fecha de nacimiento', null='True', blank=True)
    color = models.CharField('Color de tu mascota', max_length=100, blank=True)

    class Meta:
        ordering = ['tipo_animal']


class Registro(models.Model):
    email = models.EmailField('Email')
    pass_word = models.CharField('Contraseña', max_length=20)
