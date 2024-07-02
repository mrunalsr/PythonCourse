#Rock Paper Scissor Game
import random
Rock = 0
Paper = 1
Scissor = 2
user_choice = int(input("Enter your choice : "))

list= [0,1,2]
Comp_choice=int(random.choice(list))
print(Comp_choice)

if user_choice == Comp_choice:
    print("Drop")
elif Comp_choice > user_choice:
    print("Oops! You Lose the game")
elif user_choice > Comp_choice:
    print("Congratulations! You win the game")
elif user_choice == 0:
    print("Congratulations! You win the game")
else:
    print('Oops! You lost the game')

