a = int(input("Enter The age :-"))

# if elif else ladder
if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("This age is invalid")

elif(a==0):  # this condition are 3 possible are present this will be use
    print("This is Not Possible")

else:
    print("you are below the age of consent")
    
# print("End of the programm")