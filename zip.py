#Concatenar 2 ou mais lista
lista1 = [1,2,3,4,5]
lista2 = ["Abacate", "Bola", "Cachorro", "Dinheiro", "Elefante"]
lista3 = [" - R$ 2.00", " - R$ 5.00", " - Não tem preço", " - Não tem preço", " - Não tem preço"]

for numero, nome, valor in zip(lista1,lista2,lista3):
	print(numero, nome, valor)
