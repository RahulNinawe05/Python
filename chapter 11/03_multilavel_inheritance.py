class Employee:
    a = 1

class programmer(Employee):
    b = 2

class manger(programmer):
    c = 3

# this is wrong
o = Employee()
print(o.a) #print the a 
# print(o.b) # show the error as there is NO "b" attribute in Employee class

o = programmer()
print(o.a,o.b)

o = manger()
print(o.a, o.b, o.c)

