# **Tecnologías de Información y Ciberseguridad TI3032 — BASES DE DATOS NO ESTRUCTURADAS UNIDAD 4 — UNIDAD INTEGRADORA**

## **PAUTA DE EVALUACIÓN — EVA4**

**Proyecto Integrador: Levantamiento, Formulación e Implementación Básica de una Solución MongoDB**

_Este documento establece el alcance, los entregables y la rúbrica de evaluación del proyecto integrador de la Unidad 4. Léanlo completo, en equipo, antes de comenzar el trabajo._

|**Tipo de evaluación**|Sumativa (EVA4) — Proyecto aplicado, modalidad grupal|
|---|---|
|**Código de evaluación**||
|**Ponderación**|30% de la nota final de la asignatura TI3032|
|**Aprendizajes Esperados Evaluados**|AE 4.1.1, AE 4.1.5 y AE 4.1.6 (detalle en sección 1)|
|**Puntaje total**|100 puntos (exigencia 60% → 60 puntos equivalen a nota 4,0)|
|**Modalidad de trabajo**|Grupal — grupos de 3 a 4 estudiantes (ajustar según matrícula del curso)|
|**Fecha y hora límite de entrega**|Miércoles 15 de julio de 2026, hasta las 23:59 hrs.|
|**Vía de entrega**|mario.yanez12@inacapmail.com|

## **1. Aprendizajes Esperados Evaluados**

Se mantiene la codificación 4.1.1–4.1.6 utilizada en la planificación de la unidad. Esta evaluación se enfoca en el análisis y la formulación del proyecto; los aprendizajes asociados a infraestructura (selección/configuración de SO e instalación del DBMS) quedan fuera del alcance de este instrumento por decisión del/la docente. Solo debe señalar el SO a seleccionar y los fundamentos para ello.

|**AE**|**Descripción**|**¿Evaluado en EVA4?**|
|---|---|---|
|**4.1.1**|Identifica los requisitos del negocio, en base al caso de estudio.|**Sí**|
|**4.1.2**|Selecciona el sistema operativo a emplear, a partir de los requisitos del software de base de datos._|Evaluado solo en fundamento|
|**4.1.3**|Configura el sistema operativo seleccionado, considerando un entorno de virtualización.|Evaluado solo en fundamentos|
|**4.1.4**|_Instala el software de DBMS, tomando en cuenta aspectos de seguridad._|No evaluado en EVA4|
|**4.1.5**|Crea estructuras de base de datos, a partir del caso de estudio.|**Sí**|
|**4.1.6**|Crea componentes de software, considerando conexiones a base de datos.|**Sí**|

## **2. Contexto y Rol a Asumir**

## **Rol del equipo**

Cada grupo conforma una consultora de Tecnologías de la Información contratada por una empresa chilena (el “cliente”) para evaluar e iniciar una solución de información sobre una base de datos NoSQL documental (MongoDB). El grupo deberá recorrer las etapas iniciales reales de un  proyecto de este  tipo:  desde el levantamiento de información  con  el cliente hasta la autorización formal para comenzar el desarrollo (Kick Off), entregando además una primera evidencia técnica — un módulo de software básico — que demuestre la viabilidad de la solución propuesta.

## **3. Caso de Estudio**

El caso de estudio sobre el que trabajará cada grupo puede definirse de dos formas (a elección del/la docente):

- **Asignado por el docente** al inicio de la unidad — recomendado para mantener consistencia en la corrección entre grupos.
- **Propuesto por el grupo** a partir de un negocio real o realista, validado por el/la docente antes de iniciar el levantamiento.

## **Si se opta por la segunda alternativa, el caso propuesto debe cumplir con:**

- Corresponder a una empresa u organización chilena real o verosímil (rubro libre: comercio, salud, turismo, logística, educación, etc.).

- Presentar datos con estructura variable o semi-estructurada (catálogos heterogéneos, atributos opcionales, información anidada), de forma que se justifique el uso de MongoDB por sobre un modelo relacional.

- Tener al menos 3 entidades principales que permitan aplicar la metodología de decisión colección/subdocumento vista en clases.

- No ser un caso ya resuelto en el material de la unidad (ej. AndeanLodge) ni una copia sin adaptación de un caso publicado en internet.

## **4. Alcance del Proyecto**

## **Dentro del alcance**

- Levantamiento de requerimientos
- Documento de requerimientos (RF/RNF)
- Casos de uso

