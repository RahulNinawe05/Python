marks1 = int(input("Enter The mark1:- "))
marks2 = int(input("Enter The mark2:- "))
marks3 = int(input("Enter The mark3:- "))

# check the total percentage

total_percentage= (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print(" You ARE PASS",total_percentage)

else:
    print("You Failed , Try again Next Year",total_percentage)