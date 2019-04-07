from django import forms
from . import models

class signupForm(forms.ModelForm):
    class Meta:
        model = models.SignUp
        fields = ['Name','NickName','Email','Password']


class loginForm(forms.ModelForm):
    class Meta:
        model=models.Login
        fields=['Name','Password']



class AdminsignupForm(forms.ModelForm):
    class Meta:
        model = models.AdminSignUp
        fields = ['Name','NickName','Email','Password','Profession']


class AdminloginForm(forms.ModelForm):
    class Meta:
        model=models.AdminLogin
        fields=['Name','Password']        

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=models.Complaint
        fields=['Name','Email','Message']        