import random
def roll(count, side ):
    x = int(count)
    sum = 0

    print("Number of dice is " + str(count) + " number of sides is "+str(side))

    for i in range(x):
        temp = random.randint(1, int(side))

        print(str(temp))

        sum+=temp

    print("sum = "+str(sum))




print("Welcome to Dice Roller")

print("How many dice to roll?")

diceCount = input()

print("How many sides does the die have?")

diceSide = input()

roll(diceCount, diceSide)



