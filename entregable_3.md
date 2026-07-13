# Proyecto Tracker de Incidentes - Entregable 3

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

### Presupuesto Autorizado
<!-- TODO: Agregar monto de presupuesto autorizado (debe calzar con cotización total) -->

### Hitos y Plazos
<!-- TODO: Cambiar las horas por mínimo 4 hitos con fecha estimada de cumplimiento -->
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
* **Riesgo Normativo:** La Ley 21.719 entra en vigencia el 1 de 
diciembre de 2026. Si el sistema se extiende a un entorno productivo 
real, el cliente deberá adecuar las políticas de tratamiento de datos 
personales antes de esa fecha. **Mitigación:** Incluir notificación y adecuación legal.
<!-- TODO: Agregar un tercer riesgo y su mitigación -->

### Roles y Responsabilidades
* **Equipo de Desarrollo (Consultor):** Responsable directo de la 
arquitectura del modelo de datos NoSQL, codificación del backend en 
Django, construcción de las vistas HTML y validación del almacenamiento 
correcto de las colecciones.
* **Contraparte del Cliente (Product Owner):** Responsable de validar 
la lógica de los flujos de ciberseguridad, proveer las estructuras de 
ejemplo para las evidencias y otorgar la aceptación final de los 
entregables presentados.

### Criterios de Aceptación (Definition of Done) / Criterios de Éxito
Un requerimiento funcional se considerará completado de manera definitiva 
únicamente cuando cumpla los siguientes criterios empíricos:
1. El código asociado compile y se ejecute en el entorno de Django sin 
excepciones de tipo `NameError` o fallos de importación.
2. La vista HTML renderice correctamente la información solicitada.
3. Las operaciones de escritura y lectura impacten de forma directa las 
colecciones configuradas en MongoDB (`incidentes`, `activos`, 
`analistas`, etc.), verificando la correcta integración de los 
documentos embebidos de evidencias.

### Autorización
<!-- TODO: Espacio para firmas del Cliente y el Líder de Proyecto -->

---

## Diseño de Base de Datos
<!-- TODO: Añadir script de validación nativo MongoDB ($jsonSchema) -->
<!-- TODO: Añadir justificación de Colección vs Subdocumento -->
<!-- TODO: Añadir justificación de índices -->

## Módulo de Software Básico
<!-- TODO: Adjuntar código, README con instrucciones y Evidencia de Ejecución (video o capturas) -->
