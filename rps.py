import random

print("<<<<<< WELLCOME TO RPS >>>>>>>>")
user_score = 0
comp_score = 0
ties = 0

name = input(" Enter your name :-")
print("""
1.Paper beats Rock -->Paper
2.Rock beats Scissors -->Rock
3.Scissors beats Paper -->Scissors""")
while True:
    print(""" Choices are
    1.Rock
    2.Paper
    3.Scissors""")


    choice = int(input(" Enter your choice from 1-3 :-"))
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"
    print("This is user_choice ")
    print("Now its turn computer choice")

    computer = random.randint
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    print(" The computer choice is")

    if((user_choice == "Paper" or user_choice == "Rock") and (user_choice == "Rock" or user_choice == "Paper")):
        print("Paper wins")
        result = "Paper"
    elif((user_choice == "Scissors" or user_choice == "Rock") and (user_choice == "Rock" or user_choice == "Scissors")):
        print("Rock wins")
        result = "Rock"
    elif((user_choice == comp_choice)):
        print("its ties")
        result = "Ties"
    else:
        print("Scissors wins")
        result = "Scissors"

    if result == "Tie":
        ties += 1
    elif result == user_choice:
        print("user wins")
        user_score += 1
    else:
        print("computer wins")
        comp_score += 1
    print("Score are")
    print(name,"user_score",user_score)
    print("computer score is", comp_score)

    repeat = input("do you want to play again ?")
    if repeat == "No" or repeat == "No":
        break
    print("end game")
    print("Thank you")