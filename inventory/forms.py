from django import forms

from .models import Car, CarType, Coupler, Locomotive, Make, Manufacturer
from .models import Model, Power, Railroad

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('railroad', 'number', 'type', 'length', 'livery', 'coupler', 'couplerTuned', 'manufacturer', 'year', 'modelnumber', 'stocktype', 'notes')


class CarTypeForm(forms.ModelForm):

    class Meta:
        model = CarType
        fields = ('name',)


class CouplerForm(forms.ModelForm):

    class Meta:
        model = Coupler
        fields = ('manufacturer', 'name')


class LocomotiveForm(forms.ModelForm):
    # stocktype = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    class Meta:
        model = Locomotive
        fields = ('railroad', 'manufacturer', 'number', 'address', 'livery', 'coupler', 'couplerTuned', 'length', 'power', 'stocktype', 'year', 'modelnumber', 'make', 'model', 'power', 'axles', 'notes')


class MakeForm(forms.ModelForm):

    class Meta:
        model = Make
        fields = ('name',)


class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ('name','url')


class ModelForm(forms.ModelForm):

    class Meta:
        model = Model
        fields = ('make', 'name')


class PowerForm(forms.ModelForm):

    class Meta:
        model = Power
        fields = ('name',)


class RailroadForm(forms.ModelForm):

    class Meta:
        model = Railroad
        fields = ('mark', 'name')
