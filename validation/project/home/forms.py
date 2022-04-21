from django import forms
class register(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='password Again', widget=forms.PasswordInput)

    def clean(self):
       cleaned_data = super().clean()
       valpas=self.cleaned_data['password']
       valrpas=self.cleaned_data['rpassword']
       if valrpas != valpas:
           raise forms.ValidationError("Wrong password")
