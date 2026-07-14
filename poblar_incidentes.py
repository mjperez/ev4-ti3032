# poblar_incidentes.py
import os
import django

# Configurar el entorno de Django para poder usar la BD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from apps.incidentes.models import Analista, Activo, Incidente, Evidencia, AccionEmbebida, ReporteCierre
from datetime import datetime, timezone

def poblar_bd():
    print("Limpiando la base de datos...")
    Analista.objects.delete()
    Activo.objects.delete()
    Incidente.objects.delete()
    
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
        especialidad ="incident response",
        telefono ="+987654321",
        horario ="9:00 - 18:00",
    ).save()

    analista_3 = Analista(
        nombre="Sam Peter", 
        email="sam@cybersec.cl", 
        rol="product owner",
        especialidad ="incident response",
        telefono ="+112233445",
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
        estado="en investigacion", 
        activo=activo_1,
        analista_asignado=analista_1,
        evidencias=[
            Evidencia(tipo="log", descripcion="Log auth.log del servidor", valor="Failed password for root from 192.168.1.100"),
            Evidencia(tipo="otro", descripcion="IP reportada en blacklist pública", valor="192.168.1.100")
        ],
        acciones_embebidas=[
            AccionEmbebida(
                titulo="Análisis inicial de logs",
                descripcion="Se procedió a revisar los logs del servidor confirmando 500 intentos fallidos en 2 minutos.",
                tipo="analisis",
                analista_id=str(analista_1.id)
            ),
            AccionEmbebida(
                titulo="Bloqueo temporal de IP",
                descripcion="Se configuró una regla temporal para bloquear la IP atacante en el WAF.",
                tipo="mitigacion",
                analista_id=str(analista_2.id)
            )
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

    # 4. Crear un Incidente Cerrado con Reporte
    incidente_3 = Incidente(
        titulo="Alerta de Malware Falsa Positiva",
        severidad="media",
        estado="cerrado",
        activo=activo_2,
        analista_asignado=analista_3,
        evidencias=[
            Evidencia(tipo="hash", descripcion="Hash del archivo marcado por antivirus", valor="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        ],
        acciones_embebidas=[
            AccionEmbebida(
                titulo="Verificación en VirusTotal",
                descripcion="Se comprobó el hash en múltiples motores de AV y resultó limpio (0/72).",
                tipo="analisis",
                analista_id=str(analista_3.id)
            )
        ],
        reporte_cierre=ReporteCierre(
            resumen="Se determinó que la alerta fue generada por una actualización legítima del sistema. No hubo riesgo real.",
            conclusiones="Afinar las reglas del antivirus para evitar bloqueos en esta ruta.",
            tiempo_resolucion_horas="0.50 horas",
            analista_id=str(analista_3.id)
        )
    ).save()

    print("¡Base de datos poblada con éxito!")
    print(f"- {Analista.objects.count()} Analistas")
    print(f"- {Activo.objects.count()} Activos")
    print(f"- {Incidente.objects.count()} Incidentes")

if __name__ == '__main__':
    poblar_bd()
