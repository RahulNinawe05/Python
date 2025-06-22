import random
'''
1 for snake
-1 for water
0 for gun

'''

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"s" : 1,"w": -1, "g" : 0}
reversDict ={1: "snake", -1: "water", 0: "gun"}

you =youDict[youstr]

# by now we have 2 number (veriabel) you and computer 

print(f"you chose {reversDict[you]} \n computer chose {reversDict[computer]}")

if(computer  == you ):
    print("it's a drow")

else:
    if(computer == -1 and you == 1):     #-2
        print("You win!")

    elif(computer == -1 and you == 0):   #-1
        print("You Lose!")
        
    elif(computer == 1 and you == -1):   #2
        print("You Lose!")

    elif(computer == 1 and you == 0):    #1
        print("You win!")

    elif(computer == 0 and you == 1):    #-1
        print("You win!")

    elif(computer == 0 and you == -1):   # 1
        print("You Lose!")

    else:
        print("something went wrong")

if((computer - you)==-1 or (computer - you)==2):
    print("You Lose")