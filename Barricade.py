number = int(input("What is your favourite number? "))
if number == 1:
    int(input("Please choose a number greater than 1 "))
else:
    name = input("What is your name? ")

    for counter in range(1, number):
        print(f"{ name }'s room keep out!!!")    
