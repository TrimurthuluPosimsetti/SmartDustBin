from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import JsonResponse
from . import forms
# Create your views here.
def SignUpView(request):
    if request.method=='POST':
        data=forms.signupForm(request.POST)
        if data.is_valid():
            k=data.save(commit=False)
            alreadyexits=models.SignUp.objects.filter(Name=k.Name)
            if(len(alreadyexits)>=1):
                return HttpResponse("Name Already Exists Please SignIn With Another Name.....)")
            else:
                p=data.save()
                return render(request,'index.html')
        else:
            return HttpResponse('Error Something went wrong please check it once')    
    else:
        data=forms.signupForm()
        return render(request,'usersign.html',{'forms':data})    

def Login(request):
    if request.method=='POST':
        data=forms.loginForm(request.POST)
        if data.is_valid():
            k=data.save(commit=False)
            doesntexits=models.SignUp.objects.filter(Name=k.Name)
            if(len(doesntexits)==0):
                return HttpResponse("U Should Sign Up First....)")
            else:
                p=data.save()
                ord=models.previousScans.objects.filter(Name=p.Name)
                return render(request,'jay1.html',{'object':ord})
        else:
            return HttpResponse('Error')    
    else:
        data=forms.loginForm()
        return render(request,'userlogin.html',{'forms':data})


def QRscan(request):
    return JsonResponse({"QRscan":""})    

def Index(request):
    if request.method=='POST':
        data=forms.ComplaintForm(request.POST)
        if data.is_valid():
            k=data.save()
            return render(request,'index.html')
        else:
            return HttpResponse('Error') 
    else:
        data=forms.ComplaintForm()
        return  render(request,'index.html',{'forms':data})       


def Admin(request,slug):
    data = models.previousScans.objects.get(id=slug)
    return HttpResponse("Success")

def AdminView(request):
    return render(request,'JAY.HTML')  

def About(request):
    return render(request,'about.html')      


def AdminSignUpView(request):
    if request.method=='POST':
        data=forms.AdminsignupForm(request.POST)
        if data.is_valid():
            k=data.save(commit=False)
            alreadyexits=models.AdminSignUp.objects.filter(Name=k.Name)
            if(len(alreadyexits)>=1):
                return HttpResponse("Name Already Exists Please SignIn With Another Name.....)")
            else:
                p=data.save()
                return render(request,'index.html')
        else:
            return HttpResponse('Error')    
    else:
        data=forms.AdminsignupForm()
        return render(request,'adminsign.html',{'forms':data})    


def AdminLogin(request):
    if request.method=='POST':
        data=forms.AdminloginForm(request.POST)
        if data.is_valid():
            k=data.save(commit=False)
            doesntexits=models.AdminSignUp.objects.filter(Name=k.Name)
            if(len(doesntexits)==0):
                return HttpResponse("U Should Sign Up First....)")
            else:
                p=data.save()
                return render(request,'JAY.html')
        else:
            return HttpResponse('Error')    
    else:
        data=forms.AdminloginForm()
        return render(request,'adminlogin.html',{'forms':data})    
