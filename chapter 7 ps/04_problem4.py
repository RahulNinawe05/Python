# n = int(input("Enter The Number:"))

# for i in range(2, n):
#     if(n%i)==0:
#         print("This is not prime no.")
#         break
        
# else:
#     print("no. is prime")


### Question no.2

n = int(input("enter the no: "))

for i in range(2 , n):
    if(n%i):
        print("This is a prime no.")
        # this use break
else:
    print("This is not prime no.")