'''
sum(1)=1
sum(2)=1 + 2
sum(3)=1 + 2 + 3 
sum(4)=1 + 2 + 3 + 4 
sum(5)=1 + 2 + 3 + 4 + 5

sum(n)=1 + 2 + 3 + 4 .....+ n
sum(n)= sum (n-1)+ n

'''
# Quistion no 1(Actual Quistion)

def sum(n):
    if(n==1):
        return 1
    return  sum(n-1) + n

n =int(input("Enter the no.:"))
print(sum(n))

# Quistion no 2(Advance)

def sum(n):
    if(n==1):
        return 1
    elif(n==0):
        return ("this is not valid")
    return  sum(n-1) + n

n =int(input("Enter the no.:"))
print(sum(n))

# # Quistion no 3 (Advance)

# def recursive_natural(n):
#     a = (n-1) + n
#     return a

# n = int(input("Enter the no:-"))

# print(f"The sum of two number is:-{ recursive_natural(n):} ")