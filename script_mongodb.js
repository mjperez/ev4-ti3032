// ============================================================================
// Script de Creación de Base de Datos, Colecciones, Esquemas e Índices
// Proyecto: Security Incident Tracker
// Asignatura: Bases de Datos No Estructuradas (TI3032)
// ============================================================================

// 1. Usar la base de datos del proyecto
db = db.getSiblingDB("tracker_incidentes_db");

// COLECCIÓN 1: analistas
db.createCollection("analistas", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["nombre", "email", "rol", "especialidad", "telefono", "horario"],
         properties: {
            nombre: {
               bsonType: "string",
               description: "Nombre completo del analista (Requerido)."
            },
            email: {
               bsonType: "string",
               pattern: "^.+@.+\\..+$",
               description: "Correo electrónico del analista. Debe tener formato de email (Requerido)."
            },
            rol: {
               enum: ["junior", "senior", "lead", "product owner"],
               description: "Nivel jerárquico del analista (Requerido)."
            },
            especialidad: {
               enum: ["forensic", "malware", "network", "cloud", "endpoint", "incident response"],
               description: "Especialidad del analista (Requerido)."
            },
            telefono: {
               bsonType: "string",
               description: "Teléfono de contacto (Requerido)."
            },
            horario: {
               bsonType: "string",
               description: "Horario de trabajo, ej: '9:00 - 18:00' (Requerido)."
            }
         }
      }
   }
});

// Índice para 'analistas'
// Justificación: Garantizar que no se dupliquen usuarios en el sistema (unique: true) 
// y optimizar enormemente las consultas de inicio de sesión o búsquedas directas por correo.
db.analistas.createIndex({ email: 1 }, { unique: true });
db.analistas.createIndex({ rol: 1 }); // Justificación: Optimiza filtros por cargo.


// COLECCIÓN 2: activos
db.createCollection("activos", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["nombre", "tipo"],
         properties: {
            nombre: {
               bsonType: "string",
               description: "Nombre identificador del activo, ej: SRV-WEB-01 (Requerido)."
            },
            tipo: {
               enum: ["servidor", "endpoint", "red"],
               description: "Categoría del activo (Requerido)."
            },
            ip_address: {
               bsonType: "string",
               description: "Dirección IP del activo (Opcional)."
            },
            descripcion: {
               bsonType: "string",
               description: "Descripción adicional del activo (Opcional)."
            }
         }
      }
   }
});

// Índice para 'activos'
// Justificación: Optimizar los filtros de inventario en la vista de activos y la agrupación 
// estadística al contar cuántos servidores, endpoints o redes hay registrados.
db.activos.createIndex({ tipo: 1 });
db.activos.createIndex({ nombre: 1 });


// COLECCIÓN 3: incidentes (Sin validación estricta a nivel MongoDB para 
// permitir máxima flexibilidad en el documento y sus embebidos, cumpliendo 
// la regla de "al menos 2" validadas)
db.createCollection("incidentes");

// Índices para 'incidentes'
// Justificación: El indexamiento por fecha de reporte descendente (-1) optimiza de forma 
// crítica la carga inicial del dashboard y listados, ya que los usuarios siempre buscan 
// ver los incidentes más recientes primero.
db.incidentes.createIndex({ fecha_reporte: -1 });

// Justificación: Optimiza el filtrado dinámico en la interfaz donde el analista
// necesita ver rápidamente los incidentes agrupados por estado (ej: abiertos) o por riesgo.
db.incidentes.createIndex({ estado: 1 });
db.incidentes.createIndex({ severidad: 1 });

print("Base de datos, colecciones con $jsonSchema e índices creados exitosamente.");