## **Fuera del alcance (No se evalúa)**

- Instalación y hardening del motor MongoDB (DBMS)(no se evalúa)
- Despliegue en ambiente productivo
- Cotización
- Acta de Kick Off
- Diseño de colecciones (modelo de datos)
- Módulo de software básico con conexión a MongoDB y operaciones CRUD mínimas (Create y Read)
- Selección, instalación o configuración del sistema operativo **(se evalúa solo a nivel teórico)**
- Configuración de entornos de virtualización **(se evalúa solo a nivel teórico)**
- Interfaz gráfica de usuario (frontend) — basta con scripts, consola o un endpoint simple de prueba.

## **5. Entregables**

El proyecto se organiza en seis entregables, ordenados según el ciclo de vida real de un proyecto de consultoría TI: primero se analiza y formaliza el negocio con el cliente, luego se cotiza y autoriza el inicio, y solo entonces se construye la primera evidencia técnica.

## **5.1 Levantamiento de Requerimientos (Acta de Levantamiento)**

**Objetivo:** Mostrar cómo el equipo interpretó y comprendió las necesidades reales del negocio a partir del caso de estudio.

## **Contenido mínimo:**

- Contexto del cliente/caso de estudio (rubro, tamaño, problema actual).
- Técnica  de  levantamiento  utilizada  (entrevista  simulada,  encuesta,  observación,  revisión documental) y justificación de por qué se eligió.
- Mínimo 5 necesidades del negocio, redactadas en el lenguaje del cliente (aún no como requerimiento técnico).
- Actores/usuarios identificados preliminarmente.
- Supuestos y restricciones detectadas durante el levantamiento.

**Formato sugerido:** Acta o minuta de 1 a 3 páginas. Puede incluir una transcripción resumida de una entrevista simulada con el “cliente”.

## **5.2 Documento de Especificación de Requerimientos**

**Objetivo:** Formalizar y clasificar lo levantado en el entregable anterior.

## **Contenido mínimo:**

- Mínimo 8 requerimientos funcionales (RF), cada uno con ID, descripción, prioridad y trazabilidad a la necesidad de origen.
- Mínimo  4  requerimientos  no  funcionales  (RNF)  —  por  ejemplo  rendimiento,  seguridad, escalabilidad o disponibilidad.
- Justificación técnica de por qué el caso requiere una base de datos NoSQL documental (datos variables, volumen, escalabilidad, lectura embebida, etc.), aplicando los criterios vistos en clases.

**Formato sugerido:** Tabla de requerimientos por ítem, en el mismo formato usado en el material de la unidad.

## **5.3 Casos de Uso**

**Objetivo:** Modelar el comportamiento funcional del sistema a partir de los requerimientos.

## **Contenido mínimo:**

- Diagrama  de  casos  de  uso  en  notación  UML  (draw.io,  Lucidchart,  PowerPoint  u  otra herramienta), insertado como imagen.
- Mínimo 6 casos de uso, cada uno con: nombre, actor(es), precondición, flujo normal, al menos un flujo alternativo o de excepción, y postcondición.
- Matriz de trazabilidad Caso de Uso ↔ Requerimiento Funcional.

**Formato sugerido:** Diagrama + ficha individual por cada caso de uso.

## **5.4 Cotización (Propuesta Comercial)**

**Objetivo:** Simular la propuesta económica que la consultora entregaría al cliente para ejecutar el proyecto.

## **Contenido mínimo:**

- Resumen del alcance cotizado, en base a los entregables definidos.
- Desglose de actividades/fases con horas estimadas y rol responsable (Analista, Desarrollador, Jefe de Proyecto, etc.).
- Tarifa por hora o por rol, indicando el criterio o fuente usada para definirla.
- Costo neto, IVA (19%) y total con impuestos.
- Plazo de ejecución estimado y vigencia de la oferta.
- Forma de pago y exclusiones explícitas (qué no incluye la cotización).

**Formato sugerido:** Documento de propuesta comercial de 1 a 2 páginas, con tabla de costos.

## **5.5 Acta de Kick Off (Autorización de Inicio)**

**Objetivo:** Formalizar la autorización del cliente para iniciar el proyecto, una vez aceptada la cotización.

## **Contenido mínimo:**

