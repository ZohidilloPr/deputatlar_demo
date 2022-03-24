from django.urls import path
from .views import Home, tuman_xodimlar, Xodimlar, admin

app_name = 'app'

urlpatterns = [
    path('', Home, name="Home"),
    path('all/xodimlar/', Xodimlar, name="all_xodim"),
    path('tuman/xodimlar/', tuman_xodimlar, name="tuman_xodim"),
    path('bloger', admin, name="admin"),
]

