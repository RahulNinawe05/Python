marks=int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    gread ="EX"
if(marks<=90 and marks>=80):
    gread ="A"
if(marks<=80 and marks>=70):
    gread ="B"
if(marks<=70 and marks>=60):
     gread ="C"
if(marks<=60 and marks>=50):
    gread ="D"
if(marks<=50):
    gread ="F"

print("your gread is: ",gread)

    #Quistion No.2

mark = int(input("Enter your mark : "))

if(mark<=100 and mark >= 75):
    print("This is passed")

else:
    print("This is Fail ")