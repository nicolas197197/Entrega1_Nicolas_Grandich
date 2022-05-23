from django.shortcuts import render
from app_MVT.models import Familia



def in_familia(request, nombre: str, numero: int, fechaDeEntrega: str):
    familia = Familia(nombre=nombre, numero=numero, fechaDeEntrega=fechaDeEntrega)
    familia.save() # save into the DB

    context_dict = {
        'familia': familia
    }
    return render(
        request=request,
        context=context_dict,
        template_name="app_MVT/in_familia.html"
    )

def all_familia(request):
    familia = Familia.objects.all()

    context_dict = {
        'familia': familia
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_MVT/all_familia.html"
    )

def index(request):
    return render(request,"app_MVT/index.html")
    



