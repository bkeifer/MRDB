from django import forms

from .models import Coupler, Manufacturer, Railroad

class CouplerForm(forms.ModelForm):

    class Meta:
        model = Coupler
        fields = ('manufacturer', 'name')


class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ('name','url')


class RailroadForm(forms.ModelForm):

    class Meta:
        model = Railroad
        fields = ('mark', 'name')
