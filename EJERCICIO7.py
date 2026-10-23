print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Ejercicio 7: Subir de nivel")
print("SUBIR DE NIVEL")
#Damos de alta los variables: la XP que tengo, la que necesito y la que gano la partida
xp_actual = 1250
xp_siguiente_nivel = 2000
xp_por_partida = 120
print(f"\nTengo {xp_actual} de XP y necesito {xp_siguiente_nivel} para subir de nivel")
print(f"En cada partida gana {xp_por_partida} de XP")

#Calculamos cuanta XP me falta, esta formula dice: xp_faltante = 2000 - 1250
xp_faltante = xp_siguiente_nivel - xp_actual
print(f"Me faltan {xp_faltante} de XP")

#Calculamos cuantas partidas COMPLETAS necesito
#El // es diversion entera: solo da el numero completo, sin decimales
#Esta formula dice: partidas = 750 // 120, que da 6 (porque 120 x 6 = 720)
partidas = xp_faltante // xp_por_partida
print(f"Con {partidas} partidas llego casi al nivel")

#Calculamos cuanta XP sobra despues de esas partidas
#El % es el residuo: lo que sobra de la division
#Esta formula dice: xp_sobrante = 750 % 120, que da 30 8 porque 750 - 720 = 30)
xp_sobrante = xp_faltante % xp_por_partida
print(f"Pero todavia me faltarian {xp_sobrante} de XP, asi que necesito jugar una partida mas")

#Sumamos 1 partida mas para cubrir la XP que falta, esta formula dice: partidas_totales = 6 +1
partidas_totales = partidas + 1
print(f"\nEn total necesito jugar {partidas_totales} partidas para subir de nivel\n")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")