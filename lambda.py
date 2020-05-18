#quando se deseja usar uma função apenas uma vez
valor = [1,2,3,4,5]

a = map(lambda i: i*2, valor)
a = list(a)

print(a)