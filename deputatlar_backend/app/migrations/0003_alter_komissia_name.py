# Generated by Django 4.0.3 on 2022-04-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_townsname_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komissia',
            name='name',
            field=models.CharField(max_length=500, unique=True, verbose_name='Komissia nomi'),
        ),
    ]
