dict1={'a': 3, 'b': 4}
dict2={'a': 7, 'b': 5}
merged = dict1 | dict2
print(merged)

#######         new  
       
rahul = {"a":3, "b":5}
bady = {"d":5, "c": 5}
merged = rahul| bady
print(merged)


######          this is concept
dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 
merged = dict1 | dict2 
print(merged)

# #####     update ( camparing the two  file )

with open('file1.txt', "r") as f1, open('file2.txt',"r") as f2 :
    if f1.read() == f2.read():
        print("This file are same")
    else:
        print("This file are not same")

# ####       update ( copyed the file )

with open('file1.txt', "r") as f1, open('file2.txt', "w") as f2:
    content = f1.read()
    f2.write(content)
print(content)

# ######         update (MERGED TWO FILE)

with open("file1.txt", "r")as f1, open("file2.txt", "r")as f2, open("merged.txt","w")as f3:
    f3.write(f1.read() + "\n")
    f3.write(f2.read())
    print("file merged succesfully")

#######         new  

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    if f1.read() == f2.read():
        print("Thie are Two function are same")
    
    else:
        print("This are not Two function are same")

#######         new  

with open("file1.txt", "r") as f1, open("file2.txt","w") as f2:
    content= f1.read()
    f2.write(content)

print(content)

#######         new  

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("file3,txt", "w") as f3:
    f3.write(f2.read())
    f3.write(f1.read())

    # f1.read(f3.write) #this is not possible
    # f2.read(f3.write) #this is not possible
