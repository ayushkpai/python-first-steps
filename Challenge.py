pineapple = 4
zebra = 2

print("zebra < pineapple", zebra < pineapple)
print("zebra > pineapple", zebra > pineapple)
print("pineapple == zebra", pineapple == zebra)
print("pineapple == 3", pineapple == 3)
print("zebra == 2", zebra == 2)

ask_pineapple = int(input("How many pineapples are there? "))

if ask_pineapple == pineapple:
    print("You win")
else:
    print("Try again")

