print("\nEjercicio 3: ¿Cuanto escucho a mi artista favorito?")
print("\nMI ARTISTA FAVORITO\n")

artista = "Omar courtz"
canciones_por_dia = 35
duracion_promedio = 3.13    # minutos por cancion

minutos_dia = canciones_por_dia * duracion_promedio      # minutos al dia 
minutos_anio = minutos_dia * 365                         # minutos al año
horas_anio = minutos_dia / 60                            # 1 hora = 60 minutos
dias_anio = horas_anio / 24                              # 1 dia = 24 horas

print(f"Escuchas a {artista} {minutos_dia} minutos al dia")
print(f"Al año son {minutos_anio} minutos")
print(f"Eso equivale a {horas_anio:.1f} horas")
print(f"¡O sea{dias_anio:.1f} dias completos escuchando a {artista}!\n")