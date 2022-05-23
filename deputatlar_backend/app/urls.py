from django.urls import path
from .views import (
    Home, 
    tuman_xodimlar, 
    Xodimlar, 
    admin,
    doimiy_komisalar,
    all_blog,
    Work_plan,
    cv,
    Empty,
    BlogDetail,
    # AddTaklif
)

app_name = 'app'

urlpatterns = [
    path('cv/', cv, name="cv"),
    path('', Home, name="Home"),
    # path('/add/taklif/', AddTaklif, name="AT"),
    path('none/', Empty, name="None"),
    path('bloger', admin, name="admin"),
    path('ish/reja/', Work_plan, name="WP"),
    path('all/blogs/', all_blog, name="AB"),
    path('all/xodimlar/', Xodimlar, name="AX"),
    path('komisia/doimiy/<int:pk>/', doimiy_komisalar, name="DK"),
    path('blogs/blog/<int:pk>/', BlogDetail, name="BD"),
    path('tuman/xodimlar/<int:pk>/', tuman_xodimlar, name="TX"),
]

