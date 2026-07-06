from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    
    # Incidentes
    path("incidentes/",views.lista_incidentes, name="lista_incidentes"),
    path("incidentes/<str:incidente_id>",views.detalle_incidente,name="detalle_incidente"),
    path("crear-incidente/",views.crear_incidente,name="crear_incidente"),
    path("editar-incidente/<str:incidente_id>",views.editar_incidente,name="editar_incidente"),
    path("eliminar-incidente/<str:incidente_id>",views.eliminar_incidente,name="eliminar_incidente"),
    
    # Activos
    path("activos/",views.lista_activos,name="lista_activos"),
    path("activos/<str:activo_id>",views.detalle_activo,name="detalle_activo"),
    path("crear-activo/",views.crear_activo,name="crear_activo"),
    path("editar-activo/<str:activo_id>",views.editar_activo,name="editar_activo"),
    path("eliminar-activo/<str:activo_id>",views.eliminar_activo,name="eliminar_activo"),
    
    # Analistas
    path("analistas/",views.lista_analistas,name="lista_analistas"),
    path("analistas/<str:analista_id>",views.detalle_analista,name="detalle_analista"),
    path("crear-analista/",views.crear_analista,name="crear_analista"),
    path("editar-analista/<str:analista_id>",views.editar_analista,name="editar_analista"),
    path("eliminar-analista/<str:analista_id>",views.eliminar_analista,name="eliminar_analista"),
    
    # Acciones
    path("acciones/",views.lista_acciones,name="lista_acciones"),
    path("acciones/<str:accion_id>",views.detalle_accion,name="detalle_accion"),
    path("crear-accion/",views.crear_accion,name="crear_accion"),
    path("editar-accion/<str:accion_id>",views.editar_accion,name="editar_accion"),
    path("eliminar-accion/<str:accion_id>",views.eliminar_accion,name="eliminar_accion")
]
