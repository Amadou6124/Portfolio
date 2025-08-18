from django.db import models

# Create your models here.
class Competences(models.Model):
    nom = models.CharField(max_length=80)
    icone = models.URLField(max_length=255, help_text="Liens vers icone de la compétence")

    class Meta:
        verbose_name = 'Compétence'

    
    def __str__(self):
        return self.nom
    

class Certificat(models.Model):
    titre = models.CharField(max_length=100)
    organisme = models.CharField(max_length=100, help_text="Nom de l'organisme")
    image = models.ImageField(upload_to='certicicats/images/')
    fichier_pdf = models.FileField(upload_to='certificats/pdf')

    def __str__(self):
        return self.titre 
    

class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image_carousel = models.ImageField(upload_to='projets/carousels/')
    lien_github = models.URLField()
    est_principal = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Projet"
    
    def __str__(self):
        return self.titre
    
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.nom} - {self.sujet}"