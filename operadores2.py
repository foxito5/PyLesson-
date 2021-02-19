
nombre = "Glenn Pavel"
print(f"Software engineer {nombre}")


marcas = ["Toyota", "Nissan", "Benz"]  # this is a list
marcas += ["Izusu", "Hashton Martin", "Bentley"]

marcas.append("Datzun")
marcas.insert(0, "Activa")


marcas.sort(reverse=True)  # ordenado
marcas.reverse()  # reversion de orden


print(marcas)

popped = marcas.pop(0)

print(f"se hizo pop a {popped} ")

for f in marcas:
    print(f)

# for i in range(2, 5):
#     print(f"{i} de 5")


aTupple = 'Mary', 'had', 'a', 'little', 'lamb'  # this is a tupple not a list

slice = aTupple[2:5]
for i in range(len(slice)):
    print(f"slice of tupple {i} : {slice[i]} ")


dictionary = {'a': 0, 'z': 25}
for index, (key, value) in enumerate(dictionary.items()):
    print(f" diccionario item {index}")

# tuples
t1 = 1, 2, 3
t2 = 4, 5, 6
t3 = t1+t2 + (6, 6, 7)

tMin = min(t3)
tMax = max(t3)
print(f"tuplas valor minimo :{tMin} maximo:{tMax}")
print(t3.count(6))

listFromTupple = list(t3)
print(f"list from tupple {listFromTupple}")
