#media do aluno
nota1 = float(input("Informe a N1: "))
nota2 = float(input("Informe a N2: "))
media = (nota1 + nota2) / 2

if media >= 6:
	print("Aprovado com a média de: ", media, "pontos.")
else:
	print("Reprovado com a média de: ", media, "pontos.")