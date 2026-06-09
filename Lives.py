import random

words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]
secret_word = random.choice(words)
clue = list("?????")
heart_symbol = u"\u2764"
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

difficulty = int(input("Choose difficulty (type 1, 2 or 3)\n 1 easy\n 2 hard\n 3 very hard\n> "))

if difficulty == 1:
    lives = 8
elif difficulty == 2:
    lives = 4
else:
    lives = 2

print("""
Clues - every line represents one word
    yummy
    magic
    mouth
    body
    aquatic mammal
    bird
""")

while lives > 0:
    print(clue)
    print("Lives left: " + heart_symbol * lives)
    guess = input("Guess a letter or the whole word: ")

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
        if secret_word == "".join(clue):
            guessed_word_correctly = True
            break
    else:
        print("incorrect you lose a life")
        lives = lives - 1
