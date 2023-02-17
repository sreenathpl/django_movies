from django import forms
from .models import model_movies

class form_movies(forms.ModelForm):
    class Meta:
        model = model_movies
        fields = ['name', 'desc', 'year', 'img', 'cat', 'duration', 'director']