#               Using walrus operator
if (n := len([1, 2, 3, 4, 5])) < 3:     # all opereter in one line
     print(f"List is too long ({n} elements, expected <= 3)") 
     # Output: List is too long (5 elements, expected <= 3)

else:
     print(f"this len is not {n}")

#              new

if(v :=  (["rahul", "Ninawe"])) < 4:
     print(f"this is not present {v}")

else:
     print(f"this is present {v}")

#                 new
if (n := len([1,2,3,4,5,67,3])) > 4:
     print(f"this is present")

else:
     print("this is not present")

#                   new

if (n:= len(["rahul", 23,4, 5,334,34.2,])) > 4:
     print("this is a greter than 4")

else:
     print("this is not greter than 4")