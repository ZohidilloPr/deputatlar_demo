from msilib.schema import File
from pyexpat import model
from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
# Create your views here


list = [1, 2, 3, 4, 5]
file = Files.objects.all()
blogs = Blogs.objects.all()
partia = Partia.objects.all()
senator = Senator.objects.all()
deputat = Deputat.objects.all()
komisia = Komissia.objects.all()
tumvash = TownsName.objects.all()
komisiaAzo = KomissiaAzo.objects.all()

def Home(request):
    last_blog = blogs.order_by("-add_date")
    five_blogs = blogs.order_by("-id")[::-5]
    context = {
        "list":list,
        "tum": tumvash,
        "five":five_blogs,
        "senator":senator,
        "komissia":komisia,
        "last_blog":last_blog,
    }
    return render(request, 'pages/home.html', context)
def Xodimlar(request):
    context = {
        "senator":senator,
        "deputat":deputat,
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/xodimlar.html', context)

def tuman_xodimlar(request):
    context = {
        "deputat":deputat,
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
        "list": list,
    }
    return render(request, 'pages/doimiy_komisia.html', context)

def all_blog(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
        'list':list,
    }
    return render(request, 'pages/all_blogs.html', context)

class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'pages/blog.html'

def Work_plan(request):
    context = {
        "files": file,
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

def Empty(request):
    context = {
        "tum": tumvash,
        "komissia":komisia,
    }
    return render(request, 'pages/none.html', context)
