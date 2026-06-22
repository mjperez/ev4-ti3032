from datetime import datetime

from django.db import models
from mongoengine import (
    DateTimeField,
    Document,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    StringField,
)


# Create your models here.
class Incidente(Document):
    titulo            = StringField(required=True)
    severidad         = StringField(choices=["baja", "media", "alta", "critica"])
    estado            = StringField(choices=["abierto", "en_investigacion", "cerrado"])
    fecha_reporte     = DateTimeField(default=datetime.utcnow)
    activo            = ReferenceField(Activo)
    analista_asignado = ReferenceField(Analista)
    evidencias        = ListField(EmbeddedDocumentField(Evidencia))

    meta = {"collection": "incidentes"}