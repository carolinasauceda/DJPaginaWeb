from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nombre',
            'apellido',
            'email',
            'telefono',
            'direccion',

        ]

        labels = {
            'id':'CURP',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'email':'Email',
            'telefono':'Telefono',
            'direccion':'Direccion de envio',
        }

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
        }