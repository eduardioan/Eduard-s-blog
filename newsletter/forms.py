from django import forms
from django.shortcuts import render

from .models import NewsUsers
class NewsUserForm(forms.ModelForm):
    class Meta:
        model = NewsUsers
        fields = ['name', 'email']

