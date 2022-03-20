from django import forms
from .models import Occupants, Businesses, Posts

class OccupantsForm(forms.ModelForm):
    class Meta:
        model = Occupants
        exclude = ['user']

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user', 'neighbourhood']
