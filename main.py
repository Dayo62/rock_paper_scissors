import random

def play():
    print("\nThis is Rock, Paper, Scissors game\n")
    user = input("['r' for Rock 'p' for Paper 's' for Scissors]\n Pick your choice:")
    computer = random.choice(['r' ,'p', 's'])

    if user == computer:
        return "Unlucky...Its a Tie"

    if win(user, computer):
        return "Well done,You win!!!"
    else:
        return "You lost, Try again"


def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(play())