from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'pages/home.html')
def Xodimlar(request):
    return render(request, 'pages/xodimlar.html')
def tuman_xodimlar(request):
    return render(request, 'pages/tuman_deputatlari.html')
def admin(request):
    return render(request, 'admin_page/sidebar.html')
def doimiy_komisalar(request):
    return render(request, 'pages/doimiy_komisia.html')
def all_blog(request):
    return render(request, 'pages/all_blogs.html')
def Work_plan(request):
    return render(request, 'pages/ish_reja.html')
def cv(request):
    return render(request, 'pages/full_cv.html')









