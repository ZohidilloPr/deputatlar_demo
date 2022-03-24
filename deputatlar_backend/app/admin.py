from django.contrib import admin
from .models import (
    TownsName, 
    Deputat, 
    KamisaAzo, 
    Kamisa, 
    Partia, 
    Blogs
)
# Register your models here.

admin.site.register(TownsName)
admin.site.register(KamisaAzo)
admin.site.register(Deputat)
admin.site.register(Kamisa)
admin.site.register(Partia)
admin.site.register(Blogs)
