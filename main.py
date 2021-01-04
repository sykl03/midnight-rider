# main.py
# midnight rider
# a text adventure game that is riveting.
# IGN gives it 4 stars out of 100

import textwrap
import time
import sys


INTRODUCTION = """

WELCOME TO MIDNIGHT RIDER 

WE HAVE STOLEN A CAR. WE NEED TO GET IT HOME. THE CAR I SPECIAL:

THE GOVERNMENT WANTS IT FOR THEIR GAIN/ 

WE CANNNOT LET THAT HAPPEN 

ONE GOAL: SURVIVAL ... AND THE CAR. 
REACH THE END BEFORE THE MAN GON GETCHU

"""

CHOICES = """ 
---
 Q. quit 
 E. Status check
 ---
 """
def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    intro()
    # Variable
    done = False
    km_traveled = 0     # 100km traveled is the goal
    agents_distance = -20.0
    turns = 0   # amount of turns taken
    tofu = 3    # 3 is max tofu
    fuel = 50   # 50 is a full tank
    hunger = 0  # hunger increases with number
    # loop
    while not done:
        pass

        # TODO: check if reached END GAME
        # TODO: Give players their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!?.,")
        if users_choice == "e":
            print(f"\t---status Check---")
            print(f"\tkm traveled: {km_traveled}")
            print(f"\tFuel left: {fuel}L")
            print(f"\tagents are: {abs(agents_distance)} kms behind you")
            print(f"\tYou have{tofu} tofu left")
            print("------\n")

        if users_choice == "q":
            done = True

        # Pause
        time.sleep(1)

    # TODO: change the environment based on choice and RNG

# outroduction
print("Thanks for playing")

if __name__ == '__main__':
    main()