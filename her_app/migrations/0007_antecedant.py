# Generated by Django 2.2.2 on 2019-06-22 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('her_app', '0006_delete_antecedant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeAntecedant', models.CharField(choices=[('A', 'Allergies'), ('C', 'Chirurgicaux'), ('F', 'Familiaux')], max_length=1)),
                ('nomAntecedant', models.CharField(max_length=50)),
                ('remarquesAntecedant', models.CharField(max_length=50)),
                ('dossier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='her_app.DossierMedical')),
            ],
        ),
    ]