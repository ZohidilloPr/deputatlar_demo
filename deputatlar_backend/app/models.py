from django.db import models

# Create your models here.
class TownsName(models.Model):
    name = models.CharField(max_length=20, verbose_name="Tuman Nomi")
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

class Kamisa(models.Model):
    name = models.CharField(max_length=250, verbose_name="Kamisa nomi")
    add_date = models.DateTimeField(auto_now_add=True)

class KamisaAzo(models.Model):
    f_name = models.CharField(max_length=100, verbose_name="To'liq ismi")
    