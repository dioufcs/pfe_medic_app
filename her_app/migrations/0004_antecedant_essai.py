# Generated by Django 2.2.2 on 2019-06-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0003_auto_20190612_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='antecedant',
            name='essai',
            field=models.CharField(default='csd', max_length=3),
            preserve_default=False,
        ),
    ]
