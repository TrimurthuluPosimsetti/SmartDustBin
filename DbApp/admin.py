from django.contrib import admin
from . import models

# Register your models here.
class SignUp(admin.ModelAdmin):
    list_display=['Name','NickName','Email','Password']
admin.site.register(models.SignUp,SignUp)

class PreviousScans(admin.ModelAdmin):
    list_display=['dbid','dbweight','lastUsage']
admin.site.register(models.previousScans,PreviousScans)


class Login(admin.ModelAdmin):
    list_display=['Name','Password']
admin.site.register(models.Login,Login)


class AdminLogin(admin.ModelAdmin):
    list_display=['Name','Password']
admin.site.register(models.AdminLogin,AdminLogin)

class AdminSignUp(admin.ModelAdmin):
    list_display=['Name','NickName','Email','Password','Profession']
admin.site.register(models.AdminSignUp,AdminSignUp)

class Complaint(admin.ModelAdmin):
    list_display=['Name','Email','Message']
admin.site.register(models.Complaint,Complaint)


