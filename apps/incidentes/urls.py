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
    path("incidentes/<str:incidente_id>/evidencia",views.agregar_evidencia,name="agregar_evidencia"),
    path("incidentes/<str:incidente_id>/accion",views.agregar_accion_incidente,name="agregar_accion_incidente"),
    path("incidentes/<str:incidente_id>/cerrar",views.cerrar_incidente_view,name="cerrar_incidente_view"),
    path("incidentes/<str:incidente_id>/reporte",views.ver_reporte_cierre,name="ver_reporte_cierre"),
    
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
]
    
