from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Amp, Pedal, Instrumento, Portapuas
from django.urls import reverse_lazy



# Comienza Amp
class CrearAmp(LoginRequiredMixin, CreateView):
    model = Amp
    template_name = "Registro/ampFormulario.html"
    success_url= reverse_lazy("amp")
    fields =["nombre", "modelo", "tipo", "descripcion", "precio", "fecha", "imagen"]
 

class AmpListView(LoginRequiredMixin, ListView):
    model = Amp
    template_name = 'Registro/amp.html'
    context_object_name = 'amps'
    
class AmpDetalle(LoginRequiredMixin, DetailView):
    model = Amp
    template_name = "Registro/detalleamp.html"
    context_object_name = 'ampsdetail'

class AmpEditar(LoginRequiredMixin, UpdateView):
    model = Amp
    success_url = reverse_lazy("amp")
    fields = ["nombre", "modelo", "tipo", "descripcion", "precio", "fecha", "imagen"]
    template_name = "Registro/updateamp.html"

    

class Ampborrar(LoginRequiredMixin, DeleteView):
    model = Amp
    success_url = reverse_lazy("amp")
    template_name = 'Registro/borraramp.html'



# Comienza pedal
class PedalListView(LoginRequiredMixin, ListView):
    model = Pedal
    template_name = 'Registro/pedal.html'
    context_object_name = 'pedals'

class CrearPedal(LoginRequiredMixin, CreateView):
    model = Pedal
    template_name = "Registro/pedalFormulario.html"
    success_url= reverse_lazy("pedal")
    fields =["nombre", "modelo", "tipo", "descripcion", "precio", "fecha", "imagen"]

class PedalDetalle(LoginRequiredMixin, DetailView):
    model = Pedal
    template_name = "Registro/detallePedal.html"
    context_object_name = 'pedaldetail'

class PedalEditar(LoginRequiredMixin, UpdateView):
    model = Pedal
    success_url = reverse_lazy("pedal")
    fields = ["nombre", "modelo", "tipo", "descripcion", "precio", "fecha", "imagen"]
    template_name = "Registro/updatepedal.html"

class Pedalborrar(LoginRequiredMixin, DeleteView):
    model = Pedal
    success_url = reverse_lazy("pedal")
    template_name = 'Registro/borrarpedal.html'
 
#  Comienza Instrumento
class InstruListView(LoginRequiredMixin, ListView):
    model = Instrumento
    template_name = 'Registro/instrumento.html'
    context_object_name = 'instrumentos'

class CrearInstrumento(LoginRequiredMixin, CreateView):
    model = Instrumento
    template_name = "Registro/instrumentoFormulario.html"
    success_url= reverse_lazy("instrumento")
    fields =["nombre", "modelo", "tipo", "descripcion", "precio", "fecha", "imagen"]

class InstrumentoDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    template_name = "Registro/detalleIntrumento.html"
    context_object_name = 'instdetail'

class InstrumentoEditar(LoginRequiredMixin, UpdateView):
    model = Instrumento
    success_url = reverse_lazy("instrumento")
    fields = ["nombre", "modelo", "tipo", "descripcion", "precio", "fecha", "imagen"]
    template_name = "Registro/updateinst.html"

class Instrumentoborrar(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy("instrumento")
    template_name = 'Registro/borrarinstrumento.html'

# Comienza Portapuas 
 
class PortaListView(LoginRequiredMixin, ListView):
    model = Portapuas
    template_name = 'Registro/portapuas.html'
    context_object_name = 'portas'

class CrearPortapuas(LoginRequiredMixin, CreateView):
    model = Portapuas
    template_name = "Registro/portapuasFormulario.html"
    success_url= reverse_lazy("porta")
    fields =["nombre", "modelo", "tipo", "descripcion", "precio", "fecha", "imagen"]

class PortaDetalle(LoginRequiredMixin, DetailView):
    model = Portapuas
    template_name = "Registro/detallePorta.html"
    context_object_name = 'portadetail'

class PortaEditar(LoginRequiredMixin, UpdateView):
    model = Portapuas
    success_url = reverse_lazy("porta")
    fields = ["nombre", "modelo", "tipo", "descripcion", "precio", "fecha", "imagen"]
    template_name = "Registro/updateporta.html"

class Portaborrar(LoginRequiredMixin, DeleteView):
    model = Portapuas
    success_url = reverse_lazy("porta")
    template_name = 'Registro/borrarporta.html'
