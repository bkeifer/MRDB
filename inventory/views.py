from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CouplerForm, MakeForm, ManufacturerForm, RailroadForm

from .models import Coupler, Make, Manufacturer, Railroad
# Create your views here.

def index(request):
    manufacturerList = Manufacturer.objects.order_by('id')

    template = loader.get_template('index.html')
    context = {
        'title': "MRDB",
        'manufacturerList': manufacturerList,
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
