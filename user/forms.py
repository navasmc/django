from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User as Userobj

class LoginForm(forms.Form):
    username = forms.CharField( 
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class Contactform(forms.Form):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )
    email = forms.EmailField(  
        max_length=254,
        widget=forms.EmailInput(attrs={'class': "form-control"}),
    )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))

    def clean(self):
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def register(self, request):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        user = Userobj.objects.create_user(name, email, password)
        user.save()
        return user