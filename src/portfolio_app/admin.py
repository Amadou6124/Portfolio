from django.contrib import admin
from .models import Certificat, Competences, Projet

# Register your models here.

@admin.register(Competences)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['nom']


@admin.register(Certificat)
class CertificatAdmin(admin.ModelAdmin):
    list_display = ['titre']

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ['titre']