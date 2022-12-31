from django import forms



class PacienteAnimal(forms.Form):
    TIPO_ANIMAL_CHOICES = (
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Pajaro', 'Pájaro'),
        ('Pez', 'Pez'),
        ('Vaca', 'Vaca'),
        ('Caballo', 'Caballo'),
        ('Oveja', 'Oveja'),
        ('Cabra', 'Cabra'),
        ('Cerdo', 'Cerdo')
    )
    nombre_animal = forms.CharField(label='Nombre', max_length=100)
    tipo_animal = forms.ChoiceField(label='Tipo de animal', choices=TIPO_ANIMAL_CHOICES)
    raza = forms.CharField(label='Raza', max_length=150)
    edad = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))
    color = forms.CharField(label='Color de tu mascota', max_length=100)


# class RegistroForm(forms.Form):
#     email = forms.EmailField(label='Email', max_length=50)
#     password = forms.PasswordInput(label='Contraseña')



class Dueno_Paciente(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=150)
    apellido = forms.CharField(label='Apellido', max_length=150)
    telefono = forms.IntegerField(label='Teléfono')
    direccion = forms.CharField(label='Dirección', max_length=150)
    dni = forms.CharField(label='DNI')

