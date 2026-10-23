print("\n♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("Ejercicio 10: Reto final, ¿soy viral?")
print("CALCULADORA DE ENGAGEMENT HECHO POR Yareshi Robles")

#input() guarda texto, aqui no convertimos porque el usuario es texto
#Si el usuario escribe mi_cuenta, ahora usuario vale "mi_cuenta"
usuario = input("\nTu usuario de instagram/TikTok: @")

#int() convierte el texto a numero entero para poder hacer cuentas 
#Si el usuario escribe 800, ahora seguidores vale 800
seguidores = int(input("¿Cuantos seguidores tienes? "))
#Si el usuario escribe 60, ahora likes vale 60
likes = int(input("¿Cuantos likes tuvo tu ultimo post? "))
#Si el usuario escribe 12, ahora comentarios vale 12
comentarios = int(input("¿Cuantos comentarios tuvo? "))

#Sumamos todas las interacciones, esta formula dice: interacciones = 60 + 12
#Ahora interacciones vale 72
interacciones = likes + comentarios

#Calculamos el engagemet: que porcentaje de mis seguidores interactuo
#Los parentesis hacen que la division se haga ANTES de multiplicar por 100
#Esta formula dice: engagemet = (72 / 800) * 100, o sea 0.09 * 100
engagment = (interacciones / seguidores) * 100
#Ahora engagement vale 9.0

print(f"\n♥♥♥♥♥♥♥♥♥♥♥♥♥♥ RESULTADO DE @{usuario} ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print(f"Interacciones totales: {interacciones}")
#El :.2f muestra 2 decimales, asi que se ve 9.00%
class engagement:
    def __init__(self, interacciones, seguidores):
        if seguidores <= 0:
            raise ValueError("Los seguidores deben ser mayor que cero.")
        self.porcentaje = (interacciones / seguidores) * 100

    def __format__(self, formato):
        return format(self.porcentaje, formato)


engagement = engagement(interacciones, seguidores)

print(f"Engagement: {engagement:.2f}%")
print("\nDato: en redes, un engagement arriba de 3% ya se considera bueno")
print("\n♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")