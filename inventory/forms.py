from django import forms

from .models import CarType, Coupler, Locomotive, Make, Manufacturer, Model, Power
from .models import Railroad

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
        fields = ('railroad', 'manufacturer', 'number', 'address', 'coupler', 'length', 'power', 'stocktype', 'year', 'modelnumber', 'make', 'model', 'power', 'axles')


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
