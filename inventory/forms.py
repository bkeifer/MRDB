from django import forms

from .models import Car, CarFeature, CarType, Coupler, Locomotive, Make
from .models import Manufacturer, Model, Power, Railroad, WheelMaterial, WheelSet

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('railroad', 'number', 'type', 'length', 'livery', 'coupler', 'couplerTuned', 'wheelset', 'manufacturer', 'year', 'modelnumber', 'stocktype', 'carfeatures', 'notes')

    carfeatures = forms.ModelMultipleChoiceField(queryset=CarFeature.objects.all(), required=False)
    # Overriding __init__ here allows us to provide initial
    # data for 'features' field
    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'features' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['carfeatures'] = [t.pk for t in kwargs['instance'].carfeature_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'features' field
    def save(self, commit=True):
        # Get the unsaved Car instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m
        def save_m2m():
            old_save_m2m()
            # This is where we actually link the car with features
            instance.carfeature_set.clear()
            for carfeature in self.cleaned_data['carfeatures']:
                instance.carfeature_set.add(carfeature)
        self.save_m2m = save_m2m

        if commit:
            instance.save()
            self.save_m2m()

        return instance


class CarFeatureForm(forms.ModelForm):

    class Meta:
        model = CarFeature
        fields = ('name',)


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


class WheelMaterialForm(forms.ModelForm):

    class Meta:
        model = WheelMaterial
        fields = ('name',)


class WheelSetForm(forms.ModelForm):

    class Meta:
        model = WheelSet
        fields = ('manufacturer', 'name', 'material')
