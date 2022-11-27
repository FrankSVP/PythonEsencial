
miNombreMinuscula ="manuel"
miNombreMayuscula ="MANUUEL"

#Convertir la primera letra en Mayuscula
print(miNombreMinuscula.capitalize())

#Convertir la primera a Minuscula
print(miNombreMayuscula.casefold())

#Alinear al centro según un tipo de caracter
print(miNombreMayuscula.center(20,"."))

#Devuelve el número de veces que aparece un valor en la cadena de texto
print(miNombreMayuscula.count("U"))

#Devuelve el número de veces que aparece un valor en la cadena de texto en un rango determinado
print(miNombreMayuscula.count("U",2,6))

#Verificar si la cadena de texto termina con un caracter especificado
print(miNombreMayuscula.endswith("L"))

#Metodo para incorporar espaciado tab
nombreEspacio = "M\tA\tM\tA"
print(nombreEspacio)

print(nombreEspacio.expandtabs(20))

#Método para buscar o encontrar una cadena de texto dentro de otra
print(miNombreMayuscula.find("NU"))

#Método para incorporar un formato especifico en nuestras variables
precio = "Un celular cuesta {price:.2f} Soles"
print(precio.format(price=299))

#Método para encontrar la primera coincidencia de la palabra buscada
print(miNombreMayuscula.index("U"))

#Método para verificar si todos los caracteres de un texto son alfanuméricos (A-Z y 0-9)
alfanumericos ="Hola103"
Noalfanumericos ="Hola103@"

print(alfanumericos.isalnum())
print(Noalfanumericos.isalnum())

#Método para verificar si todos los caracteres de un texto son LETRAS
siLetras ="Hola"
noLetras ="Hola10"

print(siLetras.isalpha())
print(noLetras.isalpha())

#Método para verificar si todos los caracteres de un texto son DIGITOS
siDigitos ="23156"
noDigitos ="Hola10"

print(siDigitos.isdigit())
print(noDigitos.isdigit())

#Método para verificar si el texto es un identificador valido (A-Z)(0-9) o guines Bajos "_"
siValido ="Demo_2"
noValido ="@Demo_2"

print(siValido.isidentifier())
print(noValido.isidentifier())

#Método para verificar si el texto está en minúscula
minuscula1="demo"
minuscula2="Demo"
print(minuscula1.islower())
print(minuscula2.islower())


