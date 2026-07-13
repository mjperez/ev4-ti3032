from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Incidente, Activo, Analista, Evidencia, AccionEmbebida, ReporteCierre, ESPECIALIDADES_ANALISTA, ROLES_ANALISTA, TIPOS_EVIDENCIA, NIVELES_SEVERIDAD, ESTADOS_INCIDENTE, TIPOS_ACCION, TIPOS_ACTIVO
from datetime import datetime, timezone

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
        estado = request.POST.get("estado")
        severidad = request.POST.get("severidad")
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
            estado = estado,
            severidad = severidad,
            fecha_reporte = fecha,
            activo = activo_obj,
            analista_asignado = analista_obj
        )

        try:
            nuevo_incidente.save()
            return redirect("lista_incidentes")
        except Exception as e:
            return render(request, "crear_incidente.html",{
                'error': str(e),
                'severidades' : NIVELES_SEVERIDAD,
                'estados' : ESTADOS_INCIDENTE,
                'activos': Activo.objects.all(),
                'analistas': Analista.objects.all()
            })

    return render(request, "crear_incidente.html", {
        'severidades' : NIVELES_SEVERIDAD,
        'estados' : ESTADOS_INCIDENTE,
        'activos': Activo.objects.all(),
        'analistas': Analista.objects.all()
    })  

def editar_incidente(request, incidente_id):
    incidente = Incidente.objects.get(id=incidente_id)
    analistas = Analista.objects.all()
    activos = Activo.objects.all()
    
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        estado = request.POST.get("estado")
        severidad = request.POST.get("severidad")
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

        incidente.titulo = titulo
        incidente.estado = estado
        incidente.severidad = severidad
        incidente.fecha_reporte = fecha
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
        ip_address = request.POST.get("ip_address")
        descripcion = request.POST.get("descripcion")

        if ip_address:
            existente = Activo.objects.filter(ip_address=ip_address).first()
            if existente:
                return render(request, 'crear_activo.html', {'error': 'La dirección IP ingresada ya está registrada en otro activo.', 'tipos_activo': TIPOS_ACTIVO})

        nuevo_activo = Activo(
            nombre = nombre,
            tipo = tipo,
            ip_address = ip_address,
            descripcion = descripcion
        )

        try:
            nuevo_activo.save()
            return redirect("lista_activos")
        except Exception as e:
            return render(request, 'crear_activo.html', {'error' : str(e), 'tipos_activo': TIPOS_ACTIVO})

    return render(request, "crear_activo.html", {'tipos_activo': TIPOS_ACTIVO})

def editar_activo(request, activo_id):
    activo = Activo.objects.get(id=activo_id)
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        tipo = request.POST.get("tipo")
        ip_address = request.POST.get("ip_address")
        descripcion = request.POST.get("descripcion")

        if ip_address and ip_address != activo.ip_address:
            existente = Activo.objects.filter(ip_address=ip_address).first()
            if existente:
                return render(request, 'editar_activo.html', {'error': 'La dirección IP ingresada ya está registrada en otro activo.', 'activo': activo, 'tipos_activo': TIPOS_ACTIVO})

        activo.nombre = nombre
        activo.tipo = tipo
        activo.ip_address = ip_address
        activo.descripcion = descripcion

        try:
            activo.save()
            messages.success(request, f'El activo "{activo.nombre}" fue actualizado exitosamente.')
            return redirect("detalle_activo", activo_id=activo.id)
        except Exception as e:
            return render(request, 'editar_activo.html', {'error' : str(e), 'activo': activo, 'tipos_activo': TIPOS_ACTIVO})
            
    return render(request, 'editar_activo.html', {'activo': activo, 'tipos_activo': TIPOS_ACTIVO})

def eliminar_activo(request, activo_id):
    activo = Activo.objects.get(id=activo_id)
    if request.method == 'POST':
        # Check if there are incidents associated with this active?
        incidentes_asociados = Incidente.objects.filter(activo=activo).count()
        if incidentes_asociados > 0:
            messages.error(request, f'No se puede eliminar el activo "{activo.nombre}" porque tiene incidentes asociados.')
            return redirect('lista_activos')
        
        activo.delete()
        messages.success(request, f'El activo "{activo.nombre}" fue eliminado exitosamente.')
        return redirect("lista_activos")
    
    return render(request, 'eliminar_activo.html', {'activo' : activo})

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
        
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return render(request, 'crear_analista.html', {'error': 'Formato de email inválido', 'especialidades' : ESPECIALIDADES_ANALISTA, 'roles' : ROLES_ANALISTA})
        
        if Analista.objects.filter(email=email).first():
            return render(request, 'crear_analista.html', {'error': 'El email ya está registrado', 'especialidades' : ESPECIALIDADES_ANALISTA, 'roles' : ROLES_ANALISTA})

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
            return render(request, 'crear_analista.html', {'error' : str(e), 'especialidades' : ESPECIALIDADES_ANALISTA, 'roles' : ROLES_ANALISTA})
    # Si la petición es GET
    return render(request, "crear_analista.html",{
        'especialidades' : ESPECIALIDADES_ANALISTA,
        'roles' : ROLES_ANALISTA
    })

