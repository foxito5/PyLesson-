# yo hice esta funcion y me quedo pijuda
def Fibonnaci(n, lista={}):
    if(n < 2):
        return n

 #   print(lista)

    if (lista.get(n) != None):
        return lista[n]

    val1 = Fibonnaci(n-1, lista)
    val2 = Fibonnaci(n-2, lista)

    if (lista.get(n-1) == None):
        lista[n-1] = val1

    if (lista.get(n-2) == None):
        lista[n-2] = val2

    return val1+val2


print(Fibonnaci(70))
