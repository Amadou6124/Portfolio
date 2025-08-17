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