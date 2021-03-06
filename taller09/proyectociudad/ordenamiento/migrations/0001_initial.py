# Generated by Django 3.2.4 on 2021-06-12 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo_parroquia', models.CharField(choices=[('urbana', 'Parroquia Urbana'), ('rural', 'Parroquia Rural')], max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Las parroquias',
                'ordering': ['tipo_parroquia'],
            },
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('numero_viviendas', models.IntegerField()),
                ('numero_parques', models.IntegerField(choices=[('1', 'Un parque'), ('2', 'Dos parques'), ('3', 'Tres parques'), ('4', 'Cuatro parques'), ('5', 'Cinco parques'), ('6', 'Seis parques')])),
                ('numero_edificios', models.IntegerField()),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losbarrios', to='ordenamiento.parroquia')),
            ],
            options={
                'verbose_name_plural': 'Los parques',
                'ordering': ['numero_parques'],
            },
        ),
    ]
