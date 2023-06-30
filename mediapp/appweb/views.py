from django.shortcuts import render, redirect, get_object_or_404
from .models import Mecanico, Mantencion
from .forms import ContactoForm, MecanicoForm, MantencionForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
    
    messages.success(request, "Primer mensaje")
    
    request.session["mensaje"] = "Hola"
    
    return render(request,"home.html")


@login_required(login_url='/accounts/login')
@permission_required(['appweb.add_contacto'], login_url='/accounts/login')

def mecanico(request):
    
    mecanico = Mecanico.objects.all()
    
    data = {
        'mecanico' : mecanico
    }   
    
    if request.method =="POST":
        valor_buscado = request.POST.get("valor_buscado")
        if valor_buscado != "":
            mecanico = Mecanico.objects.filter(rut =valor_buscado)
            data["mecanico"] = mecanico
        else:
            data["mecanico"] = Mecanico.objects.all()
            
    messages.success(request, request.session["mensaje"])
    
    #mecanico = Mecanico.objetcs.raw("Select * from appweb_mecanico where especialista = true")
    
     
    
    return render(request,"mecanico.html", data)


def contacto(request):
    
    data = {
        'form': ContactoForm,
        'mensaje': ""
    }
    
    if request.method =="POST":
        formulario = ContactoForm(data=request.POST)
        
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto Guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio Un Error"
    
    return render(request,"contacto.html", data)


def agregar_mecanico(request):
    
    data = {
        'form': MecanicoForm,
        'mensaje': ""
    }
    
    if request.method =="POST":
        formulario = MecanicoForm(data=request.POST, files = request.FILES)
        
        if formulario.is_valid():
            mec = formulario.save(commit=False)
            mec.usuario = request.user

            mec.save()
                        
            data['mensaje'] = "Mecanico Guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio Un Error"
    
    return render(request,"mantenedor/mecanico/agregar.html", data)


def listar_mecanico(request):
    
    mecanico = Mecanico.objects.all()
    data = {
        'mecanico': mecanico
    }
    
    return render(request, "mantenedor/mecanico/listar.html", data)


def modificar_mecanico(request, rut):
    
    mecanico = get_object_or_404(Mecanico, rut=rut)
    
    data = {
        
        "form" : MecanicoForm(instance = mecanico)
    }
    
    if request.method =="POST":
        formulario = MecanicoForm(data=request.POST, instance=mecanico, files = request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(to= "listar_mecanico")
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio Un Error"
            
    return render(request, "mantenedor/mecanico/modificar.html", data)


def eliminar_mecanico(request, rut):
    mecanico = get_object_or_404(Mecanico, rut=rut)
    
    mecanico.delete()
    
    return redirect(to=listar_mecanico)


def login_usuario(request):
    
    print("Bienvenido: "+ request.user.username)
    print("Este es el login")
    
    print('grupos: ', request.user.groups.all())
    
    if request.user.groups.filter(name__in=['mecanico']):
        print('usuario pertenece a grupo mecanico')
    
    return redirect(to='home')


def registro_mecanico(request):
    
    data = {
        "mensaje" :""
    }
    
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            data["mensaje"] = "Las contraseñas deben ser iguales"
        else:
            usu = User()
            usu.set_password(password1)
            usu.email = correo
            usu.username = nombre
            usu.last_name = apellido
            usu.first_name = nombre
            grupo = Group.objects.get(name='mecanico')
        try:
            usu.save()
            usu.groups.add(grupo)
            data['mensaje']= 'Usuario creado correctamente'
            
            user = authenticate(username=usu.name, password=password1)
            login(request, user)
            return redirect(to='home')
        except:
            data['mensaje']= 'Error al grabar'
    
    return render(request, "registration/registro.html", data)

def mantencion(request):
    
    mantencion = Mantencion.objects.all()
    
    data = {
        'mantencion' : mantencion
    }   
    
    if request.method =="POST":
        valor_buscado = request.POST.get("valor_buscado")
        if valor_buscado != "":
            mantencion = Mantencion.objects.filter(rut =valor_buscado)
            data["mantencion"] = mantencion
        else:
            data["mantencion"] = Mantencion.objects.all()
            
    
    
    mantencion = Mantencion.objetcs.raw("Select * from appweb_mantencion where mecani = true")
    
     
    
    return render(request,"mantencion.html", data)


def agregar_mantencion(request):
    
    data = {
        'form': MantencionForm,
        'mensaje': ""
    }
    
    if request.method =="POST":
        formulario = MantencionForm(data=request.POST, files = request.FILES)
        
        if formulario.is_valid():
            man = formulario.save(commit=False)
            man.usuario = request.user

            man.save()
                        
            data['mensaje'] = "Mantencion Guardada"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio Un Error"
    
    return render(request,"mantenedor/mantencion/agregar.html", data)


def listar_mantencion(request):
    
    mantencion = Mantencion.objects.all()
    data = {
        'mantencion': mantencion
    }
    
    return render(request, "mantenedor/mantencion/listar.html", data)


def modificar_mantencion(request, id):
    
    mantencion = get_object_or_404(Mantencion, id=id)
    
    data = {
        
        "form" : MantencionForm(instance = mantencion)
    }
    
    if request.method =="POST":
        formulario = MantencionForm(data=request.POST, instance=mantencion, files = request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(to= "listar_mantencion")
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio Un Error"
            
    return render(request, "mantenedor/mantencion/modificar.html", data)


def eliminar_mantencion(request, id):
    mantencion = get_object_or_404(Mantencion, id=id)
    
    mantencion.delete()
    
    return redirect(to=listar_mantencion)

