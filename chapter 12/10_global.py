a = 89 # global function

def fun():
    global a
    a = 3 # local function
    print(a)

fun()
print(a)