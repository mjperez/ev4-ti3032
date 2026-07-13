from datetime import datetime, timezone
from mongoengine import (
    DateTimeField,
    Document,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    StringField,
)

ROLES_ANALISTA = ["junior", "senior", "lead", "product owner"]
"""Roles válidos para un analista de seguridad."""

ESPECIALIDADES_ANALISTA = ["forensic","malware","network","cloud","endpoint","incident response"]
"""Especialidades válidas para un analista de seguridad."""

TIPOS_ACTIVO = ["servidor", "endpoint", "red"]
"""Tipos de activos informáticos registrables."""

TIPOS_EVIDENCIA = ["log", "hash", "captura", "otro"]
"""Tipos de evidencia asociable a un incidente."""

NIVELES_SEVERIDAD = ["baja", "media", "alta", "critica"]
"""Niveles de severidad de un incidente."""

ESTADOS_INCIDENTE = ["abierto", "en investigacion", "cerrado", "falso positivo"]
"""Estados del ciclo de vida de un incidente."""

TIPOS_ACCION = ["mitigacion", "analisis", "escalamiento"]
"""Tipos de acción ejecutable sobre un incidente."""

class Evidencia(EmbeddedDocument):
    """
    Evidencia asociada a un incidente de seguridad.

    Atributos:
        tipo: Categoría de la evidencia (log, hash o captura).
        descripcion: Descripción textual de la evidencia.
        valor: Contenido o valor de la evidencia (ej: hash SHA-256,
               fragmento de log, nombre de archivo de captura).
    """
    
    tipo = StringField(
        choices=TIPOS_EVIDENCIA,
        required=True,
        help_text="Categoría de la evidencia: log, hash o captura.",
    )
    descripcion = StringField(
        required=True,
        max_length=500,
        help_text="Descripción textual de la evidencia recopilada.",
    )
    valor = StringField(
        help_text="Contenido o dato concreto de la evidencia.",
    )

    def __str__(self):
        return f"[{self.tipo}] {self.descripcion[:60]}"

class Analista(Document):
    """
    Analista de seguridad registrado en el sistema, responsable de investigar incidentes,
    ejecutar acciones de mitigación y emitir reportes de cierre.

    Atributos:
        nombre: Nombre completo del analista.
        email: Correo electrónico institucional (único).
        rol: Nivel jerárquico del analista (junior, senior o lead).
        telefono: Número de teléfono del analista.
        horario: Horario de trabajo del analista.
        especialidad: Especialidad del analista.

    Indexes:
        - ``email`` (único): evita duplicados y optimiza búsquedas.
        - ``rol``: optimiza filtrado por nivel jerárquico.
    """

    nombre = StringField(
        required=True,
        max_length=100,
        help_text="Nombre completo del analista.",
    )
    email = EmailField(
        required=True,
        unique=True,
        help_text="Correo electrónico del analista (debe ser único).",
    )
    rol = StringField(
        choices=ROLES_ANALISTA,
        required=True,
        help_text="Nivel jerárquico: junior, senior o lead.",
    )
    especialidad = StringField(
        choices=ESPECIALIDADES_ANALISTA,
        required=True,
        help_text="Especialidad del analista, ej: malware, forensic.",
    )
    telefono = StringField(
        required=True,
        max_length=15,
        help_text="Número de teléfono del analista.",
    )
    horario = StringField(
        required=True,
        max_length=15,
        help_text="Horario de trabajo del analista.",
    )

    meta = {
        "collection": "analistas",
        "indexes": [
            {"fields": ["email"], "unique": True},
            "rol",
        ],
        "ordering": ["nombre"],
    }

    def __str__(self):
        return f"{self.nombre} ({self.rol})"


class Activo(Document):
    """
    Activo informático registrado en el inventario del cliente. Representa un sistema, dispositivo o segmento de red que puede
    verse afectado por un incidente de seguridad.

    Atributos:
        nombre: Nombre identificador del activo (ej: 'SRV-WEB-01').
        tipo: Categoría del activo (servidor, endpoint o red).
        ip_address: Dirección IP asociada al activo (opcional).
        descripcion: Descripción adicional del activo (opcional).

    Indexes:
        - ``tipo``: optimiza filtrado por categoría de activo.
        - ``nombre``: optimiza búsquedas por nombre.
    """

    nombre = StringField(
        required=True,
        max_length=150,
        help_text="Nombre identificador del activo.",
    )
    tipo = StringField(
        choices=TIPOS_ACTIVO,
        required=True,
        help_text="Categoría: servidor, endpoint o red.",
    )
    ip_address = StringField(
        max_length=45,
        help_text="Dirección IP del activo (IPv4 o IPv6).",
    )
    descripcion = StringField(
        max_length=500,
        help_text="Descripción adicional del activo.",
    )

    meta = {
        "collection": "activos",
        "indexes": [
            "tipo",
            "nombre",
        ],
        "ordering": ["nombre"],
    }

    def __str__(self):
        ip_info = f" ({self.ip_address})" if self.ip_address else ""
        return f"{self.nombre}{ip_info}"


