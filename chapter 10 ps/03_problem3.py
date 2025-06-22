class Demo:
    a = 4
o = Demo() # print the class atribute becouse instance atribut is not present
print(o.a)

o.a = 0 # instance attibute is set
print(o.a) # print the instance atribute are present  print instance value
print(Demo.a)# prints the class atribut