- Nombre del proyecto, fecha de inicio y término estimado.
- Presupuesto autorizado — debe ser coherente con el valor cotizado en el punto 5.4.
- Objetivos y entregables comprometidos para el proyecto.
- Equipo de proyecto, con roles y responsabilidades de cada integrante del grupo.
- Mínimo 4 hitos del proyecto, con fecha estimada.
- Mínimo 3 riesgos identificados y su plan de mitigación.
- Criterios de éxito del proyecto.
- Espacio de autorización (nombre y rol del “cliente/patrocinador” y del líder de proyecto).

**Formato sugerido:** Acta de Constitución de Proyecto / Project Charter, 1 a 2 páginas.

## **5.6 Diseño de Base de Datos y Módulo de Software Básico**

**Objetivo:** Transformar el análisis en una estructura de datos funcional y un componente de software que se conecte a ella.

## **Contenido mínimo:**

- Diseño — Identificación de entidades y decisión justificada colección vs. subdocumento, aplicando la metodología de las 4 preguntas vista en clases (independencia, volumen, consulta, reutilización).
- Diseño — Script de creación de al menos 3 colecciones en MongoDB, con validación de esquema ($jsonSchema) en al menos 2 de ellas.
- Diseño — Al menos un índice por colección, con su justificación.
- Módulo — Conexión funcional a una instancia de MongoDB (local o Atlas), en el lenguaje/framework visto en clases (se sugiere Django, Python + PyMongo u otro autorizado por el docente).
- Módulo — Operaciones mínimas implementadas: Create y Read sobre al menos una colección (Update/Delete son un plus, no obligatorias para un módulo “básico”).
- Módulo — Evidencia de ejecución (capturas de pantalla o video corto) y archivo README con instrucciones de instalación y ejecución.

**Formato sugerido:** Carpeta comprimida (.zip) o enlace a repositorio (puede ser privado, agregando al/a la docente como colaborador/a).

## **6. Calendario Sugerido (Referencial)**

Hitos internos para que cada grupo se autogestione. No son fechas de entrega oficiales (excepto la última) y pueden ajustarse.

|**Fecha sugerida**|**Hito**|
|---|---|
|Hasta el 06 de julio de 2026|Levantamiento de Requerimientos + Documento de Especificación de Requerimientos|
|Hasta el 10 de julio de 2026|Casos de Uso + Cotización|
|**15 de julio de 2026, 23:59 hrs**|**Acta de Kick Off + Diseño de BD + Módulo de Software + Entrega final consolidada**|

## **7. Formato y Vía de Entrega**

- Un archivo PDF único que consolide los entregables 5.1 a 5.5 (Levantamiento, Documento de Requerimientos, Casos de Uso, Cotización y Kick Off), con portada grupal (integrantes, sección, fecha).
- Un archivo .zip o enlace a repositorio con el contenido del punto 5.6 (script de colecciones, código del módulo, README y evidencias de ejecución).
- Nomenclatura sugerida: GrupoN_Apellido1Apellido2_EVA4.pdf y GrupoN_Apellido1Apellido2_EVA4.zip. 
- Ambos archivos se suben en [plataforma institucional indicada por el/la docente] antes de la fecha y hora límite.

## **8. Consideraciones Generales**

- **Uso de Inteligencia Artificial:** se permite como apoyo para redacción o generación de código, siempre que el equipo pueda explicar y defender cada decisión tomada. El/la docente podrá citar a una breve defensa oral grupal (5 a 10 minutos) para verificar la comprensión del trabajo entregado.
- **Consistencia entre entregables:** los montos, plazos y alcance deben ser coherentes entre la Cotización y el Kick Off (ver descuentos transversales en la sección 9.1).
- **Redacción y formato:** se evaluará ortografía, redacción profesional y formato (portada, numeración, tipografía consistente).
- **Trabajo grupal:** todos los integrantes deben poder responder por cualquier parte del trabajo. La participación desigual podrá ajustar la nota individual a criterio del/la docente.
- **Entrega fuera de plazo:** [ajustar según la normativa vigente de la sede/carrera].

## **9. Rúbrica de Evaluación**

Puntaje total: 100 puntos. Cada criterio corresponde a uno de los entregables de la sección 5 y se asocia a un Aprendizaje Esperado de la sección 1.

