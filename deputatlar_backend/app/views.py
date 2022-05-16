import os
from .models import *
from django.conf import settings
from django.shortcuts import render
from django.views.generic import DetailView
from django.http import Http404, HttpResponse
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
        "tum": tumvash,
        "senator":senator,
        "deputat":deputat,
        "komissia":komisia,
    }
    return render(request, 'pages/xodimlar.html', context)

def tuman_xodimlar(request, pk):
    tum_dep = Deputat.objects.filter(town=pk)
    town = TownsName.objects.all()
    context = {
        "town":town,
        "tum": tumvash,
        "deputat":deputat,
        "tum_dep":tum_dep,
        "komissia":komisia,
    }
    return render(request, 'pages/tuman_deputatlari.html', context)

def admin(request):
    return render(request, 'admin_page/sidebar.html')

def doimiy_komisalar(request, pk):
    kam_azo = KomissiaAzo.objects.filter(komissia=pk)
    komisia = Komissia.objects.all()
    context = {
        "list": list,
        "tum": tumvash,
        "komissia":komisia,
        "kam_azo":kam_azo,
    }
    return render(request, 'pages/doimiy_komisia.html', context)

def all_blog(request):
    context = {
        'list':list,
        "tum": tumvash,
        "komissia":komisia,
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

def download_files(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as ft:
            response = HttpResponse(ft.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline,filename='+os.path.basename(file_path)
            return response
        raise Http404
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
