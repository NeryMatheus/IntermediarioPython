#a = raw_input("Digite o nome do arquivo que deseja abrir: ")

arquivo = open("teste.txt", "r")

linha = arquivo.readlines()

for linhas in linha:
	print(linhas)
	pass