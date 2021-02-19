

"""
This is a comment
written in
more than just one line
"""

for x in "banana":
    print(x)

a = "Hello, World!"
print(a[1])

a = """Lorem ipsum dolor sit amet,
consectetur adip."""
print(a)

a = '''este tambies
es largo.'''
print(a)

print('el tamano del string:', len(a))


a = 100
b = 5
x, y, z = "Orange", "Banana", "Cherry"

givedouble = a/b
giveinteger = a//b


c = 5

# verificar  como funciona esta parte
print('Compara los valores', b == c)
print('Compara las direcciones', b is c)


listaNombres = ['Glenn', 'Pavel']

name = input('ingresee su nombre:')
print(name)

if name in listaNombres:
    print(name, ' es un administrador.')


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


txt = "The best things in life are free!"
print("free" in txt)


if "free" in txt:
    print("Yes, 'free' is present.")

if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# https://www.w3schools.com/python/python_strings_slicing.asp
# ver este
