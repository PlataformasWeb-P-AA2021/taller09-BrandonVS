# Generated by Django 3.2.4 on 2021-06-12 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0007_estudiante_modulos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={'ordering': ['tipo_estudiante'], 'verbose_name_plural': 'Los Estudiantes'},
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='modulos',
        ),
        migrations.RemoveField(
            model_name='modulo',
            name='estudiantes',
        ),
    ]
