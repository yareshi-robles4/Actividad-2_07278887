print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Ejercicio 9: Tienda de mascotas interactiva")
print("TIENDA DE MASCOTAS DE Yareshi Robles")
#input() le pregunta al usuario y guarda lo que escribe en la variable 
#input() SIEMPRE guarda TEXTO, aunque escribas un numero
mascota = input("\n¿Que mascota quieres adoptar? ")
#Si el usuario escribe gato, ahora mascota vale "gato"

#float() convierte el texto a numero con decimales para poder hacer cuentas
precio_mascota = float(input(f"¿Cuanto cuesta el/la {mascota}? $"))
#Si el usuario escribe 1500, ahora precio_mascota vale 1500.0
precio_croquetas = float(input("¿Cuanto cuesta un mes de croquetas? $"))
#Si el usuario escribe 350, ahora precio_croquetas vale 350.0
#int() convierte el texto a numero entero, porque los meses no llevan decimales 
meses = int(input("¿Para cuantos meses quieres croquetas? "))
#Si el usuario escribe 3, ahora meses vale 3
 
#Calculamos cuanto gasto en croquetas, esta formula dice: costo_croquetas = 350.0 * 3
costo_croquetas = precio_croquetas * meses 
#Ahora costo_croquetas vale 1050.0

#Calculamos el total, esta formula dice: total = 1500.0 + 1050.0
total = precio_mascota + costo_croquetas
#Ahora total vale 2550.0

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Ticket de compra")
#El :.2f muestra 2 decimales, como se ve el dinero
print(f"Mascota: {mascota}  ${precio_mascota:.2f}")
print(f"Croquetas por {meses} meses: ${costo_croquetas:.2f}")
print(f"\nTOTAL A PAGARA: ${total:.2f}\n")
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")