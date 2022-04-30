from django.contrib import admin
from .models import (
    TownsName, 
    Deputat, 
    KomissiaAzo, 
    Komissia, 
    Partia, 
    Blogs
)
# Register your models here.

admin.site.register(TownsName)
admin.site.register(KomissiaAzo)
admin.site.register(Deputat)
admin.site.register(Komissia)
admin.site.register(Partia)
admin.site.register(Blogs)
