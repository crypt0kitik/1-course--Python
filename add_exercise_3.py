# simple GAME - application "Rock-paper-scissors"
# game between a user and a computer

# import modules to generate computer choice
# and to make print in colour
import random
from colorama import Fore, Back, Style

# function to compare
# what is greater
# and make return
def greater_rsp(l, r):
    return l + r in ("ps", "sp", "pr")

# main bode of the game
while True:
    # ask a user to write a choice
    while True:
        print("Let's play Rock-paper-scissors!")
        user_input = input("What do you choose (r - rock, s - scissors, p - paper)? \n")
        # make all letters lower to use them
        user_input = user_input.lower()
        # if a user inputs something else
        # ask again to input data
        if user_input not in ("r", "s", "p"):
            print("You wrote something wrong... Try again! :)")
            print()
            continue
        else:
            break
    # print what a user choices
    print(f'You chose - {"rock" if user_input == "r" else "scissors" if user_input == "s" else "paper" if user_input == "p" else ""}.')
    # make a random choice for a computer
    computer = 'rsp'[random.randint(0, 2)]
    # print what a computer choices
    print(f'Computer chose - {"rock" if computer == "R" else "scissors" if computer == "S" else "paper"}.')

    # run the function to compare
    # and print results of the game
    if greater_rsp(user_input, computer):
        print(Fore.BLUE + "YOU ARE A WINNER" + Style.RESET_ALL)
        print()
    elif greater_rsp(computer, user_input):
        print(Fore.RED + "Sorry...the computer is a winner" + Style.RESET_ALL)
        print()
    else:
        print(Fore.GREEN + "Friendship is winner!" + Style.RESET_ALL)
        print()

    # ask about continuing in the loop
    ask_to_cont = input("If you want to continue, enter yes (y): \n")
    # if yes, repeat the main body
    if ask_to_cont == "y":
        print()
        continue
    else:
        print("See you in the next time!")
        break
    print()