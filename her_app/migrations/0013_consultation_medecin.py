# Generated by Django 2.2.2 on 2019-06-24 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0012_consultation_hypothesesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='medecin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='her_app.Medecin'),
        ),
    ]
