from django.test import TestCase

# Create your tests here.

def sumar(a,b):
    return a+b

resultado = sumar(10,9)

if resultado == 19:
   print("Prueba exitosa")
else:
   print("Prueba Fallida")

resultado = sumar(-1,9)

if resultado == 8:
   print("Prueba existisa")
else:
   print("Prueba Fallida")



    

