from django.shortcuts import render, HttpResponse , redirect
from Registro.models import Amp , Instrumento, Pedal, Portapuas
from Registro.forms import AmpFormulario, PedalFormulario, InstFormulario, PortaFormulario
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(req):
    return render(req, "Registro/index.html")

def sobremi(req):
     return render(req, "Registro/sobremi.html")


# def pedal(req):
#      return render(req, "Registro/pedal.html")


# def instrumento(req):
#      return render(req, "Registro/instrumento.html")

# @login_required
# def portapuas(req):
#      return render(req, "Registro/portapuas.html")




# def amp_formulario(request):

#      if request.method == "POST":

#           ampFormulario = AmpFormulario(request.POST, request.FILES)
#           print(ampFormulario)

#           if ampFormulario.is_valid():

#                informacion = ampFormulario.cleaned_data
#                amp = Amp(nombre=informacion["nombre"], modelo=informacion["modelo"], tipo=informacion["tipo"], descripcion=informacion["descripcion"], precio=informacion["precio"], fecha=informacion["fecha"], imagen=informacion["imagen"])
#                amp.save()
#                return redirect('amp')
#      else:
#            ampFormulario = AmpFormulario()

#      return render(request,"Registro/ampFormulario.html", {"ampFormulario" : ampFormulario})


# def pedal_formulario(request):

#      if request.method == "POST":

#           pedalFormulario = PedalFormulario(request.POST,request.FILES)
#           print(pedalFormulario)

#           if pedalFormulario.is_valid():

#                informacion = pedalFormulario.cleaned_data
#                pedal = Pedal(nombre=informacion["nombre"], modelo=informacion["modelo"], tipo=informacion["tipo"], descripcion=informacion["descripcion"], precio=informacion["precio"], fecha=informacion["fecha"],imagen=informacion["imagen"])
#                pedal.save()
#                return render(request,"Registro/index.html")
#      else:
#            pedalFormulario = PedalFormulario()

#      return render(request,"Registro/pedalFormulario.html", {"pedalFormulario" : pedalFormulario})


# def instrumento_formulario(request):

#      if request.method == "POST":

#           instFormulario = InstFormulario(request.POST,request.FILES)
#           print(instFormulario)

#           if instFormulario.is_valid():

#                informacion = instFormulario.cleaned_data
#                inst = Instrumento(nombre=informacion["nombre"], modelo=informacion["modelo"], tipo=informacion["tipo"], descripcion=informacion["descripcion"], precio=informacion["precio"], fecha=informacion["fecha"],imagen=informacion["imagen"])
#                inst.save()
#                return render(request,"Registro/index.html")
#      else:
#            instFormulario = InstFormulario()

#      return render(request,"Registro/instrumentoFormulario.html", {"instFormulario" : instFormulario})


# def portapuas_formulario(request):

#      if request.method == "POST":

#           portFormulario = PortaFormulario(request.POST, request.FILES)
#           print(portFormulario)

#           if  portFormulario.is_valid():

#                informacion =  portFormulario.cleaned_data
#                porta = Portapuas(nombre=informacion["nombre"], modelo=informacion["modelo"], tipo=informacion["tipo"], descripcion=informacion["descripcion"], precio=informacion["precio"], fecha=informacion["fecha"], imagen=informacion["imagen"])
#                porta.save()
#                return render(request,"Registro/index.html")
#      else:
#            portFormulario = PortaFormulario()

#      return render(request,"Registro/portapuasFormulario.html", {"portaFormulario" : portFormulario})






# def busquedaProducto(request):
#      return render(request,"Registro/busqueda-producto.html")

# def buscar(request):
#      if request.GET["producto"]:
#           producto = request.GET["producto"]
#           producto = Producto.objects.filter(producto_icontains=producto)
          