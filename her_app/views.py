from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.compat import get_username_field

from .serializers import *

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

    @action(methods=['get'], detail=True)
    def dossiers(self, request, pk=None):
        medecin = Medecin.objects.get(pk=pk)
        print(medecin.nom, medecin.prenom)
        dossiers = DossierSerializer(medecin.dossiers.all(), many=True)
        print(dossiers.data)
        return Response(dossiers.data)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DossierViewSet(viewsets.ModelViewSet):
    queryset = DossierMedical.objects.all()
    serializer_class = DossierSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AntecedantViewSet(viewsets.ModelViewSet):
    queryset = Antecedant.objects.all()
    serializer_class = AntecedantSerializer


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = ExamenParaclinique.objects.all()
    serializer_class = ExamensSerializer


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
def nom_medecin(request, foo):
    medecin = Medecin.objects.get(user__username=foo)
    return Response({"nom": medecin.nom + " " + medecin.prenom, "specialite": medecin.specialite})


@api_view(['GET'])
def antecedant_patient(request, foo, type):
    antecedants = Antecedant.objects.filter(dossier_id=foo, typeAntecedant=type)
    serializer = AntecedantSerializer(antecedants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def consultation_patient(request, foo):
    consultations = Consultation.objects.filter(dossier_id=foo).order_by('-dateConsultation')
    serializer = ConsultationSerializer(consultations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def hypothese_consultation(request, foo):
    hypotheses = HypotheseDiagnostique.objects.filter(consultation_id=foo)
    serializer = HypotheseSerializer(hypotheses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def examen_consultation(request, foo):
    examens = ExamenParaclinique.objects.filter(consultation_id=foo)
    serializer = ExamensSerializer(examens, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fichier_examen(request, foo):
    fichier = FichierExamen.objects.get(examenparaclinique_id=foo)
    serializer = FichiersSerializer(fichier)
    return Response(serializer.data)

@api_view(['GET'])
def fichier_examen(request, foo):
    fichier = FichierExamen.objects.get(examenparaclinique_id=foo)
    serializer = FichiersSerializer(fichier)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
