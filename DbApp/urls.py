from django.urls import include, path
from DbApp import views

urlpatterns=[
path('s/',views.SignUpView),
path('l/',views.Login),
path('as/',views.AdminSignUpView),
path('al/',views.AdminLogin),
path('q/',views.QRscan),
path('',views.Index),
path('about/',views.About),
path('a/<slug:slug>/',views.Admin),
path('a/',views.AdminView),
]