# Generated by Django 4.2 on 2024-08-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0009_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('T', 'Tierra'), ('E', 'Eléctrico'), ('F', 'Fuego'), ('A', 'Agua'), ('L', 'Lagartija')], max_length=30),
        ),
    ]
