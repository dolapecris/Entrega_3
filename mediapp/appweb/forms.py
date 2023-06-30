from django import forms
from .models import Contacto, Mecanico, Mantencion

class ContactoForm(forms.ModelForm):
    model = Contacto
    fields = "__all__"
    
class MecanicoForm(forms.ModelForm):
    
    class Meta:
        model = Mecanico
        fields = ["rut", "nombre", "apellido", "edad", "especialista", "fecha_nacimiento", "categoria", "foto"]
        
        Widgets = {
            "fecha_nacimiento": forms.SelectDateWidget()   
        }

class MantencionForm(forms.ModelForm):
    model = Mantencion
    fields = ["id", "descripcion"]
