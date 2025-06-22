username = input("enter the username: ")

if(len(username)<10):
    print("A given username contains less than 10 characters")

else:
    print("A given username contains greter than 10 characters")

# ### Example no.2

a = input("Enter the username:- ")
if(len(a)>= 10):
    print(" This is above the 10 character ", )

else:
    print("This is less than 10 character ", )

# ### Example no.3

b = input("Enter the username:")
length = len(b)

if(length>= 10):
    print(f"This is greater than 10 . Length:", {length})

else:
    print(f"This is less than 10  Length:", {length})