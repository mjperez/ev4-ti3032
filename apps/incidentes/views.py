from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Incidente, Activo, Analista, Accion, ESPECIALIDADES_ANALISTA, ROLES_ANALISTA, TIPOS_EVIDENCIA, NIVELES_SEVERIDAD, ESTADOS_INCIDENTE, TIPOS_ACCION, TIPOS_ACTIVO
from datetime import datetime

def index(request):
    total_incidentes = Incidente.objects.count()
    incidentes_abiertos = Incidente.objects.filter(estado="abierto").count()
    total_activos = Activo.objects.count()
    total_analistas = Analista.objects.count()
    context = {
        "total_incidentes": total_incidentes,
        "incidentes_abiertos": incidentes_abiertos,
        "total_activos": total_activos,
        "total_analistas": total_analistas,
    }
    return render(request, 'index.html', context)

# Incidentes
def lista_incidentes(request):
    estado = request.GET.get('estado')
    if estado:
        incidentes = Incidente.objects.filter(estado=estado)
    else:
        incidentes = Incidente.objects.all()
    return render(request, 'lista_incidentes.html', {'incidentes': incidentes, 'estado_actual': estado})

def detalle_incidente(request, incidente_id):
    incidente = Incidente.objects.get(id=incidente_id)
    return render(request, 'detalle_incidente.html',{'incidente':incidente})

