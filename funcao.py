#Palavra reservada def
# def Nome(PARAMETROS)
#	COMANDOS
from math import sqrt

def eq2grau(a,b,c):
	delta = ((b**2) - (4*a*c))
	x1 = (-b + sqrt(delta)) / 2*a
	x2 = (-b - sqrt(delta)) / 2*a
	print("x' =", x1,"  ", "x''= ", x2)

eq2grau(1,-1,-12)
