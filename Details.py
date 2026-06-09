class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)

p1 = Patient(input("What is your name? "), int(input("What is your age? ")))
p1.print_info()
