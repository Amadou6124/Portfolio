from django.shortcuts import render
from .models import Competences, Certificat, Projet

# Create your views here.
def portfolio_onepage(request):
    competences = Competences.objects.all()
    certificats = Certificat.objects.all()
    projets = Projet.objects.all()
    return render(request, 'portfolio_app/index.html', context={'competences': competences, 'certificats': certificats, 'projets': projets })