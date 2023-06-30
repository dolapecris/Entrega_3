from django.contrib import admin
from .models import *
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'mensaje', 'email']
    list_editable = ['email']
    search_fields = ['nombre']
    list_filter = ['tipo_contacto']


class MecanicoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento', 'especialista']
    list_editable = ['apellido']
    search_fields = ['id']
    list_filter = ['especialista']
    
class MantencionAdmin(admin.ModelAdmin):
    list_display = ['cod','descrip', 'mecani',]
    list_editable = ['descrip']
    search_fields = ['mecani']
    list_filter = ['mecani']


admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Categoria)
admin.site.register(Mecanico, MecanicoAdmin)
admin.site.register(Mantencion, MantencionAdmin)



