#Así como nosotros operamos cadenas de textos, también podemos operar números, veamos como lo hacemos
#Existen diferentes operadores


'''
OPERADORES ARITMÉTICOS

Se usan para operar matemáticamente números

+ : suma
- : menos
* : Multiplicación
/ : División
% : Módulo
** : Exponente
// : División redondeada (Dividirá al número entero más cercano)

'''

numero1 =20
numero2 =5

# + : suma
print(numero1+numero2)

# - : menos
print(numero1-numero2)

# * : Multiplicación
print(numero1*numero2)

# / : División
print(numero1/numero2)

# % : Módulo
print(numero1%numero2)

# ** : Exponente
print(numero1**numero2)

# // : División redondeada
print(numero1//numero2)

'''
OPERADORES DE ASIGNACIÓN

Se usan para asignar valores a nuestras variables

=  : Asignación de valor
+=  : Asignación y suma de valores [x = x+5]
-=  : Asignación y resta de valores [x = x-5]
*=  : Asignación y multiplicacion de valores [x = x*5]
/=  : Asignación y división de valores [x = x/5]
%=  : Asignación y módulo de valores [x = x%5]
**=  : Asignación y potenciación de valores [x = x**5]
//=  : Asignación y división redondeada de valores [x = x//5]


&= : Operacion And entre dos valores
5 y 3

0 1 0 1 #Binario = 5
0 0 1 1 #Binario = 3
_____________________________
0 0 0 1 # Binario = 1



|=: Operacion OR entre dos valores

0 1 0 1 #Binario = 5
0 0 1 1 #Binario = 3
_____________________________
0 1 1 1 # Binario = 7


^=: Operacion XOR entre dos valores

0 1 0 1 #Binario = 5
0 0 1 1 #Binario = 3
_____________________________
0 1 1 0 # Binario = 6

'''

numero3 = 100
numero4 = 100
numero5 = 100
numero6 = 100
numero7 = 100
numero8 = 100
numero9 = 100
numero10 = 100

# =  : Asignación de valor
print(numero3)

# +=  : Asignación y suma de valores [x = x+5]
numero4+=2
print(numero4)
# -=  : Asignación y resta de valores [x = x-5]
numero5-=2
print(numero5)
# *=  : Asignación y multiplicacion de valores [x = x*5]
numero6*=2
print(numero6)
# /=  : Asignación y división de valores [x = x/5]
numero7/=2
print(numero7)
# %=  : Asignación y módulo de valores [x = x%5]
numero8%=2
print(numero8)
# **=  : Asignación y potenciación de valores [x = x**5]
numero9**=2
print(numero9)
# //=  : Asignación y división redondeada de valores [x = x//5]
numero10//=2
print(numero10)

#&=: Operacion And entre dos valores
binario1 =5
binario1 &=3

print(binario1)

#|=: Operacion OR entre dos valores
binario2 =5
binario2 |=3

print(binario2)

#^=: Operacion XOR entre dos valores
binario3 =5
binario3 ^=3

print(binario3)

