from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    # Ajoute les classes CSS aux widgets
    nom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    sujet = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Contact
        fields = ['nom', 'email', 'sujet', 'message']

