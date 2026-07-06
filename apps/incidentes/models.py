"""
Modelos de datos MongoEngine para el sistema de gestión de incidentes
de seguridad informática.

Utiliza MongoEngine como ODM (Object-Document Mapper) para interactuar
con MongoDB. Los modelos se definen en orden de dependencia:
    1. Evidencia (EmbeddedDocument) — sin colección propia
    2. Analista (Document) — colección 'analistas'
    3. Activo (Document) — colección 'activos'
    4. Incidente (Document) — colección 'incidentes'
    5. Accion (Document) — colección 'acciones'
    6. Reporte (Document) — colección 'reportes'

Decisiones de diseño:
    - Evidencia se embebe dentro de Incidente (ListField) porque siempre
      se accede en el contexto del incidente y no requiere consultas
      independientes. Esto reduce la cantidad de queries necesarias.
    - Accion y Reporte referencian a Incidente (ReferenceField) porque
      pueden consultarse de forma independiente y potencialmente
      requerirían paginación o filtrado propio.
"""

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

ROLES_ANALISTA = ["junior", "senior", "lead"]
"""Roles válidos para un analista de seguridad."""

ESPECIALIDADES_ANALISTA = ["forensic","malware","network","cloud","endpoint","incident response"]
"""Especialidades válidas para un analista de seguridad."""

TIPOS_ACTIVO = ["servidor", "endpoint", "red"]
"""Tipos de activos informáticos registrables."""

TIPOS_EVIDENCIA = ["log", "hash", "captura"]
"""Tipos de evidencia asociable a un incidente."""

NIVELES_SEVERIDAD = ["baja", "media", "alta", "critica"]
"""Niveles de severidad de un incidente."""

ESTADOS_INCIDENTE = ["abierto", "en investigacion", "cerrado"]
"""Estados del ciclo de vida de un incidente."""

TIPOS_ACCION = ["mitigacion", "analisis", "escalamiento"]
"""Tipos de acción ejecutable sobre un incidente."""


# ---------------------------------------------------------------------------
# 1. EmbeddedDocument: Evidencia
# ---------------------------------------------------------------------------

class Evidencia(EmbeddedDocument):
    """
    Evidencia asociada a un incidente de seguridad.

    Se almacena como documento embebido dentro de la lista
    ``Incidente.evidencias``. No posee colección propia en MongoDB.

    Attributes:
        tipo: Categoría de la evidencia (log, hash o captura).
        descripcion: Descripción textual de la evidencia.
        valor: Contenido o valor de la evidencia (ej: hash SHA-256,
               fragmento de log, nombre de archivo de captura).

    Example:
        >>> evidencia = Evidencia(
        ...     tipo="hash",
        ...     descripcion="Hash SHA-256 del archivo sospechoso",
        ...     valor="a1b2c3d4e5f6..."
        ... )
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


# ---------------------------------------------------------------------------
# 2. Document: Analista
# ---------------------------------------------------------------------------

class Analista(Document):
    """
    Analista de seguridad registrado en el sistema.

    Representa a un profesional responsable de investigar incidentes,
    ejecutar acciones de mitigación y emitir reportes de cierre.

    Attributes:
        nombre: Nombre completo del analista.
        email: Correo electrónico institucional (único).
        rol: Nivel jerárquico del analista (junior, senior o lead).
        telefono: Número de teléfono del analista.
        horario: Horario de trabajo del analista.
        especialidad: Especialidad del analista.

    Indexes:
        - ``email`` (único): evita duplicados y optimiza búsquedas.
        - ``rol``: optimiza filtrado por nivel jerárquico.

    Example:
        >>> analista = Analista(
        ...     nombre="María López",
        ...     email="mlopez@empresa.cl",
        ...     rol="senior",
        ...     telefono="+123456789",
        ...     horario="8:00 - 17:00",
        ...     especialidad="malware"
        ... )
        >>> analista.save()
    """

    nombre = StringField(
        required=True,
        max_length=100,
        help_text="Nombre completo del analista.",
    )
    email = EmailField(
        required=True,
        unique=True,
        help_text="Correo electrónico institucional (debe ser único).",
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


# ---------------------------------------------------------------------------
# 3. Document: Activo
# ---------------------------------------------------------------------------

class Activo(Document):
    """
    Activo informático registrado en el inventario del cliente.

    Representa un sistema, dispositivo o segmento de red que puede
    verse afectado por un incidente de seguridad.

    Attributes:
        nombre: Nombre identificador del activo (ej: 'SRV-WEB-01').
        tipo: Categoría del activo (servidor, endpoint o red).
        ip_address: Dirección IP asociada al activo (opcional).
        descripcion: Descripción adicional del activo (opcional).

    Indexes:
        - ``tipo``: optimiza filtrado por categoría de activo.
        - ``nombre``: optimiza búsquedas por nombre.

    Example:
        >>> activo = Activo(
        ...     nombre="SRV-WEB-01",
        ...     tipo="servidor",
        ...     ip_address="192.168.1.10",
        ...     descripcion="Servidor web de producción"
        ... )
        >>> activo.save()
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


# ---------------------------------------------------------------------------
# 4. Document: Incidente
# ---------------------------------------------------------------------------

