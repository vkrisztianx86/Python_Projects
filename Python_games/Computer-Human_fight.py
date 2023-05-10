import random

points_to_win = 5
points_of_human = 0
points_of_computer = 0

round = 0

while points_of_computer != points_to_win and points_of_human != points_to_win:
    round += 1
    computer_roll = random.randint(1, 6)
    human_roll = random.randint(1, 6)
    print(f'{round}. round!')
    print(f'Stat: C = {points_of_computer}, H = {points_of_human}')
    print(f'Computer --> {computer_roll} Human --> {human_roll}')
    print()

    if human_roll == computer_roll:
        print('Draw! New Roll!')
    elif human_roll > computer_roll:
        print('This round is won by the Human.')
        points_of_human += 1
    else:
        print('This round is won by the Computer.')
        points_of_computer += 1

    print('-' * 50)  # For the visual separation of rounds

if points_of_human > points_of_computer:
    print(f'Congratulations, the human won in the {round}. round!')
else:
    print(f'We got a problem Houston, the Computer won in the {round}. round!')
