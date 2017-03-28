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
        return self.mark + " - " + self.name


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
        if self.manufacturer.name == "Kadee":
            return "Kadee " + self.name
        else:
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
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField()
    livery = models.CharField(max_length=50, null=True, blank=True)
    coupler = models.ForeignKey(Coupler, null=True, blank=True, on_delete=models.CASCADE)
    couplerTuned = models.NullBooleanField()
    length = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    stocktype = models.ForeignKey(StockType, on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank=True)
    modelnumber = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

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
    power = models.ForeignKey(Power, on_delete=models.CASCADE)
    axles = models.IntegerField(null=True, blank=True)
    address = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "locomotive"
        ordering = ["railroad", "number"]
    def __str__(self):
        return self.railroad + " " + self.number


class WheelMaterial(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "wheelmaterial"
        ordering = ["name"]
    def __str__(self):
        return self.name


class WheelSet(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, on_delete=models.CASCADE)
    material = models.ForeignKey(WheelMaterial, on_delete=models.CASCADE)

    class Meta:
        db_table = "wheelset"
        ordering = ["name"]
    def __str__(self):
        return str(self.manufacturer) + " " + self.name + " (" + str(self.material) + ")"


class Car(RollingStock):
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    wheelset = models.ForeignKey(WheelSet, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def lengthInInches(self):
        return round(((float(self.length) * 12) / 87), 1)

    @property
    def idealWeight(self):
        return (self.lengthInInches * .5) + 1

    @property
    def weightDifference(self):
        return self.idealWeight - float(self.weight)

    @property
    def isOverWeight(self):
        if float(self.weight) > self.idealWeight:
            return True
        else:
            return False

    @property
    def isUnderWeight(self):
        if float(self.weight) < self.idealWeight:
            return True
        else:
            return False

    @property
    def weightDifferencePercentage(self):
        return abs(int(round((float(self.weightDifference/self.idealWeight) * 100), 0)))

    @property
    def weightOverOrUnder(self):
        if float(self.weight) < self.idealWeight:
            return "UNDER"
        elif float(self.weight) > self.idealWeight:
            return "OVER"
        else:
            return ""

    class Meta:
        db_table = "car"
        ordering = ["railroad", "type", "number"]
    def __str__(self):
        return str(self.railroad) + " " + str(self.number) + "(" + str(type) + ")"


class CarFeature(models.Model):
    name = models.CharField(max_length=50)
    cars = models.ManyToManyField(Car, blank=True)

    class Meta:
        db_table = "carfeature"
        ordering = ["name"]
    def __str__(self):
        return self.name
