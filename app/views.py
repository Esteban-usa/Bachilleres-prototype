from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Favoritos

#login_required  

@login_required
def index(request):
    favoritos = Favoritos.objects.all()
    return render(request,'index.html', {'favoritos': favoritos})

def salir(request):
    logout(request)
    return redirect(to="/")
