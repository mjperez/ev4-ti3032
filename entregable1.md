# Proyecto Tracker de Incidentes

## Levantamiento de Información

### Situación Actual
El cliente es una empresa de consultoría de ciberseguridad con sede en 
Santiago, Chile. La empresa gestiona incidentes de seguridad de forma 
manual, mediante plantillas Excel compartidas por correo electrónico. 
Esto genera problemas de trazabilidad, pérdida de información y 
dificultad en la asignación de analistas.

### Problemas Identificados
- No existe un registro centralizado de incidentes.
- Las evidencias se pierden o quedan dispersas.
- No hay seguimiento formal de las acciones tomadas por cada analista.
- No se generan reportes de cierre estandarizados.

### Necesidades Identificadas
- Registrar y clasificar incidentes de seguridad por severidad y estado.
- Asociar cada incidente a un activo afectado y a un analista responsable.
- Almacenar evidencias para cada incidente.
- Registrar acciones de mitigación para cada incidente.
- Emitir un reporte de cierre al resolver el incidente.

### Volúmenes de Datos Actuales y Proyectados

Basado en el contexto operativo del cliente (consultora mediana, 
operación en Santiago), se estiman los siguientes volúmenes:

| Entidad | Volumen inicial | Proyección 12 meses | Proyección 24 meses |
|---|---|---|---|
| Incidentes | ~30/mes | ~360 registros | ~720 registros |
| Evidencias | ~3 por incidente | ~1.080 documentos | ~2.160 documentos |
| Acciones de mitigación | ~4 por incidente | ~1.440 registros | ~2.880 registros |
| Analistas | 5–10 usuarios | Sin variación significativa | Sin variación significativa |
| Activos registrados | ~20 activos iniciales | ~50 activos | ~80 activos |

**Conclusión de volumen:** El volumen total proyectado a 24 meses no 
supera los 500 MB en MongoDB, considerando documentos embebidos de 
evidencias en formato texto y hashes. Este volumen es manejable en 
una instancia local de MongoDB Community Server sin requerir 
estrategias de sharding ni réplicas en la fase inicial.

---

## Requerimientos

### Requerimientos Funcionales

| Requerimiento | Descripción |
| --- | --- |
| RF01 | Registrar un analista con nombre, email y rol. |
| RF02 | Listar todos los analistas registrados. |
| RF03 | Registrar un activo (sistema o dispositivo afectado) con nombre, tipo, dirección IP y descripción. |
| RF04 | Listar todos los activos registrados. |
| RF05 | Crear un incidente asociado a un activo y un analista responsable. |
| RF06 | Agregar evidencias a un incidente. |
| RF07 | Listar incidentes con posibilidad de filtrar por riesgo o estado. |
| RF08 | Listar el detalle de un incidente. |
| RF09 | Registrar una acción tomada sobre un incidente, indicando tipo y analista responsable. |
| RF10 | Listar las acciones asociadas a un incidente específico. |
| RF11 | Generar un reporte de cierre para un incidente cerrado. |
| RF12 | Consultar el reporte asociado a un incidente. |

### Requerimientos No Funcionales

| Requerimiento | Descripción |
| --- | --- |
| RNF01 | La base de datos debe ser MongoDB, ejecutándose localmente. |
| RNF02 | El framework backend debe ser Django 6.0.6 |
| RNF03 | Las vistas serán function-based views con templates HTML simples.|
| RNF04 | El proyecto debe incluir un script de datos de prueba ejecutable desde la shell de Django. |
| RNF05 | El sistema no implementará autenticación de sesiones complejas. El despliegue se acota a infraestructura local de desarrollo. |
| RNF06 | El sistema debe responder en menos de 2 segundos ante consultas de listado de incidentes bajo carga normal (hasta 10 usuarios concurrentes). |
| RNF07 | La disponibilidad esperada es del 95% en horario hábil (lunes a viernes, 9:00–18:00 hrs). |
| RNF08 | Los datos almacenados no deben exponerse a redes públicas. MongoDB debe escuchar exclusivamente en la interfaz local (127.0.0.1).|
| RNF09 | El acceso a MongoDB debe requerir autenticación con usuario y contraseña configurados durante la instalación. |
| RNF10 | El sistema debe registrar en logs las operaciones de escritura sobre incidentes para mantener trazabilidad de auditoría. |

