import random

def play():
    user = [input("'r' for Rock, 'p' for Paper, or 's' for scissors: \n")]

    if user == ['r'] or user == ['p'] or user == ['s']:
        computer = random.choices(['r', 'p', 's'])
        
        print(f"You chose {user}")
        print(f"The computer chose {computer}")

        if user == computer:
            print("It's a tie!")
            return 0

        elif is_win(user, computer):
            print("You win!")
            return 0

        print("You lose!")
        return 0
    else:
        print("Invalid input!")
        exit()


def is_win(player, opponent):
    if (player == ['r'] and opponent == ['s']):
        return True
    elif (player == ['p'] and opponent == ['r']):
        return True
    elif (player == ['s'] and opponent == ['p']):
        return True


if __name__ == "__main__":
    play()
