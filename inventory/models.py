from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Railroad(models.Model):
    name = models.CharField(max_length=100)
    mark = models.CharField(max_length=5)

    class Meta:
        db_table = "railroad"
        ordering = ["name"]
    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "manufacturer"
        ordering = ["name"]
    def __str__(self):
        return self.name


class Coupler(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    class Meta:
        db_table = "coupler"
        ordering = ["name"]
    def __str__(self):
        return self.name


class Make(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "make"
        ordering = ["name"]
    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=20)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

    class Meta:
        db_table = "model"
        ordering = ["name"]
    def __str__(self):
        return self.name


class StockType(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "stocktype"
        ordering = ["name"]
    def __str__(self):
        return self.name


class CarType(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        db_table = "cartype"
        ordering = ["name"]
    def __str__(self):
        return self.name


class RollingStock(models.Model):
    railroad = models.ForeignKey(Railroad, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    number = models.IntegerField()
    coupler = models.ForeignKey(Coupler, on_delete=models.CASCADE)
    length = models.IntegerField()
    stocktype = models.ForeignKey(StockType, on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    modelnumber = models.CharField(max_length=20, null=True)

    class Meta:
        abstract = True


class Power(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        db_table = "power"
        ordering = ["name"]
    def __str__(self):
        return self.name

        
class Locomotive(RollingStock):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    axles = models.IntegerField()

    class Meta:
        db_table = "locomotive"
        ordering = ["railroad", "number"]
    def __str__(self):
        return self.railroad + " " + self.number


class Car(RollingStock):
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)

    class Meta:
        db_table = "car"
        ordering = ["railroad", "type", "number"]
    def __str__(self):
        return self.railroad + " " + self.number + "(" + type + ")"
