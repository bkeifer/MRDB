from django import forms

from .models import Coupler, Make, Manufacturer, Railroad

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


class RailroadForm(forms.ModelForm):

    class Meta:
        model = Railroad
        fields = ('mark', 'name')
