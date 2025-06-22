class Employee:
    def __init__(self):
        print("constructor of Employee")
    a = 1

class programmer(Employee):
    def __init__(self):
        print("constructor of programmer n")
    b = 2

class manger(programmer):
    def __init__(self):  # print the parent constructore 
        super().__init__() ## Calls Parent's __init__ method
        print("constructor of manger")
    c = 3

# # this is wrong

# o = Employee()
# print(o.a) #print the a 

# o = programmer()
# print(o.a,o.b)

o = manger()
print(o.a, o.b, o.c)

