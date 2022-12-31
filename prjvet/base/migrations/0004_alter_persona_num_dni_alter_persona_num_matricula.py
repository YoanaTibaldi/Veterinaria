# Generated by Django 4.1.4 on 2022-12-29 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_dueno_dni_dueno_localidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='num_dni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='base.dueno'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='num_matricula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='base.empleado'),
        ),
    ]
