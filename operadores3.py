thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist = thislist + ["uvas","limones"]

print(thislist[2:5])
print(thislist[:4])

print(thislist[-4:-1])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


thislist[1:3] = ["watermelon"]  # remnove 2 and add 1
print(thislist)

thislist.insert(2, "Glenn")
