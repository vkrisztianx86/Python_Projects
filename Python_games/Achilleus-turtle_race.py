import os
import time


class Achilleus_runner:
    def __init__(self, name):
        self.position = 0
        self.name = name

    def run(self, distance=10.0):
        self.position += distance
        print(' ' * int(self.position) + self.name[0])

runner_1 = Achilleus_runner('Achilleus')
runner_2 = Achilleus_runner('Turtle')
total_distance = 100

while True:
       os.system('cls')
       print('-' * total_distance)
       always_half_way = (total_distance - runner_1.position) / 2
       runner_1.run(distance=always_half_way)
       runner_2.run()

       print(f"{runner_1.name}'s position: {runner_1.position}")
       print(f"{runner_2.name}'s position: {runner_2.position}")

       if runner_1.position == total_distance or runner_2.position == total_distance:
           break

       time.sleep(1)

       # 4. feladat megoldása jöhet ide

       # points_to_win = 5
       # points_of_player = 0
       # points_of_computer = 0
       #
       # round = 0
       #
       # while points_of_computer != points_to_win and points_of_player != points_to_win:
       #     round += 1
       #     computer_roll = random.randint(1, 6)
       #     player_roll = random.randint(1, 6)
       #     print(f'{round}. forduló!')
       #     print(f'Aktuális állás: C = {points_of_computer}, P = {points_of_player}')
       #     print()
       #     print(f'Computer --> {computer_roll} Player --> {player_roll}')
       #
       #     if player_roll == computer_roll:
       #         print('Döntetlen! Új dobás!')
       #     elif player_roll > computer_roll:
       #         print('Ezt a fordulót a JÁTÉKOS nyerte.')
       #         points_of_player += 1
       #     else:
       #         print('Ezt a fordulót a COMPUTER nyerte.')
       #         points_of_computer += 1
       #
       #     print('-' * 50) # Csak hogy átláthatóbb legyen a kiíratás majd
       #
       # if points_of_player > points_of_computer:
       #     print('Éljen, a JÁTÉKOS nyert!')
       # else:
       #     print('Hát most a COMPUTER nyert.')