from django.contrib import admin
from .models import (
    TownsName,
    Deputat,
    KomissiaAzo,
    Komissia,
    Partia,
    Blogs,
    Senator,
    Taklif,
    Files,
    Qisqa_yangiliklar,
)
# Register your models here.

admin.site.register(TownsName)
admin.site.register(KomissiaAzo)
admin.site.register(Deputat)
admin.site.register(Komissia)
admin.site.register(Partia)
admin.site.register(Blogs)
admin.site.register(Senator)
admin.site.register(Taklif)
admin.site.register(Files)
admin.site.register(Qisqa_yangiliklar)
