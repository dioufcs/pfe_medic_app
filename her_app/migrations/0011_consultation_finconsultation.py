# Generated by Django 2.2.2 on 2019-06-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0010_auto_20190623_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='finConsultation',
            field=models.BooleanField(default=False),
        ),
    ]