print("\n******************************************************")
print("Ejercicio 8: Mi tiempo de pantalla")
print("n******************** TIEMPO DE PANTALLA n**************")
#Damos de alta la variable app y las horas que paso al dia 
app = "TikTok"
horas_diarias = 4
print(f"\nPaso {horas_diarias} horas diarias en {app}")

#Calculamos las horas al año, esta formula dice: horas_anio = 4 * 365
horas_anio = horas_diarias * 365
print(f"Al año son {horas_anio} horas")

#Convertimos las horas a dias completos (1 dia tiene 24 horas)
#Esta formula dice: dias_anio = 1460 / 24, que da 60.833333
dias_anio = horas_anio / 24
#El :.1f muestra solo 1 decimal, asi que se ve 60.8
print(f"¡Eso equivale a {dias_anio:.1f} dias completos sin parar!")

#Calculamos cuantos meses son (un mes tiene aprox. 30 dias)
#Esta formula dice: meses = 60.8 / 30
meses = dias_anio / 30
print(f"\nO sea, casi {meses:.1f} meses de mi año se van en {app}\n")
print("*********************************************************************")