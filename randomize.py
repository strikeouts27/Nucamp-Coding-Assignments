import random
# allows me to access the random module built in by python.
pips = random.randint(1, 6)
# set a variable to pips and pick a random integer between one and six.
print("You roll the die... it lands with", pips, "pips showing.")

# choice method
prizes = ["a car", "10,000", "a pony", "$500000"]
prize_won = random.choice(prizes)
print("You turn the wheel of fortune... It lands on a prize of", prize_won + "!!")
# string concatenation with ,'s will add things togather with a space. Adding with a + will not add a space.

# shuffle method
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print("The cards are now in this order: ")
print(cards)
