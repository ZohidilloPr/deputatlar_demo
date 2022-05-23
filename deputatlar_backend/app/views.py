import os
import random
from .models import *
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import Http404, HttpResponse
from .forms import AddTaklifForm
# Create your views here


list = [1, 2, 3, 4, 5]
file = Files.objects.all()
blogs = Blogs.objects.all()
partia = Partia.objects.all()
senator = Senator.objects.all()
deputat = Deputat.objects.all()
komisia = Komissia.objects.all()
tumvash = TownsName.objects.all()
ran_ch = random.sample(set(blogs), 3)
komisiaAzo = KomissiaAzo.objects.all()
short_news = Qisqa_yangiliklar.objects.all()


def Home(request):
    short = short_news.latest("-add_date")
    last_blog = blogs.latest("-add_date")
    five_blogs = blogs.order_by("id")[::-5]
    if request.method == "POST":
        form = AddTaklifForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("app:Home")
    form = AddTaklifForm
    context = {
        "blogs":blogs,
        "list":list,
        "form":form,
        "short":short,
        "rand": ran_ch,
        "tum": tumvash,
        "five":five_blogs,
        "senator":senator,
        "komissia":komisia,
        "deputat":deputat,
        "last_blog":last_blog,
    }
    return render(request, 'pages/home.html', context)

def Xodimlar(request):

    short = short_news.latest("add_date")
    context = {
        "tum": tumvash,
        "senator":senator,
        "deputat":deputat,
        "komissia":komisia,
        "short": short,
        "rand": ran_ch,

    }
    return render(request, 'pages/xodimlar.html', context)

def tuman_xodimlar(request, pk):

    tum_dep = Deputat.objects.filter(town=pk)
    short = short_news.latest("add_date")
    town = TownsName.objects.all()
    context = {
        "town": town,
        "tum": tumvash,
        "deputat": deputat,
        "tum_dep": tum_dep,
        "komission": komisia,
        "short": short,
        "rand": ran_ch,

    }
    return render(request, 'pages/tuman_deputatlari.html', context)

def admin(request):
    return render(request, 'admin_page/sidebar.html')

def doimiy_komisalar(request, pk):
    kam_azo = KomissiaAzo.objects.filter(komissia=pk)
    short = short_news.latest("add_date")
    komisia = Komissia.objects.all()
    context = {
        "list": list,
        "tum": tumvash,
        "komissia":komisia,
        "kam_azo":kam_azo,
        "short": short,
        "rand": ran_ch,

    }
    return render(request, 'pages/doimiy_komisia.html', context)

def all_blog(request):
    short = short_news.latest("add_date")
    context = {
        'list': list,
        "tum": tumvash,
        "komissia": komisia,
        "short": short,
        "rand": ran_ch,
        "blogs":blogs,

    }
    return render(request, 'pages/blogs.html', context)

def BlogDetail(request, pk):
    blog = blogs.get(pk=pk)
    short = short_news.latest("add_date")
    context = {
        'list': list,
        "blog":blog,
        "tum": tumvash,
        "komissia": komisia,
        "short": short,
        "rand": ran_ch,

    }
    return render(request, 'pages/blog.html', context)

def Work_plan(request):
    short = short_news.latest("add_date")
    context = {
        "files": file,
        "tum": tumvash,
        "komissia":komisia,
        "short": short,
        "rand": ran_ch,

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
    short = short_news.latest("add_date")
    context = {
        "tum": tumvash,
        "komissia":komisia,
        "short": short,
        "rand": ran_ch,

    }
    return render(request, 'pages/full_cv.html', context)

def Empty(request):
    short = short_news.latest("add_date")
    context = {
        "tum": tumvash,
        "komissia":komisia,
        "short":short,
        "rand": ran_ch,

    }
    return render(request, 'pages/none.html', context)
