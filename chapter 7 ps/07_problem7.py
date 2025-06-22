'''
for n= 3
  *
 ***
*****

for n= 5
    *
   ***
  *****
 *******
*********
'''

n = int(input("Enter the no."))

for i in range(1, n+1): 
    print(" " * (n - i),end="") # Print spaces to center the stars
    print("*"* (2*i-1),end="")   # Print stars &  this is farmula let i= 1,2,3,.....
    print()   # Move to the next line after printing spaces and stars


