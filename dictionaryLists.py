# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.

children = {}  # empty
children["nombres"] = ["Glenn", "Pavel"]
children["apellidos"] = ["Barrientos", "Caraccioli", "Rivera"]
children["apellidos"].append("Golverg")  # ,"Saindfeld".insert("GoldBerg")
children["apellidos"].append("Pavelverg")

print(children["nombres"])
print(children["apellidos"])

dictionary = dict()
list = ["1", "2", "3"]
for value in list:
    for element in range(int(value), int(value)+3):
        dictionary.setdefault(element, []).append(value)

print(dictionary)