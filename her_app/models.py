from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Utilisateur(models.Model):
    sexes = [('M', 'Masculin'), ('F', 'Féminin')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50, blank=False)
    prenom = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    numIdentNational = models.CharField(max_length=13, blank=False, unique=True)
    dateNaissance = models.DateField(auto_now=False, auto_now_add=False)
    sexe = models.CharField(max_length=1, choices=sexes)
    nationalite = models.CharField(max_length=50, blank=False)

    class Meta:
        abstract = True


class Medecin(Utilisateur):
    specialite = models.CharField(max_length=50, blank=False)
    ville = models.CharField(max_length=50, blank=True, null=True)
    nomHopital = models.CharField(max_length=50, blank=True, null=True)


class Patient(Utilisateur):
    situationMatris = [('M', 'Marié(e)'), ('C', 'Célibataire')]
    situationMatri = models.CharField(max_length=1, choices=situationMatris)
    profession = models.CharField(max_length=50, blank=False)


class LieuTravail(models.Model):
    ville = models.CharField(max_length=50, blank=False)
    nomHopital = models.CharField(max_length=50, blank=False)
    medecin = models.OneToOneField(Medecin, related_name='lieuTravails', on_delete=models.CASCADE, blank=True,
                                   null=True)


class DossierMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    medecin = models.ManyToManyField(Medecin, related_name='dossiers')


class Antecedant(models.Model):
    typeAntecedants = [('A', 'Allergies'), ('C', 'Chirurgicaux'), ('F', 'Familiaux')]
    typeAntecedant = models.CharField(max_length=1, choices=typeAntecedants)
    nomAntecedant = models.CharField(max_length=50, blank=False)
    remarquesAntecedant = models.CharField(max_length=500, blank=False)
    dossier = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)


#### Élements du dossier patient ####

class Consultation(models.Model):
    poids = models.IntegerField(blank=True)
    temperature = models.IntegerField(blank=True)
    motifs = models.CharField(max_length=300, blank=False)
    remarquesMedecin = models.CharField(max_length=500, blank=True)
    hypothesesC = models.CharField(max_length=500, blank=True)
    dateConsultation = models.DateField()
    finConsultation = models.BooleanField(default=False)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, default=1)
    diagnostic = models.CharField(max_length=300, blank=True)
    dossier = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)


class Traitement(models.Model):
    nomTraitement = models.CharField(max_length=50, blank=False)
    posologieTrait = models.CharField(max_length=50, blank=False)
    datePrescritpion = models.DateField()
    dureeTrait = models.CharField(max_length=50, blank=False)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='traitements')


class HypotheseDiagnostique(models.Model):
    nomMaladie = models.CharField(max_length=50, blank=False)
    Remarques = models.CharField(max_length=300, blank=True)
    Confirmation = models.BooleanField(default=False)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='hypotheses')


class ExamenParaclinique(models.Model):
    typeExamen = models.CharField(max_length=50, blank=False)
    nomExamen = models.CharField(max_length=50, blank=False)
    datePrescription = models.DateField()
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='examens')


class FichierExamen(models.Model):
    typeFichier = models.CharField(max_length=50, blank=False)
    nomFichier = models.CharField(max_length=50, blank=False)
    fichier = models.FileField(blank=True)
    examenparaclinique = models.OneToOneField(ExamenParaclinique, on_delete=models.CASCADE)


class ClassesArrythmie(models.Model):
    lettreClasse = models.CharField(max_length=1, blank=False)


class Anomalies(models.Model):
    nomAnomalie = models.CharField(max_length=100, blank=False)
    lettre = models.ManyToManyField(ClassesArrythmie)
