# Generated by Django 2.2.2 on 2019-06-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0014_consultation_remarquesmedecin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenparaclinique',
            name='datePrescription',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='traitement',
            name='datePrescritpion',
            field=models.DateField(),
        ),
    ]
