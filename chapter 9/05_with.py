f= open("myfile")
print(f.read())
f.close

# they will be use #with# statement

with(open("myfile")) as f:
    print(f.read)


'''
you don't have to use f.close,
becouse complete the with statement they will close.

'''


'''
with statement does not require parentheses around,
    with (open("hari.txt")) , like this.
# '''

with open("hari.txt") as f:
    print (f.read())


with open("pratik.txt","w") as f:
    print(f.write(" this is not preatent"))
