def myfunc(n):
    return abs(n - 50)

# no entiendo que hace eso
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)

print(thislist)

thislist.sort(reverse=True)
print(thislist)