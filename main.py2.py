# main.py
# Midnight Rider
# a text adventure game that is riveting.
# IGN gives it 4 stars out of 100

import random
import sys
import textwrap
import time

INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME. 
THE CAR IS SPECIAL

THE GOVERNMENT WANTS IT FOR THEIR GAIN

WE CAN'T LET THAT HAPPEN 

ONE GOAL: SURVIVAL... AND THE CAR.
REACH THE END BEFORE THE MAN GON GETCHU

"""

WIN = """ 

You pressed the button to open the gate. 
This isn't the first time you've done this, so you know how to time it exactly.
Just as the doors close, you slide right into HQ
You know you did the right thing, the government would have just torn the car apart.
They don't know it's secrets...
that it holds the key to different worlds
As you step out of the vehicle, Fido runs up to you.
"Thanks you for saving me," he says 
As you take a couple steps away from the car makes a strange sound.
It changes it shapes.
You've seen it before, but only on YV
"...Bumblebee?"
"""

LOSE_HUNGER = """
yYOUR STOMACH IS EMPTY.
WHO KNEW THAT WHAT THE DOCTOR SAID WAS TRUE. 
THAT HUMAN/ROBOT HYBRIDS WOULD NEED TOFU TO SUSTAIN THEMSELVES.
YOUR ROBOT SYSTEMS START TO SHUT DOWN
YOUR HUMAN EYES CLOSE
THE LAST THING THAT YOU HEAR ARE SIRENS.
THEY GOTCHU. THEY GOT THE CAR
WE FAILED... 
------ GAME OVER ------
"""

LOSE_AGENTS = """
THE AGENTS
"""


CHOICES = """
-----
A. Eat some tofu
B. Continue ahead at a moderate speed
C. Speed ahead at full throttle
D. Stop for fuel at refuelling station. (No food available)
E. Status check
Q. Quit
-----
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
    MAX_DISTANCE_TRAVELED = 100
    TOFU_CHANCE = 0.03

    # Variables
    done = False

    km_traveled = 0
    agents_distance = -20.0
    turns = 0
    tofu = MAX_TOFU_LEVEL
    fuel = MAX_FUEL_LEVEL
    hunger = 0

    while not done:
        # TODO: Random events
        # Fido
        if random.random() < TOFU_CHANCE:
            # Fido pops up says something and refills tofu
            tofu = MAX_TOFU_LEVEL
            print()
            print("****** Your tofu is magically refilled!")
            print("******\"you're welcome!\" a voice says.")
            print("****** It's Fido.")
            print("****** He's using his tofu cooking skillz.")

        # Check if reached END GAME
        if km_traveled > MAX_DISTANCE_TRAVELED:
            # WIN
            # Print out win scenario (typing way)
            time.sleep(2)
            type_text_output(WIN)
            break

        elif hunger > 45:
            # Lose - too hungry
            # print losing hunger scenario
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            break

        elif agents_distance >= 0:
            # LOSE - AGENTS REACHED YOU
            # print losing agents scenario
            time.sleep(2)
            type_text_output(LOSE_AGENTS)
            break

        elif fuel <= 0:
            #LOSE - RAN OUT OF FUEL
            pass
            # TODO; PRINT LOSE SCENARIO - FUEL
            break

        #Showing hunger
        if hunger > 35:
            print("***** Your stomach rumbles. You need to eat something soon.")
        elif hunger > 20:
            print("***** Your hunger is small but manageable.")



        # Give the player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do?").lower().strip("!,.?")

        if users_choice == "a":
            # eat
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- MMMMMMmmmm. Soybean goodness")
                print("--------- Your hunger is sated.")
                print()

            else:
                print()
                print("------- You have none left")
                print()

        elif users_choice == "b":
            # drive slow
            player_distance_now = random.randrange(7, 15)
            agents_distance_now = random.randrange(7, 15)

            # burn fuel
            fuel -= random.randrange(2, 7)

            # Player distance traveled
            km_traveled += player_distance_now

            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Feedback to player
            print()
            print(f"-------- You traveled {player_distance_now} kms!")
            print()

        elif users_choice == "c":
            # drive fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7 ,15)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # player distance traveled
            km_traveled += player_distance_now

            # agents distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)

            # feedback to player
            print()
            print(f"-------- you sped ahead {player_distance_now} kms!")
            print()

        elif users_choice == "d":
            # refuel
            # fill the fuel tank
            fuel = MAX_FUEL_LEVEL

            # consider the agents coming close
            agents_distance += random.randrange(7, 15)

            # give the user feedback
            print()
            print("--------- You filled the fuel tank")
            print("-------- The agents got closer...")
            print()

        elif users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkms traveled: {km_traveled} kms")
            print(f"\tFuel left: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms")
            print(f"\tYou have {tofu} tofu left")
            print("\t------\n")

        elif users_choice == "q":
            done = True

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)
            turns += 1

        # Pause
        time.sleep(1.2)

    # Outroduction
    print("Thanks for playing! Please play again :) ")
    print("You finished the game in {turns} turns.")

if __name__ == '__main__':
    main()