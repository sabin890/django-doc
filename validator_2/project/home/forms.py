from django.core import validators
from django import forms
from .models import User


class Reg(forms.ModelForm):
    # password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'Enter name','password':'Enter password','email':'Enter email'}
        error_messages={
            'name':{'required':'Nam Lekh mujhi!!!!'},
            'password':{'required':'password Lekh mujhi!!!!'},
            }
        widgets={
            'password':forms.PasswordInput
        }