def editar_analista(request, analista_id):
    analista = Analista.objects.get(id=analista_id)
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        rol = request.POST.get("rol")
        especialidad = request.POST.get("especialidad")
        telefono = request.POST.get("telefono")
        horario = request.POST.get("horario")
        
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return render(request, 'editar_analista.html', {'error': 'Formato de email inválido', 'analista': analista, 'especialidades': ESPECIALIDADES_ANALISTA, 'roles': ROLES_ANALISTA})
        
        if email != analista.email and Analista.objects.filter(email=email).first():
            return render(request, 'editar_analista.html', {'error': 'El email ya está registrado por otro analista', 'analista': analista, 'especialidades': ESPECIALIDADES_ANALISTA, 'roles': ROLES_ANALISTA})

        analista.nombre = nombre
        analista.email = email
        analista.rol = rol
        analista.especialidad = especialidad
        analista.telefono = telefono
        analista.horario = horario

        try:
            analista.save()
            messages.success(request, f'El analista "{analista.nombre}" fue actualizado exitosamente.')
            return redirect("detalle_analista", analista_id=analista.id)
        except Exception as e:
            return render(request, 'editar_analista.html', {'error': str(e), 'analista': analista, 'especialidades': ESPECIALIDADES_ANALISTA, 'roles': ROLES_ANALISTA})
            
    return render(request, 'editar_analista.html', {'analista': analista, 'especialidades': ESPECIALIDADES_ANALISTA, 'roles': ROLES_ANALISTA})

def eliminar_analista(request, analista_id):
    analista = Analista.objects.get(id=analista_id)
    if request.method == 'POST':
        # Check if there are incidents associated with this analyst?
        incidentes_asociados = Incidente.objects.filter(analista_asignado=analista).count()
        if incidentes_asociados > 0:
            messages.error(request, f'No se puede eliminar el analista "{analista.nombre}" porque tiene incidentes asignados.')
            return redirect('lista_analistas')
            
        analista.delete()
        messages.success(request, f'El analista "{analista.nombre}" fue eliminado exitosamente.')
        return redirect("lista_analistas")
        
    return render(request, 'eliminar_analista.html', {'analista': analista})



# --- Vistas para componentes embebidos de Incidentes ---

def agregar_evidencia(request, incidente_id):
    incidente = Incidente.objects.get(id=incidente_id)
    if request.method == 'POST':
        tipo = request.POST.get("tipo")
        descripcion = request.POST.get("descripcion")
        valor = request.POST.get("valor")
        
        evidencia = Evidencia(
            tipo=tipo,
            descripcion=descripcion,
            valor=valor
        )
        
        try:
            incidente.evidencias.append(evidencia)
            incidente.save()
            messages.success(request, "Evidencia añadida exitosamente.")
            return redirect("detalle_incidente", incidente_id=incidente.id)
        except Exception as e:
            return render(request, 'agregar_evidencia.html', {'error': str(e), 'incidente': incidente, 'tipos_evidencia': TIPOS_EVIDENCIA})
            
    return render(request, 'agregar_evidencia.html', {'incidente': incidente, 'tipos_evidencia': TIPOS_EVIDENCIA})

def agregar_accion_incidente(request, incidente_id):
    incidente = Incidente.objects.get(id=incidente_id)
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        tipo = request.POST.get("tipo")
        analista_id = request.POST.get("analista")
        
        try:
            analista_obj = Analista.objects.get(id=analista_id)
            accion_embebida = AccionEmbebida(
                titulo=titulo,
                descripcion=descripcion,
                tipo=tipo,
                fecha=datetime.now(timezone.utc),
                analista_id=str(analista_obj.id)
            )
            incidente.acciones_embebidas.append(accion_embebida)
            incidente.save()
            
            messages.success(request, "Acción registrada exitosamente.")
            return redirect("detalle_incidente", incidente_id=incidente.id)
        except Exception as e:
            return render(request, 'registrar_accion.html', {'error': str(e), 'incidente': incidente, 'tipos_accion': TIPOS_ACCION, 'analistas': Analista.objects.all()})
            
    return render(request, 'registrar_accion.html', {'incidente': incidente, 'tipos_accion': TIPOS_ACCION, 'analistas': Analista.objects.all()})

def cerrar_incidente_view(request, incidente_id):
    incidente = Incidente.objects.get(id=incidente_id)
    if not incidente.acciones_embebidas:
        messages.error(request, "El incidente no tiene acciones registradas, no se puede generar reporte de cierre.")
        return redirect("detalle_incidente", incidente_id=incidente.id)

    if request.method == 'POST':
        resumen = request.POST.get("resumen")
        conclusiones = request.POST.get("conclusiones")
        analista_id = request.POST.get("analista")
        
        try:
            incidente.cerrar_incidente(resumen=resumen, conclusiones=conclusiones, analista_id=analista_id)
            messages.success(request, "Reporte de cierre generado y guardado exitosamente.")
            return redirect("ver_reporte_cierre", incidente_id=incidente.id)
        except Exception as e:
            return render(request, 'cerrar_incidente.html', {'error': str(e), 'incidente': incidente, 'analistas': Analista.objects.all()})
            
    return render(request, 'cerrar_incidente.html', {'incidente': incidente, 'analistas': Analista.objects.all()})

def ver_reporte_cierre(request, incidente_id):
    incidente = Incidente.objects.get(id=incidente_id)
    analista_obj = None
    if incidente.reporte_cierre and incidente.reporte_cierre.analista_id != "Desconocido":
        try:
            analista_obj = Analista.objects.get(id=incidente.reporte_cierre.analista_id)
        except:
            pass
            
    return render(request, 'reporte_cierre.html', {'incidente': incidente, 'analista': analista_obj})