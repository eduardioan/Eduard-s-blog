from django import forms
from django.forms import TextInput, EmailInput
from django.shortcuts import render

from .models import NewsUsers
class NewsUserForm(forms.ModelForm):
    class Meta:
        model = NewsUsers
        fields = ['name', 'email']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        users = NewsUsers.objects.all()
        for user in users:
            if cleaned_data.get('email') == NewsUsers.email:
                msg = ' adresa de email exista deja'
                self._errors['email'] = self.error_class([msg])

        return cleaned_data
