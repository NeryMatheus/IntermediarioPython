def par(i):
	if i%2 == 0:
		return i

lista = [1,2,3,4,5,6,7,8,9,10]

var_par = filter(par, lista)

print(list(var_par))