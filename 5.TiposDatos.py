'''
Tipo de Texto: str
Tipos Numéricos: int, float, complex
Tipos de Secuencia: list, tuplas, range
Tipo de Mapeo: dict

Establecer Tipos de Datos set, frozenset
Tipo Booleano : bool
Tipos Binarios: bytes, bytearray, memoryview
Ninguno Tipo: NoneType
'''

#Obtener el tipo de dato de una variable
miNumero =15
print(type(miNumero))

#Asignar valores a los diferentes Tipos de Datos

texto = "Texto"
print(texto)
entero =203
print(entero)
flotante = 10.1
print(flotante)
complejo = 2j
print(complejo)
lista = ["Perro","Gato","Conejo"]
print(lista)
tupla = ("Perro","Gato","Conejo")
print(tupla)

rangos = range(5)
print(rangos)

x= range (3,6)
for n in x:
    print(n)

diccionario = {'color':'rosa', 'marca':'Zara','talla':'U'}
print(diccionario)

sets = {"Perro","Gato","Conejo"}
print(sets)

setsCongelados = frozenset({"Perro","Gato","Conejo"})
print(setsCongelados)

'''miNuevaLista =['Manzana','Platano','Cereza']
frozen = frozenset(miNuevaLista)
x[1] = "Naranja"
print(x)'''

booleanos = True;
print(booleanos)

bytesPython = b"Hola"
print(bytesPython)

arraysBytes = bytearray(10)
print(arraysBytes)

vistaMemoria  = memoryview(bytes(5))
vistaMemoria2  = memoryview(bytesPython)
print(vistaMemoria)
print(vistaMemoria2)

ningunTipo = None
print(ningunTipo)