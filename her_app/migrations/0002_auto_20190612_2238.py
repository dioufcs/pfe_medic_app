# Generated by Django 2.2.2 on 2019-06-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='numIdentNational',
            field=models.CharField(max_length=17, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='numIdentNational',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]