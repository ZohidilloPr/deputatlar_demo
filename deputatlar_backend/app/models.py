from django.db import models

# Create your models here.

lavozim = (
    ('Komissia rayisi', 'Komissia rayisi'),
    ('Komissia rayisi o\'rinbosari', 'Komissia rayisi o\'rinbosari'),
    ('Komissia azolari', 'Komissia azolari'),
)
class TownsName(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tuman Nomi", unique=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Partia(models.Model):
    name = models.CharField(max_length=150, verbose_name="Partia nomini kiriting")
    add_date = models.DateTimeField(auto_now_add=True)

class Deputat(models.Model):
    f_name = models.CharField(verbose_name="To'liq ismi", max_length=100)
    partia = models.ForeignKey(Partia, on_delete=models.CASCADE, verbose_name="Qaysi partia")
    town = models.ForeignKey(TownsName, on_delete=models.CASCADE, verbose_name="Qaysi tuman")
    phone = models.CharField(max_length=10, verbose_name="Telefon raqami")
    email = models.EmailField(verbose_name="Electron pochta")
    faks = models.CharField(max_length=9, verbose_name="Faks nomeri")
    image = models.ImageField(verbose_name="Rasmi")
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
    f_name = models.CharField(max_length=100, verbose_name="To'liq ismi")
    lavozim_type = models.CharField(max_length=50, verbose_name="Lavozim turi", choices=lavozim, default='Komissia azolari')
    lavozim_now = models.CharField(max_length=250, verbose_name="Hozirgi egallab turgan lavozimi")
    number = models.CharField(verbose_name="Saylangan saylov okrugi", max_length=25)
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.f_name
    
class Blogs(models.Model):
    image = models.ImageField(verbose_name="Yangilik uchun rasim")
    title = models.CharField(verbose_name="Sarlavha", unique=True, max_length=200)
    blog = models.TextField(verbose_name="Maqola")
    add_date = models.DateTimeField(verbose_name=("Published date"), auto_now_add=True)