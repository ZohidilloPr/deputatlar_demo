from django.shortcuts import render
from .models import *
# Create your views here.

tumvash = TownsName.objects.all()
komisia = Komissia.objects.all()
def Home(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/home.html', context)
def Xodimlar(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/xodimlar.html', context)

def tuman_xodimlar(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/tuman_deputatlari.html', context)

def admin(request):
    return render(request, 'admin_page/sidebar.html')

def doimiy_komisalar(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/doimiy_komisia.html', context)

def all_blog(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/all_blogs.html', context)

def Work_plan(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/ish_reja.html', context)

def cv(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/full_cv.html', context)









