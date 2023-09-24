from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Beca

#login_required  

@login_required
def base(request):
    return render(request,'base.html')

def salir(request):
    logout(request)
    return redirect(to="/")

def list_becas(request):
    becas=list(Beca.objects.values())
    data={'Becas':becas}
    return JsonResponse(data)