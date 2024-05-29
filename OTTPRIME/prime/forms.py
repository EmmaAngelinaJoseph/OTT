from django import forms
from .models import User, movies


class MyLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="password",widget=forms.PasswordInput)
    password2= forms.CharField(label=" Confirm password", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','first_name','email','password')
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('password does not match')
        return cd['password2']

class MovieForm(forms.ModelForm):
    class Meta:
        model = movies
        fields = ['title', 'description', 'genres', 'director', 'main_actor', 'duration', 'image', 'video']
