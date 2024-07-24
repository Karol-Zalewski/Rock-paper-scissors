import random

def translate(letter):
    if letter == 'R':
        return "Rock"
    if letter == 'P':
        return "Paper"
    if letter == 'S':
        return "Scissors"

def win_if(player, computer):
    if (player == 'R' and computer == 'S') or (player == 'P' and computer == 'R') or (player == 'S' and computer == 'P'):
        return True
    else:
        return False

def Play():
    player_choice = None
    possible_choices = ['R', 'P', 'S']

    while True:
        try:
            choice = input('Chose:\n(R) - rock\n(P) - paper\n(S) - scissors\n').upper()
            if choice not in possible_choices:
                raise ValueError
        except ValueError:
            print("Wrong choice. Try again. ")
            continue

        computer_choice = random.choice(possible_choices)

        print(f"Your choice: {translate(choice)}\nComputer's choice: {translate(computer_choice)}")

        if win_if(choice, computer_choice):
            print('Gratulation. You have won! ')
        
        elif choice == computer_choice:
            print("It's a draw. ")
        
        else:
            print("You have lost. ")
        
        while player_choice not in ['N', 'Y']:
            player_choice = input("Would you like to continue playing?\nType: (Y) - yes or (N) - No\n").upper()
        
        if player_choice == 'N':
            break

        elif player_choice == 'Y':
            player_choice = None

        

if __name__ == "__main__":
    Play()


    