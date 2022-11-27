# Insertar numeros en cadenas de Texto

anio =10
texto = "Mi nombres Pedro y mi edad es de {} años"
print(texto.format(anio))


# Insertar numeros en cadena de Texto en un orden determinado

sueldoBruto=100
descuento =20
totalSueldo =80

miSueldoFinal = "Sueldo:{0}, Descuento:{1}, Total de Sueldo {2}"

print (miSueldoFinal.format(sueldoBruto,descuento,totalSueldo))
