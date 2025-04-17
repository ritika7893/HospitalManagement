from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Patient(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patients"
    )
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)  # Made nullable
    gender = models.CharField(max_length=10, default="Not Specified")  # Default added
    contact_number = models.CharField(max_length=15, blank=True, default="")  # Default
    address = models.TextField(blank=True, default="")  # Default
    medical_history = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.IntegerField(default=0)  # Default added
    qualification = models.CharField(max_length=100, default="MBBS")  # Default added
    contact_number = models.CharField(max_length=15, default="0000000000")  # Default
    email = models.EmailField(default="doctor@example.com")  # Default added
    available_days = models.CharField(max_length=100, default="Monday-Friday")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="doctor_mappings"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="patient_mappings"
    )
    assigned_date = models.DateField(auto_now_add=True)
    reason = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("patient", "doctor")

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
