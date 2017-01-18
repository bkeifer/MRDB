from django.contrib import admin

from .models import Car, CarType, Coupler, Locomotive, Make, Manufacturer
from .models import Model, Railroad, StockType

# Register your models here.
admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(Coupler)
admin.site.register(Locomotive)
admin.site.register(Make)
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Railroad)
admin.site.register(StockType)
