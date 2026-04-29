from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca
import sys
import io
import random

from faker import Faker

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def generar_libros_aleatorios(cantidad: int, faker_es: Faker) -> list[Libro]:
    libros = []
    palabras_titulo = ["Sombras", "Memorias", "Horizonte", "Viaje", "Ecos", "Destino"]
    for _ in range(cantidad):
        isbn = faker_es.numerify(text="978-0-##-######-#")
        titulo = f"{random.choice(palabras_titulo)} de {faker_es.word().capitalize()}"
        autor = faker_es.name()
        libros.append(Libro(isbn, titulo, autor))
    return libros


def generar_estudiantes_aleatorios(cantidad: int, faker_es: Faker) -> list[Estudiante]:
    estudiantes = []
    carreras = [
        "Ingeniería en Software",
        "Ingeniería Industrial",
        "Ingeniería en Alimentos",
        "Ingeniería en biotecnologia",
    ]
    for _ in range(cantidad):
        cedula = faker_es.numerify(text="09########")
        nombre = faker_es.first_name()
        apellido = faker_es.last_name()
        carrera = random.choice(carreras)
        estudiantes.append(Estudiante(cedula, nombre, apellido, carrera))
    return estudiantes


def main():
    # ─── Crear la biblioteca ───
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")
    print(f"\n{biblioteca}\n")

    # ─── Registrar libros (RF-01) ───
    print("Registrando libros")
    libro1 = Libro("978-0-13-468599-1", "El Principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("978-0-06-112008-4", "Cien Años de Soledad", "Gabriel García Márquez")
    libro3 = Libro("978-84-376-0494-7", "Don Quijote de la Mancha", "Miguel de Cervantes")
    libro4 = Libro("978-84-376-0494-7", "El paseo", "Robert Walser")

    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_libro(libro3)
    biblioteca.registrar_libro(libro4)


    print("\n── Registrando estudiantes ──")
    est1 = Estudiante("0926400615", "Marlon", "Bejarano", "Ingeniería en Software")
    est2 = Estudiante("0912345678", "Danilo", "Loaiza", "Ingeniería en Software")
    est3 = Estudiante("0912345678", "Michael", "Menendez", "Ingeniería en Software")
    est4 = Estudiante("0912345678", "Adolfo", "Anchundia", "Ingeniería en Software")

    biblioteca.registrar_estudiante(est1)
    biblioteca.registrar_estudiante(est2)
    biblioteca.registrar_estudiante(est3)
    biblioteca.registrar_estudiante(est4)

    # ─── Carga aleatoria con Faker ───
    print("\n── Cargando datos aleatorios (Faker) ──")
    faker_es = Faker("es_ES")
    libros_aleatorios = generar_libros_aleatorios(3, faker_es)
    estudiantes_aleatorios = generar_estudiantes_aleatorios(3, faker_es)

    for libro in libros_aleatorios:
        biblioteca.registrar_libro(libro)

    for estudiante in estudiantes_aleatorios:
        biblioteca.registrar_estudiante(estudiante)

    # ─── Estado actual ───
    print(f"\n{biblioteca}\n")

    # ─── Transacciones manuales (RF-03 y RF-04) ───
    print("Realizando préstamos manuales")
    resultado = biblioteca.prestar_libro(
        "978-0-13-468599-1", "0926400615", "2026-04-15", "2026-04-29"
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        "978-0-06-112008-4", "0926400615", "2026-04-15", "2026-05-01"
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        "978-84-376-0494-7", "0912345678", "2026-04-15", "2026-04-22"
    )
    print(resultado)

    # ─── Intentar prestar un libro ya prestado (RF-04: validación) ───
    print("\nIntentando prestar libro ya prestado")
    resultado = biblioteca.prestar_libro(
        "978-0-13-468599-1", "0912345678", "2026-04-16", "2026-04-30"
    )
    print(resultado)

    # ─── Transacciones con datos aleatorios ───
    print("\nRealizando préstamos con datos aleatorios")
    libro_random_1 = libros_aleatorios[0]
    libro_random_2 = libros_aleatorios[1]
    est_random_1 = estudiantes_aleatorios[0]
    est_random_2 = estudiantes_aleatorios[1]

    resultado = biblioteca.prestar_libro(
        libro_random_1.isbn, est_random_1.cedula, "2026-04-17", "2026-04-24"
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        libro_random_2.isbn, est_random_2.cedula, "2026-04-18", "2026-04-25"
    )
    print(resultado)

    print("\nIntentando prestar libro aleatorio ya prestado")
    resultado = biblioteca.prestar_libro(
        libro_random_1.isbn, est_random_2.cedula, "2026-04-19", "2026-04-28"
    )
    print(resultado)

    print(f"\nPréstamos activos de {est_random_1.nombre} {est_random_1.apellido}")
    prestamos_random = biblioteca.consultar_prestamos_activos(est_random_1.cedula)
    for prestamo in prestamos_random:
        print(f"  → {prestamo}")

    print("\nDevolviendo un libro aleatorio")
    resultado = biblioteca.devolver_libro(libro_random_1.isbn, est_random_1.cedula)
    print(resultado)

    print(f"\nPréstamos activos de {est_random_1.nombre} {est_random_1.apellido} (después de devolución)")
    prestamos_random = biblioteca.consultar_prestamos_activos(est_random_1.cedula)
    if prestamos_random:
        for prestamo in prestamos_random:
            print(f"  → {prestamo}")
    else:
        print("  (Sin préstamos activos)")

    # ─── Consultar préstamos activos (RF-06) ───
    print("\nPréstamos activos de Marlon Bejarano")
    prestamos_maria = biblioteca.consultar_prestamos_activos("0926400615")
    for prestamo in prestamos_maria:
        print(f"  → {prestamo}")

    # ─── Devolver un libro (RF-05) ───
    print("\nDevolviendo un libro")
    resultado = biblioteca.devolver_libro("978-0-13-468599-1", "0926400615")
    print(resultado)

    # ─── Verificar que el libro está disponible nuevamente ───
    print(f"\nEstado del libro devuelto")
    print(f"  {libro1}")
    

    # ─── Consultar préstamos activos después de devolución ───
    print("\nPréstamos activos de María López (después de devolución)")
    prestamos_maria = biblioteca.consultar_prestamos_activos("0926400615")
    if prestamos_maria:
        for prestamo in prestamos_maria:
            print(f"  → {prestamo}")
    else:
        print("  (Sin préstamos activos)")

    # ─── Ahora el libro puede prestarse de nuevo ───
    print("\nPrestando el libro devuelto a otro estudiante")
    resultado = biblioteca.prestar_libro(
        "978-0-13-468599-1", "0912345678", "2026-04-16", "2026-04-30"
    )
    print(resultado)

    # ─── Estado final ───
    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()