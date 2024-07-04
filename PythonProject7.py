#A number is given by the computer between 1 to 50 and the user according to level get attempts to guess a number
# if the guess is correct okay not then upto last attempt navigate the user if the user then also don't understant
# print lose the game
import random
def start():
    print("Welcome to the number game : ")
    number = random.randint(1,50)
    print("Think a number from 1 to 50 in your mind ")
    return number

def output(result):
    input1 = str(input("Enter the level of game easy or medium or hard : "))
    if input1 == 'easy':
        attempt = 10
        print("You will get 10 chances to guess the number : ")
        for i in range(attempt):
            var = int(input("enter the number here : "))
            attempt -=1
            print("No of attempts left are : ", attempt)
            if attempt == 0:
                print("You lose")
            elif var == result:
                print("Congrats you win the game :")
            elif var > result:
                print("You are far from result")
            elif var < result:
                print("You are near to the result")


    elif input1 == 'medium':
        attempt = 5
        print("You will get 5 chances to guess the number")
        for i in range(attempt):
            var = int(input("enter the number here : "))
            attempt -= 1
            print("No of attempts left are : ",attempt)
            if attempt == 0:
                print("You lose attempts are over")
            elif var == result:
                print("Congrats you win the game :")
                break
            elif var > result:
                print("You are far from result")
            elif var < result:
                print("You are near to the result")
            else:
                print("You lose your guesses are wrong")


    elif input1 == 'hard':
        attempt =3
        print("You will get 3 chances to guess the number")
        for i in range(attempt):
            var = int(input("enter the number here : "))
            attempt -= 1
            print("No of attempts left are : ", attempt)
            if attempt == 0:
                print("You lose")
            elif var == result:
                print("Congrats you win the game :")
            elif var > result:
                print("You are far from result")
            elif var < result:
                print("You are near to the result")

result = start()
print(result)
output(result)
