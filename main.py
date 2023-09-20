import math
import random


def mainMenu():
    print("Welcome to the main menu of CP12 ReviewProject, please select a number to access an area of the project")
    print("1. Data Caster")
    print("2. Grade Calculator")
    print("3. Number Gap Lister")
    print("4. Guessing Game")
    print("5. Number List Calculator")
    print("6. Create a Person (via Person class)")
    print("7. Calculate tax on an item")
    print("8. Exit Program")
    print("")
    selection = int(input("Input choice here: "))

    match selection:
        case 1:
            problemOne()
        case 2:
            problemTwo()
        case 3:
            problemThree()
        case 4:
            problemFour()
        case 5:
            problemFive()
        case 6:
            problemSix()
        case 7:
            problemSeven()


def problemOne():
    print("")
    selected_number = input('Input a number: ')
    print('Choose one of the following to cast to')
    print('1. String')
    print('2. Int')
    print('3. Float')
    choice = input()
    if choice == "1":
        casted_choice = str(selected_number)
        print(casted_choice + " is instanceOf: " + str(type(casted_choice)))
    elif choice == "2":
        casted_choice = int(selected_number)
        print(str(casted_choice) + " is instanceOf: " + str(type(casted_choice)))
    elif choice == "3":
        casted_choice = float(selected_number)
        print(str(casted_choice) + " is instanceOf: " + str(type(casted_choice)))

    print("")
    mainMenu()


def problemTwo():
    print("")
    grade_score = input('Input your grade score: ')
    score = int(grade_score)
    print("Your approximate letter grade: ")
    if score >= 86:
        print('A')
    elif score >= 73:
        print('B')
    elif score >= 60:
        print('C')
    elif score >= 50:
        print('D')
    elif score < 50:
        print('F')

    print("")
    mainMenu()


def problemThree():
    print("")
    starting_number = int(input("Choose a starting number: "))
    ending_number = int(input("Choose an ending number: "))
    gap = int(input("Choose a gap number: "))
    for i in range(starting_number, ending_number, gap):
        print(i)

    print("")
    mainMenu()


def problemFour():
    print("")
    random_number = random.randint(1, 10)
    num_guessed = False
    while not num_guessed:
        guess = int(input("There's a random number between one and 10, try to guess it! : "))
        if guess == random_number:
            print("You guessed the number!")
            num_guessed = True
            print("")
            mainMenu()


def problemFive():
    print("")
    numbers = []
    adding_numbers = True
    while adding_numbers:
        number_to_add = input("Enter a number or type stop to stop")
        if type(number_to_add) == str and number_to_add == 'stop':
            print(numbers)
            maximum = max(numbers)
            minimum = min(numbers)
            sum_of_num = sum(numbers)
            total_numbers = len(numbers)
            average = sum_of_num / total_numbers
            print(maximum)
            print(minimum)
            print(average)
            adding_numbers = False
        else:
            numbers.append(int(number_to_add))


def problemSix():
    print("")
    print("Welcome to create a person")
    name = input("Input their name: ")
    age = int(input("Input their age: "))
    quote = input("Input their favorite quote (Without quotation marks) : ")

    users_person = Person(age, name, quote)

    print("Your persons name: " + users_person.get_name())
    print("Your persons age: " + str(users_person.get_age()))
    print("Your persons favourite quote: " + users_person.get_favorite_quote())

    print("")
    mainMenu()


class Person:

    def __init__(self, age: int, name: str, favorite_quote: str):
        self._age = age
        self._name = name
        self._favorite_quote = favorite_quote

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_favorite_quote(self):
        return self._favorite_quote


def problemSeven():
    print("")
    item_cost = input("Enter the total of your item ($): ")
    tax = input("Enter tax amount (%) : ")
    tax_multiplier = int(tax) * 0.01 + 1
    total = int(item_cost) * tax_multiplier
    print("Your item after tax is: $" + str(total))
    choice = input("Would you like to see how much of this item you can afford? (Y/N) : ")
    if choice == "Y" or choice == "y":
        bank_balance = float(input("Enter your bank balance ($) : "))
        amount = math.floor(bank_balance / total)
        print("You can afford " + str(amount))
        print('')
        mainMenu()
    else:
        print('')
        mainMenu()


mainMenu()