def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)

def a(n):
    if(n==0):
        return ("This is not valid")
    
    print("*" * n)
    a = (n-1)

a =(3) 