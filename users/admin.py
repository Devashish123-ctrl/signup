# admin.py

from django.contrib import admin
from .models import PatientProfile, DoctorProfile ,User # Import your models here

admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(User)
