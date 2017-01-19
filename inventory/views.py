from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarTypeForm, CouplerForm, MakeForm, ManufacturerForm
from .forms import ModelForm, PowerForm, RailroadForm

from .models import CarType, Coupler, Make, Manufacturer, Model, Power, Railroad
# Create your views here.

def index(request):
    manufacturerList = Manufacturer.objects.order_by('id')

    template = loader.get_template('index.html')
    context = {
        'title': "MRDB",
        'manufacturerList': manufacturerList,
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
