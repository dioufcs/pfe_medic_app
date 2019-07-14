from django.contrib import admin
from .models import *

models = [Medecin,
          Patient,
          LieuTravail,
          DossierMedical,
          Antecedant,
          Consultation,
          Traitement,
          HypotheseDiagnostique,
          ExamenParaclinique,
          FichierExamen,
          ClassesArrythmie,
          Anomalies]

admin.site.register(models)
