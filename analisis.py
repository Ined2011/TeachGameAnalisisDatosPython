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

