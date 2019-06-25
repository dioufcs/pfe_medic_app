from rest_framework import serializers
from .models import *

from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierMedical
        fields = '__all__'


class AntecedantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antecedant
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'


class HypotheseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HypotheseDiagnostique
        fields = '__all__'


class ExamensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenParaclinique
        fields = '__all__'


class FichiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichierExamen
        fields = '__all__'


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')
