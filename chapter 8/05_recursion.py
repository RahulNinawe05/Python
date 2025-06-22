'''
factorial(0)=1
factorial(1)=1
factorial(2)=2*1
factorial(3)=3*2*1
factorial(4)=4*3*2*1
factorial(5)=5*4*3*2*1
factorial(n)= n*(n-1).....3*2*1

factorial(n)= n* factorial(n-1)

'''

# def factorial(n):
#     if(n==1 or n==1):
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter the no. :-"))
# print(f"factorial of this no. is : {factorial (n)}")


# quistion no 2

def factorial(n):
    if(n==1 or n==0):
        return 1

    else:
        return n * factorial(n-1)   ## The function calls itself here (recursion)

n = int(input("Enter the no."))
print(f"factorial of this no. is : {factorial (n)}")
print(factorial(n))

#Recursion means that a function calls itself to solve a smaller part of the problem.