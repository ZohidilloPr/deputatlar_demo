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