### Requisitos de Seguridad y Cumplimiento Normativo

#### Marco normativo aplicable

El sistema almacena datos personales de analistas (nombre, email, rol) 
y potencialmente de personas involucradas en incidentes de seguridad. 
En consecuencia, el tratamiento de estos datos queda sujeto a la 
normativa chilena vigente de protección de datos personales.

**Ley 19.628** (sobre protección de la vida privada): norma vigente al 
momento del desarrollo del proyecto.

**Ley 21.719** (publicada el 13 de diciembre de 2024, vigente a partir 
del 1 de diciembre de 2026): reforma íntegramente la Ley 19.628 y 
establece obligaciones concretas de seguridad, notificación de brechas 
y derechos de los titulares. Dado que el sistema será operado por una 
consultora privada que trata datos personales, queda dentro del ámbito 
de aplicación de esta ley.

Obligaciones de la Ley 21.719 con impacto directo en este sistema:

| Obligación | Descripción | Impacto en el sistema |
|---|---|---|
| Notificación de brechas | En caso de vulneración de datos personales, notificar a la Agencia de Protección de Datos en un plazo máximo de 72 horas. | El sistema debe mantener logs de acceso que permitan detectar y documentar brechas. |
| Minimización de datos | Solo se deben almacenar los datos estrictamente necesarios para el fin declarado. | Los campos de analistas y activos deben limitarse a los definidos en los RF. |
| Seguridad del tratamiento | Implementar medidas técnicas apropiadas según la naturaleza del tratamiento. | Autenticación en MongoDB, restricción de red, logs de auditoría. |
| Principio de finalidad | Los datos recogidos para gestión de incidentes no pueden usarse para otro fin. | El sistema no debe exponer datos fuera del contexto operativo definido. |

---

## Cotización

### Alcance y especificaciones

**Descripción**: Desarrollo de una aplicación para la gestión de 
incidentes de seguridad.

**Tecnologías**: Python, Django, MongoDB

#### Fases del proyecto
| Fase | Horas |
| --- | --- |
| Levantamiento | 8 horas |
| Arquitectura y Modelado | 15 horas |
| Desarrollo del Backend | 45 horas |
| Integración y Frontend | 30 horas |
| Pruebas y Despliegue | 15 horas |

### Desglose de Costos
| Descripción | Cantidad de horas | Tarifa por hora | Total |
| --- | --- | --- | --- |
| Levantamiento | 8 horas | $15.000 | $120.000 |
| Arquitectura y Modelado | 15 horas | $15.000 | $225.000 |
| Desarrollo del Backend | 45 horas | $15.000 | $675.000 |
| Integración y Frontend | 30 horas | $15.000 | $450.000 |
| Pruebas y Despliegue | 15 horas | $15.000 | $225.000 |
| **Total** | | | **$1.695.000** |

#### Mantención Preventiva y Monitoreo
Costo mensual: $28.250 CLP

Incluye:
- Monitoreo y optimización de base de datos MongoDB.
- Configuración de respaldos automáticos diarios.
- Aplicación de parches de seguridad críticos en Django y Python.
- Renovación y soporte de certificados de seguridad SSL.
- Tiempo de respuesta ante caídas del servidor: Menor a 4 horas 
(en horario hábil).

### Forma de pago
50% al iniciar el proyecto y 50% al término y entrega del proyecto.

---

## Kickoff

### Contexto
El cliente opera actualmente bajo un esquema manual de gestión de 
incidentes basado en plantillas Excel e intercambios por correo 
electrónico, un entorno propenso a la pérdida de trazas críticas y 
dispersión de datos. Dada la naturaleza semiestructurada o heterogénea 
de las evidencias informáticas (parámetros de logs, hashes de archivos, 
capturas de pantalla), se determina que el almacenamiento óptimo 
corresponde a una base de datos orientada a documentos (MongoDB). Esto 
permite un esquema flexible mediante el uso de documentos embebidos para 
consolidar la información en un único punto de acceso.

