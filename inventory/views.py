from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from django.forms import HiddenInput

from .forms import CarForm, CarFeatureForm, CarTypeForm, CouplerForm
from .forms import LocomotiveForm, MakeForm, ManufacturerForm, ModelForm
from .forms import PowerForm, RailroadForm

from .models import Car, CarFeature, CarType, Coupler, Locomotive, Make
from .models import Manufacturer, Model, Power, Railroad, StockType

def index(request):
    carList = Car.objects.order_by('id')
    locomotiveList = Locomotive.objects.order_by('id')
    manufacturerList = Manufacturer.objects.order_by('id')
    railroadList = Railroad.objects.order_by('id')

    template = loader.get_template('index.html')
    context = {
        'title': "MRDB",
        'carList': carList,
        'locomotiveList': locomotiveList,
        'manufacturerList': manufacturerList,
        'railroadList': railroadList
    }
    return HttpResponse(template.render(context, request))


# --------------------------------------------------------[ CAR ]---------------
def car_create(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('car_list')
    else:
        form = CarForm(initial={'stocktype': get_object_or_404(StockType, pk=2)})
        form.fields['stocktype'].widget = HiddenInput()

    template = loader.get_template('carEdit.html')
    context = {
        'title': "New Car",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def car_delete(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        car.delete()
        return redirect('car_list')
    except:
        noop = ""

def car_edit(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)

    template = loader.get_template('carEdit.html')
    context = {
        'title': "Edit Car",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def car_list(request):
    carList = Car.objects.order_by('railroad', 'number')
    template = loader.get_template('carList.html')
    context = {
        'carList': carList,
    }
    return HttpResponse(template.render(context, request))


# --------------------------------------------------------[ CAR FEATURE ]-------
def carfeature_create(request):
    if request.method == "POST":
        form = CarFeatureForm(request.POST)
        if form.is_valid():
            carfeature = form.save()
            return redirect('carfeature_list')
    else:
        form = CarFeatureForm()

    template = loader.get_template('carfeatureEdit.html')
    context = {
        'title': "New CarFeature",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def carfeature_delete(request, carfeature_id):
    try:
        carfeature = CarFeature.objects.get(id=carfeature_id)
        carfeature.delete()
        return redirect('carfeature_list')
    except:
        noop = ""

def carfeature_edit(request, carfeature_id):
    carfeature = get_object_or_404(CarFeature, pk=carfeature_id)
    if request.method == "POST":
        form = CarFeatureForm(request.POST, instance=carfeature)
        if form.is_valid():
            carfeature = form.save()
            return redirect('carfeature_list')
    else:
        form = CarFeatureForm(instance=carfeature)

    template = loader.get_template('carfeatureEdit.html')
    context = {
        'title': "Edit Car Feature",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def carfeature_list(request):
    carfeatureList = CarFeature.objects.order_by('name')
    template = loader.get_template('carfeatureList.html')
    context = {
        'carfeatureList': carfeatureList,
    }
    return HttpResponse(template.render(context, request))


# --------------------------------------------------------[ CAR TYPE ]----------
def cartype_create(request):
    if request.method == "POST":
        form = CarTypeForm(request.POST)
        if form.is_valid():
            cartype = form.save()
            return redirect('cartype_list')
    else:
        form = CarTypeForm()

    template = loader.get_template('cartypeEdit.html')
    context = {
        'title': "New CarType",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def cartype_delete(request, cartype_id):
    try:
        cartype = CarType.objects.get(id=cartype_id)
        cartype.delete()
        return redirect('cartype_list')
    except:
        noop = ""

def cartype_edit(request, cartype_id):
    cartype = get_object_or_404(CarType, pk=cartype_id)
    if request.method == "POST":
        form = CarTypeForm(request.POST, instance=cartype)
        if form.is_valid():
            cartype = form.save()
            return redirect('cartype_list')
    else:
        form = CarTypeForm(instance=cartype)

    template = loader.get_template('cartypeEdit.html')
    context = {
        'title': "Edit CarType",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def cartype_list(request):
    cartypeList = CarType.objects.order_by('name')
    template = loader.get_template('cartypeList.html')
    context = {
        'cartypeList': cartypeList,
    }
    return HttpResponse(template.render(context, request))


# --------------------------------------------------------[ COUPLER ]-----------
def coupler_create(request):
    if request.method == "POST":
        form = CouplerForm(request.POST)
        if form.is_valid():
            coupler = form.save()
            return redirect('coupler_list')
    else:
        form = CouplerForm()

    template = loader.get_template('couplerEdit.html')
    context = {
        'title': "New Coupler",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def coupler_delete(request, coupler_id):
    try:
        coupler = Coupler.objects.get(id=coupler_id)
        coupler.delete()
        return redirect('coupler_list')
    except:
        noop = ""

def coupler_edit(request, coupler_id):
    coupler = get_object_or_404(Coupler, pk=coupler_id)
    if request.method == "POST":
        form = CouplerForm(request.POST, instance=coupler)
        if form.is_valid():
            coupler = form.save()
            return redirect('coupler_list')
    else:
        form = CouplerForm(instance=coupler)

    template = loader.get_template('couplerEdit.html')
    context = {
        'title': "Edit Coupler",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def coupler_list(request):
    couplerList = Coupler.objects.order_by('manufacturer', 'name')
    template = loader.get_template('couplerList.html')
    context = {
        'couplerList': couplerList,
    }
    return HttpResponse(template.render(context, request))


# --------------------------------------------------------[ POWER ]-------------
def power_create(request):
    if request.method == "POST":
        form = PowerForm(request.POST)
        if form.is_valid():
            power = form.save()
            return redirect('power_list')
    else:
        form = PowerForm()

    template = loader.get_template('powerEdit.html')
    context = {
        'title': "New Power",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def power_delete(request, power_id):
    try:
        power = Power.objects.get(id=power_id)
        power.delete()
        return redirect('power_list')
    except:
        noop = ""

def power_edit(request, power_id):
    power = get_object_or_404(Power, pk=power_id)
    if request.method == "POST":
        form = PowerForm(request.POST, instance=power)
        if form.is_valid():
            power = form.save()
            return redirect('power_list')
    else:
        form = PowerForm(instance=power)

    template = loader.get_template('powerEdit.html')
    context = {
        'title': "Edit Power",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def power_list(request):
    powerList = Power.objects.order_by('name')
    template = loader.get_template('powerList.html')
    context = {
        'powerList': powerList,
    }
    return HttpResponse(template.render(context, request))


# --------------------------------------------------------[ LOCOMOTIVE ]--------
def locomotive_create(request):
    if request.method == "POST":
        form = LocomotiveForm(request.POST)
        if form.is_valid():
            locomotive = form.save()
            return redirect('locomotive_list')
    else:
        form = LocomotiveForm(initial={'stocktype': get_object_or_404(StockType, pk=1)})
        form.fields['stocktype'].widget = HiddenInput()

    template = loader.get_template('locomotiveEdit.html')
    context = {
        'title': "New Locomotive",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def locomotive_delete(request, locomotive_id):
    try:
        locomotive = Locomotive.objects.get(id=locomotive_id)
        locomotive.delete()
        return redirect('locomotive_list')
    except:
        noop = ""

def locomotive_edit(request, locomotive_id):
    locomotive = get_object_or_404(Locomotive, pk=locomotive_id)
    if request.method == "POST":
        form = LocomotiveForm(request.POST, instance=locomotive)
        if form.is_valid():
            locomotive = form.save()
            return redirect('locomotive_list')
    else:
        form = LocomotiveForm(instance=locomotive)

    template = loader.get_template('locomotiveEdit.html')
    context = {
        'title': "Edit Locomotive",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def locomotive_list(request):
    locomotiveList = Locomotive.objects.order_by('railroad', 'number')
    template = loader.get_template('locomotiveList.html')
    context = {
        'locomotiveList': locomotiveList,
    }
    return HttpResponse(template.render(context, request))


# --------------------------------------------------------[ RAILROAD ]----------
def railroad_create(request):
    if request.method == "POST":
        form = RailroadForm(request.POST)
        if form.is_valid():
            railroad = form.save()
            return redirect('railroad_list')
    else:
        form = RailroadForm()

    template = loader.get_template('railroadEdit.html')
    context = {
        'title': "New Railroad",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def railroad_delete(request, railroad_id):
    try:
        railroad = Railroad.objects.get(id=railroad_id)
        railroad.delete()
        return redirect('railroad_list')
    except:
        noop = ""

def railroad_edit(request, railroad_id):
    railroad = get_object_or_404(Railroad, pk=railroad_id)
    if request.method == "POST":
        form = RailroadForm(request.POST, instance=railroad)
        if form.is_valid():
            railroad = form.save()
            return redirect('railroad_list')
    else:
        form = RailroadForm(instance=railroad)

    template = loader.get_template('railroadEdit.html')
    context = {
        'title': "Edit Railroad",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def railroad_list(request):
    railroadList = Railroad.objects.order_by('mark')
    template = loader.get_template('railroadList.html')
    context = {
        'railroadList': railroadList,
    }
    return HttpResponse(template.render(context, request))


# --------------------------------------------------------[ MAKE ]--------------
def make_create(request):
    if request.method == "POST":
        form = MakeForm(request.POST)
        if form.is_valid():
            make = form.save()
            return redirect('make_list')
    else:
        form = MakeForm()

    template = loader.get_template('makeEdit.html')
    context = {
        'title': "New Make",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def make_edit(request, make_id):
    make = get_object_or_404(Make, pk=make_id)
    if request.method == "POST":
        form = MakeForm(request.POST, instance=make)
        if form.is_valid():
            make = form.save()
            return redirect('make_list')
    else:
        form = MakeForm(instance=make)

    template = loader.get_template('makeEdit.html')
    context = {
        'title': "Edit Make",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def make_list(request):
    makeList = Make.objects.order_by('name')
    template = loader.get_template('makeList.html')
    context = {
        'makeList': makeList,
    }
    return HttpResponse(template.render(context, request))

def make_delete(request, make_id):
    try:
        make = Make.objects.get(id=make_id)
        make.delete()
        return redirect('make_list')
    except:
        noop = ""


# --------------------------------------------------------[ MANUFACTURER ]------
def manufacturer_create(request):
    if request.method == "POST":
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            manufacturer = form.save()
            return redirect('manufacturer_list')
    else:
        form = ManufacturerForm()

    template = loader.get_template('manufacturerEdit.html')
    context = {
        'title': "New Manufacturer",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def manufacturer_edit(request, manufacturer_id):
    manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
    if request.method == "POST":
        form = ManufacturerForm(request.POST, instance=manufacturer)
        if form.is_valid():
            manufacturer = form.save()
            return redirect('manufacturer_list')
    else:
        form = ManufacturerForm(instance=manufacturer)

    template = loader.get_template('manufacturerEdit.html')
    context = {
        'title': "Edit Manufacturer",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def manufacturer_list(request):
    manufacturerList = Manufacturer.objects.order_by('name')
    template = loader.get_template('manufacturerList.html')
    context = {
        'manufacturerList': manufacturerList,
    }
    return HttpResponse(template.render(context, request))

def manufacturer_delete(request, manufacturer_id):
    try:
        manufacturer = Manufacturer.objects.get(id=manufacturer_id)
        manufacturer.delete()
        return redirect('manufacturer_list')
    except:
        noop = ""


# --------------------------------------------------------[ MODEL ]-------------
def model_create(request):
    if request.method == "POST":
        form = ModelForm(request.POST)
        if form.is_valid():
            model = form.save()
            return redirect('model_list')
    else:
        form = ModelForm()

    template = loader.get_template('modelEdit.html')
    context = {
        'title': "New Model",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def model_delete(request, model_id):
    try:
        model = Model.objects.get(id=model_id)
        model.delete()
        return redirect('model_list')
    except:
        noop = ""

def model_edit(request, model_id):
    model = get_object_or_404(Model, pk=model_id)
    if request.method == "POST":
        form = ModelForm(request.POST, instance=model)
        if form.is_valid():
            model = form.save()
            return redirect('model_list')
    else:
        form = ModelForm(instance=model)

    template = loader.get_template('modelEdit.html')
    context = {
        'title': "Edit Model",
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def model_list(request):
    modelList = Model.objects.order_by('make', 'name')
    template = loader.get_template('modelList.html')
    context = {
        'modelList': modelList,
    }
    return HttpResponse(template.render(context, request))
