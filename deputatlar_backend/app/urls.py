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
    Empty
)

app_name = 'app'

urlpatterns = [
    path('cv/', cv, name="cv"),
    path('', Home, name="Home"),
    path('none/', Empty, name="None"),
    path('bloger', admin, name="admin"),
    path('ish/reja/', Work_plan, name="WP"),
    path('all/blogs/', all_blog, name="AB"),
    path('all/xodimlar/', Xodimlar, name="all_xodim"),
    path('komisia/doimiy/', doimiy_komisalar, name="DK"),
    path('tuman/xodimlar/', tuman_xodimlar, name="tuman_xodim"),
]

