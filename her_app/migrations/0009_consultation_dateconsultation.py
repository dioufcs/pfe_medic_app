# Generated by Django 2.2.2 on 2019-06-23 21:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0008_auto_20190622_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='dateConsultation',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
