# Proyecto Tracker de Incidentes - Entregable 1

## Levantamiento de Información

### Situación Actual
El cliente es una empresa de consultoría de ciberseguridad con sede en 
Santiago, Chile. La empresa gestiona incidentes de seguridad de forma 
manual, mediante plantillas Excel compartidas por correo electrónico. 
Esto genera problemas de trazabilidad, pérdida de información y 
dificultad en la asignación de analistas.

### Técnica de Levantamiento
Para el levantamiento de información se utilizó la técnica de entrevista simulada con el cliente (Product Owner). Esta técnica se seleccionó porque permite explorar a fondo los procesos manuales actuales y entender los dolores del negocio desde la perspectiva de los usuarios finales, generando una base sólida para definir requerimientos ajustados a su realidad operativa.

### Problemas Identificados
- No existe un registro centralizado de incidentes.
- Las evidencias se pierden o quedan dispersas.
- No hay seguimiento formal de las acciones tomadas por cada analista.
- No se generan reportes de cierre estandarizados.

### Actores Identificados
- **Analista de Seguridad:** Usuario encargado de registrar incidentes, agregar evidencias y generar reportes.
- **Product Owner (Cliente):** Revisa y valida la gestión de incidentes y reportería.

### Supuestos y Restricciones del Negocio
- **Supuesto:** El cliente cuenta con servidores en un entorno local donde podrá alojarse la base de datos (MongoDB).
- **Restricción:** El sistema no debe estar expuesto a internet público debido a la sensibilidad de las evidencias manejadas.

### Necesidades Identificadas
- **N01:** Registrar y clasificar incidentes de seguridad por severidad y estado.
- **N02:** Asociar cada incidente a un activo afectado y a un analista responsable.
- **N03:** Almacenar evidencias de distintos tipos y formatos para cada incidente.
- **N04:** Registrar acciones de mitigación para cada incidente.
- **N05:** Emitir un reporte de cierre al resolver el incidente.

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
supera los 500 MB en MongoDB. Este volumen es manejable en 
una instancia local de MongoDB Community Server sin requerir 
estrategias de sharding ni réplicas en la fase inicial.

---

## Requerimientos

### Requerimientos Funcionales

| Requerimiento | Descripción | Prioridad | Origen |
| --- | --- | --- | --- |
| RF01 | Registrar un analista con nombre, email y rol. | Alta | N02 |
| RF02 | Listar todos los analistas registrados. | Alta | N02 |
| RF03 | Registrar un activo (sistema o dispositivo afectado) con nombre, tipo, dirección IP y descripción. | Alta | N02 |
| RF04 | Listar todos los activos registrados. | Alta | N02 |
| RF05 | Crear un incidente asociado a un activo y un analista responsable. | Alta | N01, N02 |
| RF06 | Agregar evidencias a un incidente. | Alta | N03 |
| RF07 | Listar incidentes con posibilidad de filtrar por riesgo o estado. | Media | N01 |
| RF08 | Listar el detalle de un incidente. | Alta | N01 |
| RF09 | Registrar una acción tomada sobre un incidente, indicando tipo y analista responsable. | Alta | N04 |
| RF10 | Listar las acciones asociadas a un incidente específico. | Media | N04 |
| RF11 | Generar un reporte de cierre para un incidente cerrado. | Media | N05 |
| RF12 | Consultar el reporte asociado a un incidente. | Baja | N05 |

### Requerimientos No Funcionales

| Requerimiento | Descripción | Prioridad |
| --- | --- | --- |
| RNF01 | La base de datos debe ser MongoDB, ejecutándose localmente. | Alta |
| RNF02 | El framework backend debe ser Django 6.0.6. | Alta |
| RNF03 | Las vistas serán function-based views con templates HTML simples. | Baja |
| RNF04 | El proyecto debe incluir un script de datos de prueba ejecutable desde la shell de Django. | Media |
| RNF05 | El sistema no implementará autenticación de sesiones complejas. El despliegue se acota a infraestructura local de desarrollo. | Media |
| RNF06 | El sistema debe responder en menos de 2 segundos ante consultas de listado de incidentes bajo carga normal. | Alta |
| RNF07 | La disponibilidad esperada es del 95% en horario hábil (lunes a viernes, 9:00–18:00 hrs). | Media |
| RNF08 | Los datos almacenados no deben exponerse a redes públicas. MongoDB debe escuchar exclusivamente en la interfaz local. | Alta |
| RNF09 | El acceso a MongoDB debe requerir autenticación con usuario y contraseña configurados durante la instalación. | Alta |
| RNF10 | El sistema debe registrar en logs las operaciones de escritura sobre incidentes para mantener trazabilidad de auditoría. | Alta |

### Justificación de uso de base de datos NoSQL
Para resolver el problema planteado, se ha decidido utilizar un motor de bases de datos NoSQL Documental (MongoDB) fundamentado en:
1. **Estructura variable y semiestructurada:** Las evidencias recolectadas varían ampliamente (trazas de log, hashes, capturas de red, extractos de memoria). Un esquema relacional requeriría tablas excesivamente normalizadas o con campos opcionales nulos, mientras que en un diseño documental las evidencias disímiles se embeben de manera natural.
2. **Agrupación de datos para consultas rápidas:** Al consultar el detalle de un incidente, usualmente se requiere cargar al instante sus evidencias. El enfoque documental permite recuperar toda la entidad y sus dependencias en una única operación de lectura.
3. **Escalabilidad ágil:** El negocio de ciberseguridad es dinámico, y frecuentemente aparecerán nuevos vectores de ataque que exigirán registrar campos inéditos. La flexibilidad de esquema de MongoDB facilita estas adiciones.

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
