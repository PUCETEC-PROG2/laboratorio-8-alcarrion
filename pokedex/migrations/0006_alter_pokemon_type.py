# Generated by Django 4.2 on 2024-08-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0005_trainer_picture_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('E', 'Eléctrico'), ('P', 'Planta'), ('T', 'Tierra'), ('L', 'Lagartija'), ('A', 'Agua'), ('F', 'Fuego')], max_length=30),
        ),
    ]
