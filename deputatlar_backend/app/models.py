from unicodedata import name
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

lavozim = (
    ('Komissia rayisi', 'Komissia rayisi'),
    ('Komissia rayisi o\'rinbosari', 'Komissia rayisi o\'rinbosari'),
    ('Komissia azolari', 'Komissia azolari'),
)
LANG = (
    ('uz', 'UZ'),
    ('уз', 'УЗ'),
)
class TownsName(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tuman Nomi", unique=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Partia(models.Model):
    name = models.CharField(max_length=150, verbose_name="Partia nomini kiriting")
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Senator(models.Model):
    f_name = models.CharField(_("Senatorning to'liq ismi"), max_length=300)
    senat_img = models.ImageField(_("Senator rasmi"), upload_to='senator_images/')
    phone = models.IntegerField(_("Telefon raqami"))
    email = models.EmailField(_("E-Pochta manzili"), max_length=254)
    faks = models.IntegerField(_("Faks Nomeri"))
    
    def __str__(self):
        return self.f_name
    
class Deputat(models.Model):
    f_name = models.CharField(verbose_name="To'liq ismi", max_length=100)
    partia = models.ForeignKey(Partia, on_delete=models.CASCADE, verbose_name="Qaysi partia")
    town = models.ForeignKey(TownsName, on_delete=models.CASCADE, verbose_name="Qaysi tuman")
    phone = models.CharField(max_length=10, verbose_name="Telefon raqami")
    email = models.EmailField(verbose_name="Electron pochta")
    faks = models.CharField(max_length=9, verbose_name="Faks nomeri")
    image = models.ImageField(verbose_name="Rasmi", upload_to='Deputatlar/')
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name

class Komissia(models.Model):
    name = models.CharField(max_length=500, verbose_name="Komissia nomi", unique=True)
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class KomissiaAzo(models.Model):
    komissia = models.ForeignKey(Komissia, verbose_name="Qaysi komissiaga azo", on_delete=models.CASCADE)
    azo_img = models.ImageField(_("A'zoning rasmi"), upload_to='Komisia_Azolar/', height_field=None, width_field=None, max_length=None)
    f_name = models.CharField(max_length=100, verbose_name="To'liq ismi")
    lavozim_type = models.CharField(max_length=50, verbose_name="Lavozim turi", choices=lavozim, default='Komissia azolari')
    lavozim_now = models.CharField(max_length=250, verbose_name="Hozirgi egallab turgan lavozimi")
    number = models.CharField(verbose_name="Saylangan saylov okrugi", max_length=25)
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.f_name
    
class Blogs(models.Model):
    lang = models.CharField(verbose_name="Tilni tanlang", max_length=50, choices=LANG, default='uz')
    image = models.ImageField(verbose_name="Yangilik uchun rasim", upload_to='Blogs/')
    title = models.CharField(verbose_name="Sarlavha", unique=True, max_length=200)
    blog = models.TextField(verbose_name="Maqola")
    add_date = models.DateTimeField(verbose_name=("Published date"), auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Taklif(models.Model):
    f_name = models.CharField(_("Full Name"), max_length=150)
    phone = models.IntegerField(_("Phone Number"))
    subject = models.CharField(_("Mazmuni"), max_length=150)
    comment = models.TextField(_("Izoh"))
    
    def __str__(self):
        return self.subject
    
class Files(models.Model):
    name = models.CharField(_("Fayl nomi"), max_length=500)
    file = models.FileField(_("Fayl"), upload_to='Xujjatlar')
    upload_date = models.DateTimeField(_("Yuklangan vaqti"), auto_now_add=True)
    
    def __str__(self):
        return self.name

class Qisqa_yangiliklar(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlovha")
    xabar = models.TextField(verbose_name="Yangilik Mazmuni")
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title