def crear_incidente(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        estado = request.POST.get("estado")
        prioridad = request.POST.get("prioridad")
        fecha_str = request.POST.get("fecha")
        activo_id = request.POST.get("activo")
        analista_id = request.POST.get("analista_asignado")

        analista_obj = None
        activo_obj = None

        if analista_id:
            try:
                analista_obj = Analista.objects.get(id=analista_id)
            except Analista.DoesNotExist:
                pass
        
        if activo_id:
            try:
                activo_obj = Activo.objects.get(id=activo_id)
            except Activo.DoesNotExist:
                pass

        fecha = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M")
        nuevo_incidente = Incidente(
            titulo = titulo,
            descripcion = descripcion,
            estado = estado,
            prioridad = prioridad,
            fecha = fecha,
            activo = activo_obj,
            analista_asignado = analista_obj
        )

        try:
            nuevo_incidente.save()
            return redirect("lista_incidentes")
        except Exception as e:
            return render(request, "crear_incidente.html",{
        'tipos_evidencia' : TIPOS_EVIDENCIA,
        'niveles_severidad' : NIVELES_SEVERIDAD,
        'estados_incidente' : ESTADOS_INCIDENTE
    })

    return render(request, "crear_incidente.html")  

def editar_incidente(request, incidente_id):
    incidente = Incidente.objects.get(id=incidente_id)
    analistas = Analista.objects.all()
    activos = Activo.objects.all()
    
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        estado = request.POST.get("estado")
        severidad = request.POST.get("severidad")
        fecha_str = request.POST.get("fecha_reporte")
        activo_id = request.POST.get("activo")
        analista_id = request.POST.get("analista_asignado")

        analista_obj = None
        activo_obj = None

        if analista_id:
            try:
                analista_obj = Analista.objects.get(id=analista_id)
            except Analista.DoesNotExist:
                pass
        
        if activo_id:
            try:
                activo_obj = Activo.objects.get(id=activo_id)
            except Activo.DoesNotExist:
                pass

        fecha = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M")

        incidente.titulo = titulo
        incidente.descripcion = descripcion
        incidente.estado = estado
        incidente.fecha = fecha
        incidente.activo = activo_obj
        incidente.analista_asignado = analista_obj

        try:
            incidente.save()
            return redirect("lista_incidentes")
        except Exception as e:
            return render(request, "editar_incidente.html",{
                'incidente':incidente, 
                'severidades':NIVELES_SEVERIDAD, 
                'estados': ESTADOS_INCIDENTE,
                'analistas':analistas,
                'activos':activos
                })
    #Petición es GET
    return render(request, "editar_incidente.html",{'incidente':incidente, 'severidades':NIVELES_SEVERIDAD, 'estados': ESTADOS_INCIDENTE, 'analistas':analistas, 'activos':activos})

def eliminar_incidente(request, incidente_id):
    incidente = Incidente.objects.get(id=incidente_id)
    if request.method == 'POST':
        incidente.delete()
        messages.success(request, f'El incidente "{incidente.titulo}" fue eliminado exitosamente.')
        return redirect("lista_incidentes")
    
    return render(request, 'eliminar_incidente.html', {'incidente' : incidente})

# Activos
def lista_activos(request):
    activos = Activo.objects.all()
    return render(request, 'lista_activos.html', {'activos' : activos})

def detalle_activo(request, activo_id):
    activo = Activo.objects.get(id=activo_id)
    return render(request, 'detalle_activo.html',{'activo':activo})

def crear_activo(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        tipo = request.POST.get("tipo")
        categoria = request.POST.get("categoria")
        ip_address = request.POST.get("ip_address")

        nuevo_activo = Activo(
            nombre = nombre,
            tipo = tipo,
            categoria = categoria,
            ip_address = ip_address
        )

        try:
            nuevo_activo.save()
            return redirect("lista_activos")
        except Exception as e:
            return render(request, 'crear_activo.html', {'error' : str(e)})

    return render(request, "crear_activo.html")

def editar_activo(request, activo_id):
    pass

def eliminar_activo(request, activo_id):
    pass

# Analistas
def lista_analistas(request):
    analistas = Analista.objects.all()
    return render(request, 'lista_analistas.html', {'analistas' : analistas})

def detalle_analista(request, analista_id):
    analista = Analista.objects.get(id=analista_id)
    return render(request, 'detalle_analista.html',{'analista':analista})

def crear_analista(request):
    if request.method == 'POST':
        # datos del form HTML (get("name_de_la_form"))
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        rol = request.POST.get("rol")
        especialidad = request.POST.get("especialidad")
        telefono = request.POST.get("telefono")
        horario = request.POST.get("horario")

        # creacion del objeto
        nuevo_analista = Analista(
            nombre = nombre, 
            email = email,
            rol = rol,
            telefono = telefono,
            horario = horario,
            especialidad = especialidad
        )

        try:
            nuevo_analista.save() 
            return redirect("lista_analistas")
        except Exception as e:
            return render(request, 'crear_analista.html', {'error' : str(e)})
    # Si la petición es GET
    return render(request, "crear_analista.html",{
        'especialidades' : ESPECIALIDADES_ANALISTA,
        'roles' : ROLES_ANALISTA
    })

def editar_analista(request, analista_id):
    pass

def eliminar_analista(request, analista_id):
    pass

# Acciones
def lista_acciones(request):
    acciones = Accion.objects.all()
    return render(request, 'lista_acciones.html', {'acciones' : acciones})

def detalle_accion(request, accion_id):
    accion = Accion.objects.get(id=accion_id)
    return render(request, 'detalle_accion.html',{'accion':accion})

def crear_accion(request):
    if request.method == 'POST':
        descripcion = request.POST.get("descripcion")
        tipo = request.POST.get("tipo")
        fecha_str = request.POST.get("fecha")
        incidente = request.POST.get("incidente")
        analista = request.POST.get("analista")

        try:
            incidente = Incidente.objects.get(id=incidente)
            analista = Analista.objects.get(id=analista)
            fecha = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M")

            nueva_accion = Accion(
                descripcion = descripcion,
                tipo = tipo,
                fecha = fecha,
                incidente = incidente,
                analista = analista
            )
            nueva_accion.save()
            return redirect("lista_acciones")
        except Exception as e:
            return render(request, 'crear_accion.html', {
                'error': str(e),
                'tipos_accion': TIPOS_ACCION,
                'incidentes': Incidente.objects.all(),
                'analistas': Analista.objects.all(),
                'hoy': datetime.now().strftime("%Y-%m-%dT%H:%M")
            })

    return render(request, "crear_accion.html",{
        'tipos_accion' : TIPOS_ACCION,
        'incidentes': Incidente.objects.all(),
        'analistas': Analista.objects.all(),
        'hoy': datetime.now().strftime("%Y-%m-%dT%H:%M")
        })

def editar_accion(request, accion_id):
    pass

def eliminar_accion(request, accion_id):
    pass    