def dobro(x):
	return x*2

valor = [1,2,3,4,5]

a = map(dobro, valor)
a = list(a)

for v in a :
	print(v)

print(a)