import os
import time
"""
For the best experience, it should be run in terminal
by typing python<path for the Achilleus-turtle_race>
"""


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
