# Generated by Django 2.2.2 on 2019-06-24 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0015_auto_20190624_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichierexamen',
            name='examenparaclinique',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='her_app.ExamenParaclinique'),
        ),
    ]
