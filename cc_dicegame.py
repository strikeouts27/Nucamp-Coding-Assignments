import random
from secrets import choice
from turtle import Turtle

high_score = 0
player_choice = True

while player_choice:
    print("Welcome to Dice Game!")
    print("Current High Score: ", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    player_choice = input("Enter your choice:")
    if player_choice == "1":
        dicethrow_one = random.randint(1, 6)
        dicethrow_two = random.randint(1, 6)
        total_dicethrow = dicethrow_one + dicethrow_two
        print("You roll a..."), print(dicethrow_one)
        print("You roll a... "), print(dicethrow_two)
        print("You have rolled a total of:", total_dicethrow)
        if total_dicethrow > high_score:
            high_score = total_dicethrow
            print(total_dicethrow)
            print(
                "Congratulations you have set a new record! \n Would you like to try to beat that high score?")
    if player_choice == "2":
        print("Thank you for playing! Goodbye!")
        break

        '''elif total_dicethrow <= high_score:
            continue_question = input(
                "Would you like to try again and beat the high score?")
                if continue_question == 1:
                else: continue_question == 2:
                break
            if continue_question == "2":
                print("Thank you for playing!")
                break
    elif player_choice == "2":
        print("The gaming software will now exit. Thank you for playing!")
        break
dice_game()
# I learned that you can create a while loop using the boolean true value.
# Doing so will cause an infinite loop because there is nothing that would make it false!
# Be sure to make an exit!'''
