# Generated by Django 4.2 on 2024-08-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0008_alter_pokemon_type_alter_trainer_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('L', 'Lagartija'), ('F', 'Fuego'), ('E', 'Eléctrico'), ('A', 'Agua'), ('T', 'Tierra')], max_length=30),
        ),
    ]
