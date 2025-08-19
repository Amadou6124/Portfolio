from django.shortcuts import render, redirect
from .models import Competences, Certificat, Projet
from .forms import ContactForm


# Create your views here.
def portfolio_onepage(request):
    competences = Competences.objects.all()
    certificats = Certificat.objects.all()
    projets = Projet.objects.all()

    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil') 
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/index.html', context={'competences': competences, 'certificats': certificats, 'projets': projets, 'form': form })