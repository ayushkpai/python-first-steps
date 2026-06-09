import random
import string
check_guess = 0

while True:
    adjectives = ["sleepy", "slow", "smelly",
    "wet", "fat", "red",
    "orange", "yellow", "green",
    "blue", "purple", "fluffy",
    "white", "proud", "brave"]

    nouns = ["apple", "dinosaur", "ball",
    "toaster", "goat", "dragon",
    "hammer", "duck", "panda"]

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print("Your new password is: %s" % password)
    check_guess = password
    response = input("Would you like another password? Type [Y/n]: ")
    if response == "n":
        break
