from django import forms

from .models import CarType, Coupler, Make, Manufacturer, Model, Railroad

class CarTypeForm(forms.ModelForm):

    class Meta:
        model = CarType
        fields = ('name',)


class CouplerForm(forms.ModelForm):

    class Meta:
        model = Coupler
        fields = ('manufacturer', 'name')


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


class RailroadForm(forms.ModelForm):

    class Meta:
        model = Railroad
        fields = ('mark', 'name')
