from django import forms

from .models import Link

class LinkForm(forms.ModelForm): # using forms.ModelForm instead of forms.Model lets you save data to your model from form directly using django's built-in functionality
    class Meta:
        model = Link # specify what model you want
        fields = ['name', 'url', 'slug'] # specify what fields you want in the form