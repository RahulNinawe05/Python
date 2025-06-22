a = int(input("Enter the no.:-"))
b = int(input("Enter the no.:-"))


# raise n programm crash hote

if (b == 0):
    raise ZeroDivisionError("this type of error are stop")

else:
    print(f" the divison of a/b {a/b}")

print("TRY AGAIN") # don't print becouse program are crash