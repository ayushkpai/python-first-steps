def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry wrong answer. Try again ")
            attempt = attempt + 1

    if attempt == 3:
        print("The correct answer is " + answer)
score = 0

print("Guess the animal")
guess = input("Which one of these is a fish?\n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
Type A, B, C, or D ")
check_guess(guess, 'C')

guess = input("Which one of these is the fastest animal?\n \
A) Cheetah\n B) Rabbit\n C) Tiger\n D) Lion\n \
Type A, B, C, or D ")
check_guess(guess, 'A')

guess = input("Which is the largest animal?\n \
A) Elephant\n B) Blue Whale\n C) Dolphin\n D) None of these\n \
Type A, B, C, or D ")
check_guess(guess, 'B')

print("Your score is " + str(score))
