## 5! = 1*2*3*4*5

n = int(input("Enter the no."))

product =1
for i in range(1, n+1):
    product = product * i

print(f"the factorial of {n} is value {product}")