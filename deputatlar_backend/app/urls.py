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
)

app_name = 'app'

urlpatterns = [
    path('', Home, name="Home"),
    path('all/xodimlar/', Xodimlar, name="all_xodim"),
    path('tuman/xodimlar/', tuman_xodimlar, name="tuman_xodim"),
    path('bloger', admin, name="admin"),
    path('komisia/doimiy/', doimiy_komisalar, name="DK"),
    path('all/blogs/', all_blog, name="AB"),
    path('ish/reja/', Work_plan, name="WP"),
    path('cv/', cv, name="cv"),
]

