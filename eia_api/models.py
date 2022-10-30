from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.


class Machines(models.Model):
    machine_name = models.CharField(max_length=250)
    buy_date = models.DateField("fecha de compra", auto_now_add=True)
    marca = models.CharField(max_length=250)


class Devices(models.Model):
    machine_name = models.ForeignKey(Machines, on_delete=SET_NULL, null=True)
    buy_date = models.DateField("fecha de compra", auto_now_add=True)
    marca = models.CharField(max_length=250)
