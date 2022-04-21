from django import forms
class registers(forms.Form):
    name = forms.CharField()
    email=forms.EmailField()
    password=forms.PasswordInput()