class AccionEmbebida(EmbeddedDocument):
    """
    Acción embebida dentro de un incidente.
    """
    titulo = StringField(required=True, help_text="Titulo de la acción.")
    descripcion = StringField(required=True, max_length=1000, help_text="Descripción detallada de la acción realizada.")
    tipo = StringField(choices=TIPOS_ACCION, required=True, help_text="Categoría: mitigacion, analisis o escalamiento.")
    fecha = DateTimeField(default=lambda: datetime.now(timezone.utc), help_text="Fecha y hora en que se ejecutó la acción (UTC).")
    analista_id = StringField(required=True, help_text="ID del analista que ejecutó la acción (para auditoría).")

    def __str__(self):
        return f"[{self.tipo}] {self.descripcion[:60]}"

class ReporteCierre(EmbeddedDocument):
    """
    Reporte de cierre embebido indisolublemente asociado al incidente.
    """
    resumen = StringField(required=True, max_length=2000, help_text="Resumen ejecutivo de los hallazgos del incidente.")
    conclusiones = StringField(max_length=2000, help_text="Conclusiones y recomendaciones finales.")
    fecha_emision = DateTimeField(default=lambda: datetime.now(timezone.utc), help_text="Fecha y hora de emisión del reporte (UTC).")
    tiempo_resolucion_horas = StringField(help_text="Tiempo total de resolución calculado al momento del cierre.")
    analista_id = StringField(required=True, help_text="ID del analista que emite el reporte.")

    def __str__(self):
        return f"Reporte del {self.fecha_emision}"

class Incidente(Document):
    """
    Incidente de seguridad informática.

    Atributos:
        titulo: Título descriptivo del incidente.
        severidad: Nivel de severidad (baja, media, alta, critica).
        estado: Estado del ciclo de vida (abierto, en_investigacion, cerrado).
        fecha_reporte: Fecha y hora del registro (default: ahora UTC).
        activo: Referencia al activo afectado.
        analista_asignado: Referencia al analista responsable.
        evidencias: Lista de evidencias embebidas.

    Indices:
        - ``severidad``: optimiza filtrado por nivel de severidad.
        - ``estado``: optimiza filtrado por estado del incidente.
        - ``fecha_reporte`` (desc): optimiza ordenamiento cronológico.
    """

    titulo = StringField(
        required=True,
        max_length=200,
        help_text="Título descriptivo del incidente.",
    )
    severidad = StringField(
        choices=NIVELES_SEVERIDAD,
        required=True,
        help_text="Nivel de severidad: baja, media, alta o critica.",
    )
    estado = StringField(
        choices=ESTADOS_INCIDENTE,
        default="abierto",
        required=True,
        help_text="Estado actual: abierto, en_investigacion o cerrado.",
    )
    fecha_reporte = DateTimeField(
        default=lambda: datetime.now(timezone.utc),
        help_text="Fecha y hora de registro del incidente (UTC).",
    )
    activo = ReferenceField(
        Activo,
        required=True,
        help_text="Activo informático afectado por el incidente.",
    )
    analista_asignado = ReferenceField(
        Analista,
        help_text="Analista responsable de la investigación.",
    )
    evidencias = ListField(
        EmbeddedDocumentField(Evidencia),
        help_text="Lista de evidencias embebidas en el incidente.",
    )
    acciones_embebidas = ListField(
        EmbeddedDocumentField(AccionEmbebida),
        help_text="Lista de acciones embebidas en el incidente.",
    )
    reporte_cierre = EmbeddedDocumentField(
        ReporteCierre,
        help_text="Reporte de cierre embebido asociado al incidente.",
    )

    meta = {
        "collection": "incidentes",
        "indexes": [
            "severidad",
            "estado",
            "-fecha_reporte",
        ],
        "ordering": ["-fecha_reporte"],
    }

    def __str__(self):
        return f"[{self.severidad.upper()}] {self.titulo}"

    def cerrar_incidente(self, resumen, conclusiones=None, analista_id=None):
        """
        Cierra el incidente y genera automáticamente el reporte de cierre embebido.
        Calcula el tiempo de resolución en horas.
        """
        self.estado = "cerrado"
        tiempo_resolucion = ""
        if self.fecha_reporte:
            delta = datetime.now(timezone.utc) - self.fecha_reporte
            horas = delta.total_seconds() / 3600
            tiempo_resolucion = f"{horas:.2f} horas"
            
        self.reporte_cierre = ReporteCierre(
            resumen=resumen,
            conclusiones=conclusiones,
            tiempo_resolucion_horas=tiempo_resolucion,
            analista_id=str(analista_id) if analista_id else "Desconocido"
        )
        self.save()


