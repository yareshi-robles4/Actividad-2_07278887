print("\n♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("Ejercicio realizado por Yareshi Robles\n")
print("Ejercicio 4: ¿Cuanto tardo en terminar una serie?")

# Damos de alta las variables
serie = "Mi vida con los chicos Walter"
temporadas = 3
episodios_por_temporada = 10
minutos_por_episodio = 50 
horas_al_dia = 2     # cuanto tiempo le dedico diario
# Usamoslas variables en las formulas
# Total de episodios
total_episodios = temporadas * episodios_por_temporada 

# Total de minutos y horas
total_minutos = total_episodios * minutos_por_episodio
total_horas = total_minutos / 60

# ¿Cuantos dias necesito?
dias_necesarios = total_horas / horas_al_dia

print("\nResultados")
print(f"{serie} tiene {total_episodios} episodios")
print(f"Son {total_minutos} minutos en total")
print(f"Equivale a {total_horas:.1f} horas")
print(f"Viendo {horas_al_dia} horas diarias, la terminas en {dias_necesarios:.1f}dias")
print("\n♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")