import time

def getWinner(player1_choice, player2_choice):
    if player1_choice == 0:
        if player2_choice == 1:
            return 'player 2'
        elif player2_choice == 2:
            return 'player 1'
        else:
            return '.. oh shucks, it\'s a draw'
    elif player1_choice == 1:
        if player2_choice == 0:
            return 'player 1'
        elif player2_choice == 2:
            return 'player 2'
        else:
            return '.. oh shucks, it\'s a draw'
    elif player1_choice == 2:
        if player2_choice == 0:
            return 'player 2'
        elif player2_choice == 1:
            return 'player 1'
        else:
            return '.. oh shucks, it\'s a draw'



def declareWinner(player1_choice, player2_choice):
    moves = ["rock", "paper", "scissors"]
    print(f'Player 1: {moves[player1_choice]}')
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(f'Player 2: {moves[player2_choice]}')
    print(f'Our winner is {getWinner(player1_choice, player2_choice)}')

def play_rps():
    
    player1_choice = int(input("""player one, pick your move:
    rock(1), paper(2), scissors(3)""")) - 1
    
    player2_choice = int(input("""player two, your turn to pick:
    rock(1), paper(2), scissors(3)""")) - 1
    
    print("Let's see who got lucky...")
    time.sleep(1)

    declareWinner(player1_choice, player2_choice)

user_input = input("Welcome! shall we play a game? (type yes to play)\n")

while (user_input.lower() == "yes"):
    play_rps()
    user_input = input("Do you wand to go another round? (type yes to continue): ")
