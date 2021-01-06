# main.py
# midnight rider
# a text adventure game that is riveting.
# IGN gives it 4 stars out of 100

import random
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
WIN = """
You pressed the button to open the gate.
This isn't the first time you've done this, so you know how to time it exactly.
Just as the doors close, you slide right into HQ
You know you did the right thing, the government would have just torn the car apart. 
They don't know its secrets... 
that it holds the key to different worlds 
As you step out of the vehicle, Fido runs up to you. 
"Thank you for saving me," he says.
As you take a couple steps away from the car makes a strange sound. 
It changes it shape. 
You've seen it before, but only on TV.
"....Bumblebee?"
"""

CHOICES = """ 
---
 A. Eat some tofu
 B. Drive at a moderate speed
 C. Speed ahead at full throttle 
 D. Stop for fie; a refuelling station  (no food available)
 Q. quit 
 E. Status check
 ---
 """
def type_text_output(text):
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

def main():
    type_text_output(INTRODUCTION)

    # CONSTANTS
MAX_FUEL_LEVEL = 50
MAX_TOFU_LEVEL = 3
MAX_DISTANCE_TRAVELLED = 100
    # Variable
done = False
km_traveled = 99     # 100km traveled is the goal
agents_distance = -20.0
turns = 0   # amount of turns taken
tofu = MAX_TOFU_LEVEL    # 3 is max tofu
fuel = MAX_FUEL_LEVEL   # 50 is a full tank
hunger = 0  # hunger increases with number
    # loop
while not done:
    # TODO: Random events
    # Fido
    if random.random() < 0.3:
        # Fido pops up says something and fills your tofu
        tofu = MAX_TOFU_LEVEL
        print()
        print("******** Your tofu is magically refilled")
        print("******** \"Your welcome!\" a voice says.")
        print("********* It's Fido.")
        print("******** He's using his tofu cooking skills")

    # TODO: Showing Hunger
    if hunger > 35:
        print("******** Your stomach rumbles. You need to eat something soon.")
    elif hunger > 20:
        print("******** Your hunger is small but manageable.")
        pass


        # TODO: check if reached END GAME
        if km_traveled > MAX_DISTANCE_TRAVELLED:
            # WIN
            # print out win scenario (typing way)
         time.sleep(2)
         type_text_output(WIN)
            # Break from while loop
        break


    elif hunger > 45:
    # TODO: lose - too hungry
    # print losing hunger scenario
     break


        # TODO: Give players their choices
    print(CHOICES)

        # Handle user's input
    users_choice = input("What do you want to do? ").lower().strip("!?.,")
    if users_choice == "a":
            # eat
          if tofu > 0:
                tofu -= 1
                hunger= 0
                print()
                print("------- mmmmmm soybean goodness ")
                print("-------- Your hunger is sated.")
        else:
                print()
                print("-------- You have none left")



        elif users_choice == "b":
            # drive moderately
            player_distance_now = random.randrange(7, 15)
            agents_distance_now = random.randrange(7, 15)
            # burn fuel
            fuel -= random.randrange(2, 6)
            # player distance travelled
            km_traveled += player_distance_now
            # agents distanced travelled
            agents_distance -= (player_distance_now - agents_distance_now)
            # player feedback
            print()
            print(f"--------- You just drove {player_distance_now} km now!")


        elif users_choice == "c":
            # drive fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)
            # burn fuel
            fuel -= random.randrange(5, 11)
            # player distanced travelled
            km_traveled += player_distance_now
            # agent distance travelled
            agents_distance -= (player_distance_now - agents_distance_now)
            # player feedback
            print()
            print(f"-------- You sped ahead {player_distance_now}kms!")
        elif users_choice == "d":
            # refuel
            # fill the fuel tank
            fuel = MAX_FUEL_LEVEL
            # consider the agents coming closer
            agents_distance += random.randrange(7, 15)
            # give user feedback
            print()
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer.")
            print()
        elif users_choice == "e":
            print(f"\t---status Check---")
            print(f"\tkm traveled: {km_traveled}")
            print(f"\tFuel left: {fuel}L")
            print(f"\tagents are: {abs(agents_distance)} kms behind you")
            print(f"\tYou have {tofu} tofu left")
            print("------\n")

        elif users_choice == "q":
            done = True

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)


        # Pause
        time.sleep(1)

    # TODO: change the environment based on choice and RNG

# outroduction
print("Thanks for playing")

if __name__ == '__main__':
    main()