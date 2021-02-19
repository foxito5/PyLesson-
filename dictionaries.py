squares = {}
for i in range(6):
    squares[i] = i*i

squares[7] = "glenn"
squares[8] = "glenn Pavel"
squares[6] = "Pavel del 6"
squares[16] = "Pavel del 16"
squares[17] = "Pavel del 17"

print(squares)

del(squares[6])  # eliminacion
squares.pop  # pop

for key in squares:
    print(key)

for key, value in sorted(squares.items()):
    print(key, value)