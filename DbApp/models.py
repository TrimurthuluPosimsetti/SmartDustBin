from django.db import models
from django import forms
# Create your models here.
class SignUp(models.Model):
    Name=models.CharField(max_length=200)
    NickName=models.TextField()
    Email=models.EmailField(max_length=70)
    Password=models.CharField(max_length=5)

class Login(models.Model):
    Name=models.CharField(max_length=200)
    Password=models.CharField(max_length=5)

class previousScans(models.Model):
    Name=models.CharField(max_length=30,default='x')
    dbid=models.CharField(max_length=100)
    dbweight=models.IntegerField()
    lastUsage=models.DateTimeField()

class AdminSignUp(models.Model):   
    Name=models.CharField(max_length=200)
    NickName=models.TextField()
    Email=models.EmailField(max_length=70)
    Password=models.CharField(max_length=5) 
    Profession=models.CharField(max_length=5)


class AdminLogin(models.Model):
    Name=models.CharField(max_length=200)
    Password=models.CharField(max_length=5)

class Complaint(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=70)
    Message=models.CharField(max_length=250)    


