# Generated by Django 2.2.2 on 2019-06-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0007_antecedant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedant',
            name='remarquesAntecedant',
            field=models.CharField(max_length=500),
        ),
    ]
