from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class profilForm(forms.form):
"""
class ConnexionForm(forms.Form):
	username = forms.CharField(label = "Nom d'utilisateur", max_length = 30)
	password = forms.CharField(label = "Mot de passe", widget = forms.PasswordInput)
"""

class ConnexionForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    location = forms.CharField() 

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )