x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


# usando globales

y = "awesome"


def myfuncY():
    global y
    y = "fantastic"


myfuncY()
print("Python is y:" + y)
