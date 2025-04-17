from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    LoginView,
    PatientViewSet,
    DoctorViewSet,
    PatientDoctorMappingViewSet,
    PatientDoctorsView,
    DoctorPatientsView,
)

router = DefaultRouter()
router.register(r"patients", PatientViewSet, basename="patient")
router.register(r"doctors", DoctorViewSet, basename="doctor")
router.register(r"mappings", PatientDoctorMappingViewSet, basename="mapping")

urlpatterns = [
    # Auth endpoints
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    # ViewSet endpoints
    path("", include(router.urls)),
    # Custom endpoints
    path(
        "mappings/patient/<int:patient_id>/",
        PatientDoctorsView.as_view(),
        name="patient-doctors",
    ),
    path(
        "mappings/doctor/<int:doctor_id>/",
        DoctorPatientsView.as_view(),
        name="doctor-patients",
    ),
]