class Incidente(Document):
    """
    Incidente de seguridad informática.

    Documento principal del sistema. Cada incidente se asocia a un activo
    afectado y a un analista responsable. Las evidencias se almacenan como
    documentos embebidos (ListField de EmbeddedDocumentField) para
    consolidar toda la información en un único punto de acceso.

    Attributes:
        titulo: Título descriptivo del incidente.
        severidad: Nivel de severidad (baja, media, alta, critica).
        estado: Estado del ciclo de vida (abierto, en_investigacion, cerrado).
        fecha_reporte: Fecha y hora del registro (default: ahora UTC).
        activo: Referencia al activo afectado.
        analista_asignado: Referencia al analista responsable.
        evidencias: Lista de evidencias embebidas.

    Indexes:
        - ``severidad``: optimiza filtrado por nivel de severidad.
        - ``estado``: optimiza filtrado por estado del incidente.
        - ``fecha_reporte`` (desc): optimiza ordenamiento cronológico.

    Example:
        >>> incidente = Incidente(
        ...     titulo="Acceso no autorizado a SRV-WEB-01",
        ...     severidad="alta",
        ...     estado="abierto",
        ...     activo=activo_obj,
        ...     analista_asignado=analista_obj,
        ...     evidencias=[
        ...         Evidencia(tipo="log", descripcion="Log de acceso SSH",
        ...                   valor="Failed password for root from 10.0.0.5")
        ...     ]
        ... )
        >>> incidente.save()
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


# ---------------------------------------------------------------------------
# 5. Document: Accion
# ---------------------------------------------------------------------------

class Accion(Document):
    """
    Acción tomada sobre un incidente de seguridad.

    Registra las intervenciones realizadas por los analistas durante
    el ciclo de vida de un incidente (mitigación, análisis, escalamiento).

    Attributes:
        incidente: Referencia al incidente sobre el que se actúa.
        analista: Referencia al analista que ejecuta la acción.
        descripcion: Descripción detallada de la acción realizada.
        tipo: Categoría de la acción (mitigacion, analisis, escalamiento).
        fecha: Fecha y hora de la acción (default: ahora UTC).

    Indexes:
        - ``incidente``: optimiza listado de acciones por incidente.
        - ``fecha`` (desc): optimiza ordenamiento cronológico.

    Example:
        >>> accion = Accion(
        ...     incidente=incidente_obj,
        ...     analista=analista_obj,
        ...     descripcion="Se bloqueó la IP de origen en el firewall",
        ...     tipo="mitigacion"
        ... )
        >>> accion.save()
    """

    incidente = ReferenceField(
        Incidente,
        required=True,
        help_text="Incidente sobre el cual se ejecutó la acción.",
    )
    analista = ReferenceField(
        Analista,
        required=True,
        help_text="Analista que ejecutó la acción.",
    )
    titulo = StringField(
        required=True,
        help_text="Titulo de la acción.",
    )
    descripcion = StringField(
        required=True,
        max_length=1000,
        help_text="Descripción detallada de la acción realizada.",
    )
    tipo = StringField(
        choices=TIPOS_ACCION,
        required=True,
        help_text="Categoría: mitigacion, analisis o escalamiento.",
    )
    fecha = DateTimeField(
        default=lambda: datetime.now(timezone.utc),
        help_text="Fecha y hora en que se ejecutó la acción (UTC).",
    )

    meta = {
        "collection": "acciones",
        "indexes": [
            "incidente",
            "-fecha",
        ],
        "ordering": ["-fecha"],
    }

    def __str__(self):
        return f"[{self.tipo}] {self.descripcion[:60]}"


# ---------------------------------------------------------------------------
# 6. Document: Reporte
# ---------------------------------------------------------------------------

class Reporte(Document):
    """
    Reporte de cierre de un incidente de seguridad.

    Se genera una vez que un incidente se resuelve y pasa al estado
    'cerrado'. Consolida el resumen de hallazgos y las conclusiones
    del análisis realizado.

    Attributes:
        incidente: Referencia al incidente reportado (único).
        analista: Referencia al analista que emite el reporte.
        resumen: Resumen ejecutivo de los hallazgos.
        conclusiones: Conclusiones y recomendaciones (opcional).
        fecha_emision: Fecha de emisión del reporte (default: ahora UTC).

    Indexes:
        - ``incidente`` (único): un incidente solo puede tener un reporte.
        - ``fecha_emision`` (desc): optimiza ordenamiento cronológico.

    Example:
        >>> reporte = Reporte(
        ...     incidente=incidente_cerrado,
        ...     analista=analista_obj,
        ...     resumen="Se identificó acceso no autorizado vía SSH...",
        ...     conclusiones="Se recomienda habilitar MFA en todos los servidores."
        ... )
        >>> reporte.save()
    """

    incidente = ReferenceField(
        Incidente,
        required=True,
        unique=True,
        help_text="Incidente al que pertenece este reporte de cierre.",
    )
    analista = ReferenceField(
        Analista,
        required=True,
        help_text="Analista que emite el reporte.",
    )
    resumen = StringField(
        required=True,
        max_length=2000,
        help_text="Resumen ejecutivo de los hallazgos del incidente.",
    )
    conclusiones = StringField(
        max_length=2000,
        help_text="Conclusiones y recomendaciones finales.",
    )
    fecha_emision = DateTimeField(
        default=lambda: datetime.now(timezone.utc),
        help_text="Fecha y hora de emisión del reporte (UTC).",
    )

    meta = {
        "collection": "reportes",
        "indexes": [
            {"fields": ["incidente"], "unique": True},
            "-fecha_emision",
        ],
        "ordering": ["-fecha_emision"],
    }

    def __str__(self):
        return f"Reporte: {self.incidente.titulo}"