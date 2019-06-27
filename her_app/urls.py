# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns
#
# from . import views
#
# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'medecins', views.MedecinViewSet)
#
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]
#

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from her_app import views

router = DefaultRouter()
router.register('medecins', views.MedecinViewSet)
router.register('patients', views.PatientViewSet)
router.register('dossiers', views.DossierViewSet)
router.register('users', views.UserViewSet)
router.register('antecedants', views.AntecedantViewSet)
router.register('consultations', views.ConsultationViewSet)
router.register('examens', views.ExamenViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('medecin/<slug:foo>/', views.nom_medecin),
    path('antecedant/<int:foo>/<slug:type>/', views.antecedant_patient),
    path('consultation/<int:foo>/', views.consultation_patient),
    path('hypothese/<int:foo>/', views.hypothese_consultation),
    path('examen/<int:foo>/', views.examen_consultation),
    path('fichier/<int:foo>/', views.fichier_examen)
]
