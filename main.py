import aleatorio as a
import media as m

lista = a.geraListaInt(4)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("Elementos da Lista: ", lista)
print("A méida é: ", media)
print("A mediana é: ", mediana)
print("A moda é: ", moda)