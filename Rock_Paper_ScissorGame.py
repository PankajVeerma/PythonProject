import random

n = ["rock", "paper", "scissor"]


if __name__ == "__main__":
    while True:
        computercount = 0
        yourcount = 0
        yourchoice = input(
            """
        1 for Yes
        2 for Exit"""
        )
        if yourchoice == 1:
           for i in range(6):
                yourInput = input(
                    """
        1 rock
        2 paper
        3 scissor """
                )
                if yourInput == 1:
                    youEnter = "rock"
                elif yourInput == 2:
                    youEnter = "paper"
                elif yourInput == 3:
                    youEnter = "scissor"
                computerInput = random.choice(l)
                print(computerchoice)
                print(yourInput)
                if computerInput == yourInput:
                    print("Match tie ")
                    computercount += 1
                    yourcount += 1
                elif (
                    (computerInput == "paper" and yourInput == "scissor")
                    or (computerInput == "rock " and yourInput == "paper")
                    or computerInput == "scissor"
                    and yourInput == "rock "
                ):
                    print(
                        "YOu Win",
                    )
                    yourcount += 1
                else:
                    print("Computer Win  ")
                    computercount += 1
        if yourcount == computercount:
                print("Game Over")
                print("YOur Entery", yourcount)
                print("Computer Entery", computercount)
        elif yourcount > computercount:
                print("YOu Win")
                print("YOur Entery", yourcount)
                print("Computer Entery", computercount)
        else:
                print("Computer Win")
                print("YOur Entery", yourcount)
                print("Computer Entery", computercount)

    else:
            break






import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
