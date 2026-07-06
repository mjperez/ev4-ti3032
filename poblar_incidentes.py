# poblar_incidentes.py
import os
import django

# Configurar el entorno de Django para poder usar la BD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from apps.incidentes.models import Analista, Activo, Incidente, Evidencia, Accion

def poblar_bd():
    print("Limpiando la base de datos...")
    Analista.objects.delete()
    Activo.objects.delete()
    Incidente.objects.delete()
    Accion.objects.delete()
    
    print("Creando datos de prueba...")
    
    # 1. Crear analistas
    analista_1 = Analista(
        nombre="John Hacker", 
        email="john@ciberseguridad.cl", 
        rol="senior",
        especialidad ="forensic",
        telefono ="+123456789",
        horario ="8:00 - 17:00",
    ).save()

    analista_2 = Analista(
        nombre="Alice Defender", 
        email="alice@ciberseguridad.cl", 
        rol="lead",
        especialidad ="incident response", # Actualizado a la opción con espacio
        telefono ="+987654321",
        horario ="9:00 - 18:00",
    ).save()

    # 2. Crear activos
    activo_1 = Activo(
        nombre="SRV-WEB-01", 
        tipo="servidor", 
        ip_address="10.0.0.5", 
        descripcion="Servidor web de producción principal"
    ).save()

    activo_2 = Activo(
        nombre="FW-CORE-01", 
        tipo="red", 
        ip_address="10.0.0.1", 
        descripcion="Firewall perimetral central"
    ).save()

    # 3. Crear Incidentes
    incidente_1 = Incidente(
        titulo="Intento de acceso fuerza bruta SSH",
        severidad="alta",
        estado="en investigacion", # Actualizado a la opción con espacio
        activo=activo_1,
        analista_asignado=analista_1,
        evidencias=[
            Evidencia(tipo="log", descripcion="Log auth.log del servidor", valor="Failed password for root from 192.168.1.100")
        ]
    ).save()

    incidente_2 = Incidente(
        titulo="Caída de tráfico anómalo en firewall",
        severidad="critica",
        estado="abierto",
        activo=activo_2,
        analista_asignado=analista_2,
        evidencias=[]
    ).save()

    # 4. Crear Acciones
    Accion(
        titulo="Análisis inicial de logs", # Nuevo campo que agregaste al modelo!
        descripcion="Se procedió a revisar los logs del servidor confirmando 500 intentos fallidos en 2 minutos.",
        tipo="analisis",
        incidente=incidente_1,
        analista=analista_1
    ).save()

    Accion(
        titulo="Bloqueo temporal de IP", # Nuevo campo
        descripcion="Se configuró una regla temporal para bloquear la IP atacante en el WAF.",
        tipo="mitigacion",
        incidente=incidente_1,
        analista=analista_2
    ).save()

    print("¡Base de datos poblada con éxito! 🚀")
    print(f"- {Analista.objects.count()} Analistas")
    print(f"- {Activo.objects.count()} Activos")
    print(f"- {Incidente.objects.count()} Incidentes")
    print(f"- {Accion.objects.count()} Acciones")

if __name__ == '__main__':
    poblar_bd()