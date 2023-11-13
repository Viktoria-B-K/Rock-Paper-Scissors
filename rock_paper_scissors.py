import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_number = input('Chosee [r]ock, [p]aper, [s]cissors: ')

if player_number == 'r':
    player_move = rock
elif player_number == 'p':
    player_move = paper
elif player_number == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid input. Try again...')

computer_number = random.randint(1, 3)

computer_move = ''
if computer_number == 1:
    computer_move = rock
elif computer_number == 2:
    computer_move = paper
elif computer_number == 3:
    computer_move = scissors
print(f"The computer's choice is {computer_move}.")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print('You won!')
elif (computer_move == rock and player_move == scissors) or \
        (computer_move == paper and player_move == rock) or \
        (computer_move == scissors and player_move == paper):
    print('You lose!')
else:
    print('Draw!')