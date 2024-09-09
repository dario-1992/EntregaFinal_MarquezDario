from Registro import views, CBV
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include




urlpatterns = [
    #Inicio
    path('Inicio/', views.inicio, name = "inicio"),
    #Amp
    path('amp/', CBV.AmpListView.as_view(), name = "amp" ),
    path('amp-formulario/', CBV.CrearAmp.as_view(), name = "Amp_formulario"),
    path('editar-amp/<int:pk>', CBV.AmpEditar.as_view(), name = "editaramp"),
    path('detalle-amp/<int:pk>', CBV.AmpDetalle.as_view(), name = "detalleamp"),
    path('borraramp/<int:pk>',CBV.Ampborrar.as_view(), name='borraramp'),
    #Pedal
    path('pedal/', CBV.PedalListView.as_view(), name = "pedal" ),
    path('pedal-formulario/', CBV.CrearPedal.as_view(), name = "Pedal_formulario"),
    path('instrumento/', CBV.InstruListView.as_view(), name = "instrumento" ),
    path('editar-pedal/<int:pk>', CBV.PedalEditar.as_view(), name = "editarpedal"),
    path('detalle-pedal/<int:pk>', CBV.PedalDetalle.as_view(), name = "detallepedal"),
    path('borrarpedal/<int:pk>',CBV.Pedalborrar.as_view(), name='borrarpedal'),
    #Instrumento
    path('instrumento/', CBV.InstruListView.as_view(), name = "instrumento" ),
    path('inst-formulario/', CBV.CrearInstrumento.as_view(), name = "Inst_formulario"),
    path('editar-instrumento/<int:pk>', CBV.InstrumentoEditar.as_view(), name = "editarinstrumento"),
    path('detalle-instrumento/<int:pk>', CBV.InstrumentoDetalle.as_view(), name = "detalleinstrumento"),
    path('borrar-instrumento/<int:pk>',CBV.Instrumentoborrar.as_view(), name='borrarinstrumento'),
    #Portapuas
    path('portapuas/', CBV.PortaListView.as_view(), name = "porta" ),
    path('porta-formulario/', CBV.CrearPortapuas.as_view(), name = "Porta_formulario"),
    path('detalle-porta/<int:pk>', CBV.PortaDetalle.as_view(), name = "detalleporta"),
    path('editar-porta/<int:pk>', CBV.PortaEditar.as_view(), name = "editarporta"),
    path('borrarporta/<int:pk>',CBV.Portaborrar.as_view(), name='borrarporta'),
    #sobre mi 
    path('sobremi/',views.sobremi ,name='sobremi')
    
    
    # path('busqueda-producto/', views.busquedaProducto, name = "BusquedaProducto"),
    # path('buscar/', views.buscar)
   
]

