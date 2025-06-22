'''
readline and readlines are two different function 

'''
#  new topic :- readline   # only one line print

f= open("myfile")
line = f.readline()
print(line)

f = open("hari.txt")
line = f.readline()
print(line)

# ## new topic :- readlines   # multipal lines are  print


line1= f.readlines()
print(line1, type(line1))

line2 = f.readlines()
print(line2, type(line2))

line3 = f.readlines()
print(line3, type(line3))

line4= f.readlines()
print(line4, type(line4))

line5= f.readlines()
print(line5, "nn")

           ## OR ##

f= open("myfile")
line = f.readline()
while(line != "" ):
    print(line)
    line = f.readline()
f.close()