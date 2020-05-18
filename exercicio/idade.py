#Verificando a Idade
idade = int(input("Digite sua idade: "))
if idade >= 18:
	print("Você é maior de idade")
elif idade > 0 and idade <= 17:
	print("Você é menor de idade")
else:
	print("Valor inserido incorreto")
	pass