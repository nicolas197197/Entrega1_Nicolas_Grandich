from django.shortcuts import render
from app_MVT.models import Futbol, Basquet, Tenis
from app_MVT.forms import FutbolForm, BasquetForm, TenisForm
from django.db.models import Q


def in_futbol(request, nombre: str, numeroDeSocio: int, fechaDeIngreso: str, email: str):
    futbol = Futbol(nombre=nombre, numeroDeSocio=numeroDeSocio, fechaDeIngreso=fechaDeIngreso, email=email)
    futbol.save() # save into the DB

    context_dict = {
        'futbol': futbol
    }
    return render(
        request=request,
        context=context_dict,
        template_name="app_MVT/in_futbol.html"
    )

def futbol(request):
    futbol = Futbol.objects.all()

    context_dict = {
        'futbol': futbol
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_MVT/futbol.html"
    )

def basquet(request):
    basquet = Basquet.objects.all()

    context_dict = {
        'basquet': basquet
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_MVT/basquet.html"
    )

def tenis(request):
    tenis = Tenis.objects.all()

    context_dict = {
        'tenis': tenis
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_MVT/tenis.html"
    )

def index(request):
    return render(request,"app_MVT/inicio.html")

def futbol_forms_django(request):
    if request.method == 'POST':
        futbol_form = FutbolForm(request.POST)
        if futbol_form.is_valid():
            data = futbol_form.cleaned_data
            futbol = Futbol(
                nombre=data['nombre'], 
            numeroDeSocio=data['numeroDeSocio'], 
            fechaDeIngreso=data['fechaDeIngreso'],
            email=data['email'],
             )
            futbol.save()

            futbol = Futbol.objects.all()
            context_dict = {
                'futbol': futbol
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_MVT/futbol.html"
            )

    futbol_form = FutbolForm(request.POST)
    context_dict = {
        'futbol_form': futbol_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_MVT/futbol_django_forms.html'
    )

def basquet_forms_django(request):
    if request.method == 'POST':
        basquet_form = BasquetForm(request.POST)
        if basquet_form.is_valid():
            data = basquet_form.cleaned_data
            basquet = Basquet(
                nombre=data['nombre'], 
            numeroDeSocio=data['numeroDeSocio'], 
            fechaDeIngreso=data['fechaDeIngreso'],
            email=data['email'],
             )
            basquet.save()

            basquet = Basquet.objects.all()
            context_dict = {
                'basquet': basquet
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_MVT/basquet.html"
            )

    basquet_form = BasquetForm(request.POST)
    context_dict = {
        'basquet_form': basquet_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_MVT/basquet_django_forms.html'
    )

def tenis_forms_django(request):
    if request.method == 'POST':
        tenis_form = TenisForm(request.POST)
        if tenis_form.is_valid():
            data = tenis_form.cleaned_data
            tenis = Tenis(
                nombre=data['nombre'], 
            numeroDeSocio=data['numeroDeSocio'], 
            fechaDeIngreso=data['fechaDeIngreso'],
            email=data['email'],
             )
            tenis.save()

            tenis = Basquet.objects.all()
            context_dict = {
                'tenis': tenis
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_MVT/tenis.html"
            )

    basquet_form = BasquetForm(request.POST)
    context_dict = {
        'basquet_form': basquet_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_MVT/basquet_django_forms.html'
    )

def search(request):
    context_dict = dict()
    if request.GET['all_search_futbolistas']:
        search_param = request.GET['all_search_futbolistas']
        query = Q(nombre__contains=search_param)
        query.add(Q(numeroDeSocio__contains=search_param), Q.OR)
        futbol = Futbol.objects.filter(query)
        context_dict = {
            'futbol': futbol
        }

    elif request.GET['all_search_basquetbolistas']:
        search_param = request.GET['all_search_basquetbolistas']
        query = Q(nombre__contains=search_param)
        query.add(Q(numeroDeSocio__contains=search_param), Q.OR)
        basquet = Basquet.objects.filter(query)
        context_dict = {
            'basquet': basquet
        }

    elif request.GET['all_search_tenistas']:
        search_param = request.GET['all_search_tenistas']
        query = Q(nombre__contains=search_param)
        query.add(Q(numeroDeSocio__contains=search_param), Q.OR)
        tenis = Tenis.objects.filter(query)
        context_dict = {
            'tenis': tenis
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_MVT/inicio.html",
    )