### Objetivos
1. Diseñar e implementar un almacén de datos centralizado basado en 
MongoDB para registrar y clasificar incidentes de seguridad.
2. Asegurar la persistencia e integridad de evidencias complejas 
utilizando las capacidades NoSQL de MongoEngine (documentos embebidos).
3. Automatizar el rastreo de las acciones tomadas por los analistas y 
estandarizar la generación de reportes de cierre del incidente.

### Alcance
* **Incluye:** Desarrollo e implementación exclusiva de los 12 
requerimientos funcionales definidos en la matriz de requerimientos.
* **Incluye:** Configuración del backend en Django 5.x integrado con 
MongoEngine como ODM para la comunicación con la instancia local 
de MongoDB.
* **Incluye:** Creación de una interfaz gráfica simple mediante 
function-based views y plantillas HTML nativas.
* **Excluye:** Sistemas de autenticación de usuarios, login o gestión 
de sesiones complejas (según RNF05). El despliegue se acota 
estrictamente a infraestructura local de desarrollo.

### Entregables
1. Código fuente completo de la aplicación Django estructurado en capas 
(configuración y aplicación de incidentes).
2. Definición del esquema de base de datos NoSQL implementado en el 
script `models.py`.
3. Script de automatización para la carga de datos de prueba ejecutable 
a través de la shell de Django.
4. Documentación técnica descriptiva del proyecto (este entregable 
unificado).

### Plazos
El proyecto cuenta con una duración total estimada de 113 horas 
cronológicas estructuradas bajo el siguiente esquema secuencial:
* **Levantamiento:** 8 horas.
* **Arquitectura y Modelado NoSQL:** 15 horas.
* **Desarrollo del Backend:** 45 horas.
* **Integración y Capa de Presentación (Frontend):** 30 horas.
* **Pruebas Unitarias y Despliegue Local:** 15 horas.

### Riesgos y Supuestos
* **Supuesto Operativo:** Se asume que el cliente cuenta con una 
instancia activa y accesible de MongoDB Community Server corriendo en 
el puerto por defecto (27017) en el entorno de ejecución local.
* **Riesgo Tecnológico:** El desacoplamiento del ORM relacional nativo 
de Django mediante un motor `dummy` inhabilita los componentes que 
dependen de esquemas SQL (como las migraciones nativas o el módulo 
`django.contrib.admin`). Se mitiga mediante el uso directo de los 
métodos de persistencia provistos por los documentos de MongoEngine.
<!-- NUEVO -->
* **Riesgo Normativo:** La Ley 21.719 entra en vigencia el 1 de 
diciembre de 2026. Si el sistema se extiende a un entorno productivo 
real, el cliente deberá adecuar las políticas de tratamiento de datos 
personales antes de esa fecha, incluyendo la designación de un 
responsable de datos y la implementación de un protocolo de 
notificación de brechas en plazo máximo de 72 horas.

### Roles y Responsabilidades
* **Equipo de Desarrollo (Consultor):** Responsable directo de la 
arquitectura del modelo de datos NoSQL, codificación del backend en 
Django, construcción de las vistas HTML y validación del almacenamiento 
correcto de las colecciones.
* **Contraparte del Cliente (Product Owner):** Responsable de validar 
la lógica de los flujos de ciberseguridad, proveer las estructuras de 
ejemplo para las evidencias y otorgar la aceptación final de los 
entregables presentados.

### Criterios de Aceptación (Definition of Done)
Un requerimiento funcional se considerará completado de manera definitiva 
únicamente cuando cumpla los siguientes criterios empíricos:
1. El código asociado compile y se ejecute en el entorno de Django sin 
excepciones de tipo `NameError` o fallos de importación.
2. La vista HTML renderice correctamente la información solicitada.
3. Las operaciones de escritura y lectura impacten de forma directa las 
colecciones configuradas en MongoDB (`incidentes`, `activos`, 
`analistas`, etc.), verificando la correcta integración de los 
documentos embebidos de evidencias.