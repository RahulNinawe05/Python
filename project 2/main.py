import random
n = random.randint(1, 10)
a = -1
guesses= 1
while(a != n):
    a = int(input("Guease the Nomber:- "))

    if(a > n):
        print("Lower Number please")
        guesses += 1

    elif(a < n):
        print("Higher Number please")
        guesses += 1

print(f"🎉 Congratulations! You Have guessed The {n} correctily in {guesses} Attempt")
print("Thank For Playing")
