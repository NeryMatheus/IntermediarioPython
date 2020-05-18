frutas = ["Abacaxi", "Melancia", "Abacate"]

tamanho = len(frutas) #verifica o tamanho da lista
print(tamanho)

frutas.append("Limão") #adiciona elementos na lista

for x in frutas:
	print(x)
	pass

del frutas[:] #deleta uma lista ou seus indices [2:](indice 2 ate o final) ou [:](s lista toda)
print(frutas)