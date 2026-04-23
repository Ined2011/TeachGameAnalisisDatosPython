from src.limpieza import (
	cargar_datos,
	manejar_valores_nulos,
	estandarizar_texto,
	validar_notas,
	eliminar_duplicados
)

# 1. Cargar datos
estudiantes = src.limpieza.cargar_datos("data/estudiantes.csv")
calificaciones = src.limpieza.cargar_datos("data/calificaciones.csv")

# 2. Limpieza de estudiantes
estudiantes = manejar_valores_nulos(estudiantes)
estudiantes = estandarizar_texto(estudiantes, ["nombre", "grado"])
estudiantes = eliminar_duplicados(estudiantes, "id_estudiante")

