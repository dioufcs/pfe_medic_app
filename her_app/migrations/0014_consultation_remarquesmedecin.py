# Generated by Django 2.2.2 on 2019-06-24 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0013_consultation_medecin'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='remarquesMedecin',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]