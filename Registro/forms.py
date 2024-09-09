from django import forms

class AmpFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    fecha = forms.DateField()
    imagen = forms.ImageField()

class PedalFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    fecha = forms.DateField()
    imagen = forms.ImageField()

class InstFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    fecha = forms.DateField()
    imagen = forms.ImageField()

class PortaFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    fecha = forms.DateField()
    imagen = forms.ImageField()


