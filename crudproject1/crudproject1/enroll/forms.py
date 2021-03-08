from django import forms
from .models import User
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name' , 'email' , 'roll_no']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control'}),
        }