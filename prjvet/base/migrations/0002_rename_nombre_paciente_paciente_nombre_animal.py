# Generated by Django 4.1.4 on 2022-12-22 13:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='nombre_paciente',
            new_name='nombre_animal',
        ),
    ]