|**Criterio**|**LOGRADO 100% del puntaje**|**EN DESARROLLO ~60% del puntaje**|**NO LOGRADO 0–30% del puntaje**|
|---|---|---|---|
|**1. Levantamiento de Requerimientos** AE 4.1.1 · 12 pts_|Proceso de levantamiento claro y justificado; mínimo 5 necesidades en lenguaje del cliente; actores y supuestos correctamente identificados.|Levantamiento superficial o técnica no justificada; faltan necesidades, actores o supuestos, o son poco claros.|No se evidencia proceso de levantamiento, o el contenido es genérico y sin relación con el caso asignado.|
|**2. Documento de Requerimientos** AE 4.1.1 · 16 pts_|Mínimo 8 RF y 4 RNF, numerados, priorizados y trazables al levantamiento; clasificación correcta; justificación sólida del uso de NoSQL.|Cumple parcialmente la cantidad o falta priorización/trazabilidad; confunde RF con RNF en algunos casos; justificación de NoSQL débil.|Requerimientos vagos o no numerados, sin relación clara con el caso, o sin RNF.|
|**3. Casos de Uso** AE 4.1.1 · 16 pts_|Diagrama UML correcto y legible; mínimo 6 casos de uso completos (actor, flujo normal, alternativo, pre/postcondición); trazabilidad a RF correcta.|Diagrama con errores de notación o casos de uso incompletos; trazabilidad parcial o ausente.|Menos de 4 casos de uso, sin diagrama, o sin relación con los requerimientos.|
|**4. Cotización** AE 4.1.1 · 13 pts_|Desglose de horas por fase/rol coherente  con el alcance; tarifas justificadas; cálculo  correcto de IVA y total; plazo y  condiciones claras.|Cálculos incompletos o erróneos, tarifas sin justificar, o falta alguna sección (plazo, exclusiones, vigencia).|No hay cotización, o los montos no guardan relación con el alcance del proyecto.|
|**5. Acta de Kick Off** AE 4.1.1 · 13 pts_|Acta completa y coherente con la cotización (mismo presupuesto y plazo); hitos, roles, riesgos y criterios de éxito bien definidos.|Acta incompleta (faltan hitos o riesgos) o con inconsistencias menores respecto a la cotización.|No hay acta de kick off, o el presupuesto/plazo no coincide con la cotización.|
|**6. Diseño de Estructuras de BD** AE 4.1.5 · 15 pts_|Decisión colección/subdocumento justificada para cada entidad según la metodología de la unidad; mínimo 3 colecciones con validación de esquema en al menos 2; índices justificados.|Colecciones creadas pero sin justificación de diseño clara; validación de esquema parcial; índices no justificados.|No se crean colecciones, o el diseño no corresponde a las entidades del caso/requerimientos.|
|**7. Módulo de Software Básico** AE 4.1.6 · 15 pts_|Conexión funcional a MongoDB demostrada; operaciones Create y Read implementadas y evidenciadas; código ordenado con README claro.|Conexión funciona parcialmente o solo una operación implementada; evidencia incompleta; falta README.|El módulo no conecta a la base de datos, o no se entrega evidencia de funcionamiento.|

## **9.1 Descuentos Transversales**

Aplicables al puntaje total del proyecto (los 100 puntos de la sección 9), independiente del puntaje obtenido por criterio.

|**Situación**|**Descuento**|
|---|---|
|Inconsistencia de montos o plazos entre Cotización y Kick Off|**-3 pts**|
|Faltas de ortografía o redacción poco profesional, de forma recurrente|**-2 pts**|
|Formato no profesional (sin portada, sin numeración, tipografía inconsistente)|**-2 pts**|
|Entrega fuera del plazo establecido, sin justificación|_Según normativa vigente de la sede/carrera_|

## **10. Escala de Conversión de Puntaje a Nota (1,0–7,0)**

Escala de exigencia 60% (estándar institucional). Ajustar si la carrera define una exigencia distinta.

**Tramo 1 (puntaje < 60 pts):** Nota = 1,0 + 3,0 × (Puntaje obtenido / 60)

**Tramo 2 (puntaje ≥ 60 pts):** Nota = 4,0 + 3,0 × ((Puntaje obtenido − 60) / 40)

|**Puntaje**|**Nota**|**Puntaje**|**Nota**|
|---|---|---|---|
|0 pts|1,0|60 pts|**4,0**|
|10 pts|1,5|70 pts|4,75|
|20 pts|2,0|80 pts|5,5|
|30 pts|2,5|90 pts|6,25|
|40 pts|3,0|100 pts|7,0|
|50 pts|3,5|—|—|



Éxito en el desarrollo de su proyecto.

