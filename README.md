# Sistema de Gestión de Biblioteca (S2-TAREA_1)

Este repositorio contiene el desarrollo del caso de estudio de una **Biblioteca**, realizado para la asignatura de **Programación Orientada a Objetos (POO)**. El proyecto aplica conceptos de herencia, asociación y encapsulamiento en Python.

---

## 👤 Información del Equipo
* **Carrera:** Ingeniería en Software
* **Semestre:** Cuarto Semestre

**Integrantes:**
* Alex Danilo Loaiza Gomezcuello 
* Michael Alberto Menendez Barzola
* Marlon Steven Bejarano Muñoz
* Christian Adolfo Mora Anchundia

---

## 📖 Estructura del Caso de Estudio
El proyecto se ha desarrollado siguiendo las 4 fases de la ingeniería de software:

1.  **Requerimientos:** Identificación de las necesidades para la gestión de préstamos de libros a estudiantes.
2.  **Análisis:** Definición de los objetos del mundo real y sus interacciones dentro de la biblioteca.
3.  **Diseño:** Creación del diagrama de clases en **PlantUML** (ubicado en `diagramas/`), definiendo atributos, métodos, visibilidad y cardinalidad.
4.  **Desarrollo:** Implementación técnica en **Python** siguiendo una arquitectura modular.

---

## 📂 Estructura del Proyecto en el Repositorio
Siguiendo los lineamientos establecidos, la organización de archivos es la siguiente:

* **`modelo/`**: Contiene la lógica de negocio y las clases del sistema.
    * `persona.py`: Clase base.
    * `estudiante.py`: Clase que hereda de Persona.
    * `libro.py`: Gestión de ejemplares.
    * `prestamo.py`: Lógica de transacciones.
    * `biblioteca.py`: Controlador principal.
* **`diagramas/`**:
    * `diagrama_clases.puml`: Archivo fuente del diagrama en PlantUML.
* **`main.py`**: Archivo principal para ejecutar y probar el sistema.
* **`README.md`**: Documentación del proyecto.

---

