# Asignación de valores a cadenas de Texto

nombres ="Juan"
apellidos ="Perez"



print(nombres,apellidos)

nombresCompletos = '''Juan 
Perez Gonzales
'''
print(nombresCompletos)

#Funciones de Textos

#Longitud de elementos de un texto
print(len(nombres))

#Verificar si el fragmento del texto está en el texto
print("an" in nombres)

#Verificar si el fragmento del texto NO está en el texto
print("an" not in nombres)

#Cortar cadenas de Texto
print(nombres[2:4])

#Cortar Cadena de Texto Hasta el final
print(nombres[1:])

#Cortar Cadena de Texto Desde el INICIO
print(nombres[:1])

#Convertir a Mayuscula
print(nombres.upper())

#Convertir a Minuscula
print(nombres.lower())

#Remover espacios en Blanco
miFruta ="           manzana            "
miMensaje = miFruta.strip()

print("Tengo una:", miMensaje)

nombreSeparador = "Juan, Perez"
print(nombreSeparador.split(","))

#Reemplazo de valores de un texto

print(nombres.replace("J","P"))

#Concatenacion de Cadenas de Texto

a = "Hola "
b = "Mundo"
c = a+b
print(c)