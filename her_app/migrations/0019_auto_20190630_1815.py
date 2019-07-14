# Generated by Django 2.2.2 on 2019-06-30 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0018_auto_20190624_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassesArrythmie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lettreClasse', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='fichierexamen',
            name='examenparaclinique',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='her_app.ExamenParaclinique'),
        ),
        migrations.CreateModel(
            name='Anomalies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomAnomalie', models.CharField(max_length=100)),
                ('lettre', models.ManyToManyField(to='her_app.ClassesArrythmie')),
            ],
        ),
    ]
