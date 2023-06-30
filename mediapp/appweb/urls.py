from django.urls import path
from .views import mantencion, agregar_mantencion,listar_mantencion,modificar_mantencion,eliminar_mantencion,registro_mecanico, home, mecanico, contacto, agregar_mecanico, listar_mecanico, modificar_mecanico, eliminar_mecanico, login_usuario

urlpatterns = [
    path('home/', home, name="home"),
    path ('', home, name="home"),
    path('mecanico/', mecanico, name="mecanico"),
    path('contacto/', contacto, name="contacto"),
    path('mantenedor/mecanico/agregar', agregar_mecanico, name="agregar_mecanico"),
    path('mantenedor/mecanico/listar', listar_mecanico, name="listar_mecanico"),
    path('mantenedor/mecanico/modificar/<rut>', modificar_mecanico, name="modificar_mecanico"),
    path('mantenedor/mecanico/eliminar/<rut>', eliminar_mecanico, name="eliminar_mecanico"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro_mecanico/', registro_mecanico, name="reg_mecanico"),
    path('mantencion/', mantencion, name="mantencion"),
    path('mantenedor/mantencion/agregar', agregar_mantencion, name="agregar_mantencion"),
    path('mantenedor/mantencion/listar', listar_mantencion, name="listar_mantencion"),
    path('mantenedor/mantencion/modificar/<cod>', modificar_mantencion, name="modificar_mantencion"),
    path('mantenedor/mantencion/eliminar/<cod>', eliminar_mantencion, name="eliminar_mantencion"),
]   
