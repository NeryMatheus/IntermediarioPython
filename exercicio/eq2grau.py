#Resolver questões de 2 Grau
from math import sqrt

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

delta = ((b**2) - (4*a*c))
x1 = (-b + sqrt(delta)) / 2*a
x2 = (-b - sqrt(delta)) / 2*a

print("O valor de x' = ", x1)
print("O valor de x'' = ", x2)