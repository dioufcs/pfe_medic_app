# Generated by Django 2.2.2 on 2019-07-06 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0020_consultation_diagnostic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lieutravail',
            name='medecin',
        ),
        migrations.AddField(
            model_name='lieutravail',
            name='medecin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lieuTravails', to='her_app.Medecin'),
        ),
    ]
