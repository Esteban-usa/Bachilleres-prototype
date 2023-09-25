from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Becas_Fav,Beca

#login_required  

@login_required
def index(request):
    
    if request.user.is_authenticated:
        becas = Beca.objects.all()
        favoritos = Becas_Fav.objects.filter(usuario=request.user)
        return render(request,'index.html', {'favoritos': favoritos,'becas':becas})

    else:
        favoritos = Becas_Fav.objects.all()
        return render(request,'index.html', {'favoritos': favoritos})

def salir(request):
    logout(request)
    return redirect(to="/")
