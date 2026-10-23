print("\n++++++++++++++")
print("Ejercicio 5 realizado por Yareshi Robles\n")
print("Ejercicio 5: ¿Cuanto dura mi playlist?")

# Duracion de cada cancion en segundos
cancion1 = 193
cancion2 = 249
cancion3 = 195
cancion4 = 180
cancion5 = 197

# Sumamos todo
total_segundos = cancion1 + cancion2 + cancion3 +cancion4 + cancion5

# // division entera: cuantos minutos completos caben 
minutos = total_segundos // 60

# % residuo: los segundos que sobran
segundos = total_segundos % 60 
print("\nResultados")
print(f"Total en segundos: {total_segundos}")
print(f"Tu playlist dura {minutos} minutos con {segundos} segundos")
print("\n+++++++++++++++")