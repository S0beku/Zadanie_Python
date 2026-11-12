import random
import math


### 1. Interactive and Script Modes
def BMI():
    height = input('Enter your height in cm: ')
    weight = input('Enter your weight in kg: ')
    height = int(height)
    weight = int(weight)
    bmi = weight / (height/100)**2
    bmi = round(bmi,2)
    print('Your BMI is', bmi)
    print('Check on the Internet if your BMI is ok!!')

def DiceFiveRolls():
    print("Dice rolling simulator")
    for i in range(5):
        dice_roll = random.randint(1,6)
        print(dice_roll, end=" ")

### 3. Variables
def addthree():
    number1 = 71
    number2 = 14
    number3 = 66
    result = number1 + number2 + number3
    print('Number 1: ', number1)
    print('Number 2: ', number2)
    print('Number 3: ', number3)
    print('The result of summation: ', result)

def swapval():
    x = 7
    y = 34
    z = 0 
    print("Before swapping: x=", x, "y=", y)
    z = x
    x = y
    y = z
    print("After swapping: x=", x, "y=", y)

def KMtoM():
    speed_kmh = 70
    speed_ms = (speed_kmh * 1000) / 3600
    print(speed_kmh, "km/h = ", speed_ms, "m/s")

def DiagRect():
    a = 5
    b = 10
    diagonal = math.sqrt(a**2 + b**2)
    print("Diagonal of rectangle with sides equal to ", a, " and ", b, " is equal to ", diagonal)

def Population():
    total = 8000000000
    north = 7200000000
    south = total - north
    print("World population: ", total)
    print("Northern Hemisphere: ", north)
    print("Northern Hemisphere in %: ", north/total*100)
    print("Southern Hemisphere: ", south)
    print("Southern Hemisphere in %: ", south/total*100)

def Avg():
    math = 5
    art = 4
    music = 5
    history = 3
    average = math + art + music + history / 4
    print("Average grade is", average)

### 4. Output Formatting
def Introduction():
    name = "Adam"
    age = 18
    height = 180
    agein6 = age + 6
    print(f"My name is {name}.\n I am {age} years old, and my height is {height} cm.\n In 6 years I will be {agein6} years old.")

def Income():
    father_income = 5450
    mother_income = 4920
    family_members = 5
    total_income = father_income + mother_income
    income_per_person = total_income/family_members
    print(f'Total family income is {total_income}, and income per person is {income_per_person}')

def Equations():
    a = 3
    b = 5
    print(f'{a}+{b}={a+b}')
    print(f'{a}-{b}={a-b}')
    print(f'{a}*{b}={a*b}')
    print(f'{a}/{b}={a/b}')

### 5. Data Input
def IntroInput():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = first_name + ' ' + last_name
    print(f'Your first name is {first_name} and your last name is {last_name}')
    print(f'And your full name is {full_name}')

def Cube():
    cube_side_string = input('Enter cube side: ')
    cube_side = int(cube_side_string)
    cube_volume = cube_side**3
    cube_surface_area = (cube_side**2)*6
    print(f'The volume of a cube with side {cube_side} is {cube_volume}')
    print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')

def Cuboid():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    volume = a*b*c
    area = (a*b)*2 + (a*c)*2 + (b*c)*2
    print(f'Cuboid with sides {a}, {b}, {c} has volume {volume} and area {area}')

def Vat():
    amount = float(input('Amount='))
    vat = amount/100 * 23
    print(f'Vat of {amount} is equal to {vat}')

def Discount():
    price = float(input('Price='))
    discount = int(input('Discount='))
    reduction = price/100*discount
    total = price - reduction
    print(f'Price is {price}, Discount is {discount}, so reduction is {reduction} and total will be {total}')

### 6. String Operations
def Charinname():
    name = 'Anna'
    surname = 'May'
    characters_in_name = len(name)
    fullname = name + " " + surname
    print(f'Your name has {characters_in_name} characters')
    print(f'Your surname has {len(surname)} characters')
    print(f'Your full name has {len(fullname)}')

def Initials():
    name = 'George'
    surname = 'Bush'
    print(name[0] + surname[0])  

def Abbrevation():
    university = "Krakow University of Economics"
    words = university.split()
    print(words[0][0] + words[1][0] + words[3][0])

def EmployeeInfo():
    employee = "Mr. John May, born on 1998-02-16"
    print(f'Name: {employee[4:8]}')
    print(f'Surname: {employee[9:12]}')
    print(f'Born: {employee[22:]}')
    print(f'Initials: {employee[4]+employee[9]}')

def Phone():
    phone = input('Enter phone number: ')
    chunks = [phone[i:i+3] for i in range(0, len(phone), 3)]
    print(f'{chunks[0]}-{chunks[1]}-{chunks[2]}')

def NumRepresentation():
    print(f'a {ord('a')}')
    print(f'b {ord('b')}')
    print(f'z {ord('z')}')
    print(f'A {ord('A')}')
    print(f'B {ord('B')}')
    print(f'Z {ord('Z')}')
    print(f'1 {ord('1')}')
    print(f'= {ord('=')}')
    print(f'+ {ord('+')}')
    print(f'€ {ord('€')}')

def NameNumRep():
    name = 'Grzegorz'
    for char in name:
        print(f'The letter {char} has a code {ord(char)}')

def CharInBetween():
    first = input('Enter first letter: ')
    last = input('Enter last letter: ')
    first_letter_code = ord(first)
    last_letter_code = ord(last)
    number_of_letters = (last_letter_code - first_letter_code + 1) * -1 if (last_letter_code - first_letter_code + 1) < 0 else (last_letter_code - first_letter_code - 1)
    print(f'Between {first} and {last} is {number_of_letters} letters')

def WordFromChar():
    print(chr(67),chr(111),chr(111),chr(108),chr(33),)

def StringManipulation():
    movie = "The Lord of the Rings: The Return of the King"
    print('Number of characters: ', len(movie))
    print("Upper case: ", movie.upper())
    print("Lower case: ", movie.lower())
    print("Number of 'e' in movie ", movie.count("e"))
    print("Lord in the text is at ", movie.find("Lord"))
    print("Dragon in the text is at ", movie.find("dragon"))

### 7. Binary Operations
def DoesTax():
    age = int(input('Enter age: '))
    no_tax = age < 26
    print(f'Exemption from paying taxes: {no_tax}')

def PassValid():
    password = input('Enter password: ')
    password_ok = len(password) >= 8
    print(f'Password length is valid: {password_ok}')

def Even():
    number = int(input('Enter number: '))
    even = number%2==0
    print(f'Number is even: {even}')

def TreeCanCut():
    circumference = int(input("Enter tree circumference in cm: "))
    tree_ok = circumference / math.pi>=50
    print(f'Tree can be cut down: {tree_ok}')

def FromKrakow():
    car_number = input('Enter car registration number')
    is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"
    print(f'Car is from Krakow: {is_krakow}')

def SpeedValid():
    speed = int(input("Enter vehicle speed: "))
    speed_valid = speed > 40 and speed < 140
    print(f'Speed is valid: {speed_valid}')

def Rng():
    for i in range(0,5):
        random_number = random.randint(5,10)
        print(random_number)

def DiceThreeRolls():
    dice_roll_1 = random.randint(1,6)
    dice_roll_2 = random.randint(1,6)
    dice_roll_3 = random.randint(1,6)

    total = dice_roll_1 + dice_roll_2 + dice_roll_3
    print(f'First dice: {dice_roll_1}\n Second dice: {dice_roll_2}\n Third dice: {dice_roll_3}\n Total: {total}')

def Dicev2():
    roll = random.randint(1,6)
    is_special = roll==1 or roll==6
    print(f'Dice rolled: {roll}\n Special number (1 or  6): {is_special}')

def GameRNG():
    computer = random.randint(1,6)
    you = int(input('Choose a number from 1 to 6: '))
    win = computer == you
    print(f'You won: {win}')

### 8. Practice Makes Perfect
def CircAndArea():
    r = int(input("Enter radius: "))
    area = 2 * r * math.pi
    circumference = r**2 * math.pi
    print(f'Area: {area}, Circumference: {circumference}')

def Temperature():
    celcius = int(input("Enter temperature in Celsius: "))
    fahrenheit = celcius * 1.8 + 32
    kelvin = celcius + 273.15
    print(f'Fahrenheit: {fahrenheit}, Kelvin: {kelvin}')

def CMtoInch():
    cm = 170
    calc = cm / 30.48
    feet = int(calc)
    inch = (calc - feet) * 12
    print(f'I am {cm}cm tall, i.e. {feet} feet and {inch} inches')

def SWIFT():
    swift = input('Enter swift: ')
    print(f'Bank Code: {swift[0:4]}\nCountry Code:{swift[4:6]}')

def CompanyExpenses():
    distance = int(input('Enter distance in km: '))
    fuel_price = float(input('Enter fuel price per liter: '))
    fuel_consumption = float(input('Enter fuel consumption per 100km: '))
    total_fuel_consumption = distance * (fuel_consumption/100)
    total_cost = total_fuel_consumption * fuel_price
    print(f'Total fuel consumption: {total_fuel_consumption}')
    print(f'Total cost: {total_cost}')

def Conversion():
    number = int(input("Enter a number: "))
    binary = bin(number)
    hexadecimal = hex(number)
    print(f'In binary this number is: {binary}\nIn hexadecimal this number is {hexadecimal}')

functions = {
    1: ("Interactive and Script Modes", {
        1: ("BMI", BMI),
        2: ("Dice", DiceFiveRolls)
    }),

    3: ("Variables", {
        1: ("addthree", addthree),
        2: ("swapval", swapval),
        3: ("KMtoM", KMtoM),
        4: ("DiagRect", DiagRect),
        5: ("Population", Population),
        6: ("Avg", Avg)
    }),

    4: ("Output Formatting", {
        1: ("Introduction", Introduction),
        2: ("Income", Income),
        3: ("Equations", Equations)
    }),

    5: ("Data Input", {
        1: ("IntroInput", IntroInput),
        2: ("Cube", Cube),
        3: ("Cuboid", Cuboid),
        4: ("Vat", Vat),
        5: ("Discount", Discount)
    }),

    6: ("String Operations", {
        1: ("Charinname", Charinname),
        2: ("Initials", Initials),
        3: ("Abbrevation", Abbrevation),
        4: ("EmployeeInfo", EmployeeInfo),
        5: ("Phone", Phone),
        6: ("NumRepresentation", NumRepresentation),
        7: ("NameNumRep", NameNumRep),
        8: ("CharInBetween", CharInBetween),
        9: ("WordFromChar", WordFromChar),
        10: ("StringManipulation", StringManipulation)
    }),

    7: ("Binary Operations", {
        1: ("DoesTax", DoesTax),
        2: ("PassValid", PassValid),
        3: ("Even", Even),
        4: ("TreeCanCut", TreeCanCut),
        5: ("FromKrakow", FromKrakow),
        6: ("SpeedValid", SpeedValid),
        7: ("Rng", Rng),
        8: ("Dice", DiceThreeRolls),
        9: ("Dicev2", Dicev2),
        10: ("GameRNG", GameRNG)
    }),

    8: ("Practice Makes Perfect", {
        1: ("CircAndArea", CircAndArea),
        2: ("Temperature", Temperature),
        3: ("CMtoInch", CMtoInch),
        4: ("SWIFT", SWIFT),
        5: ("CompanyExpenses", CompanyExpenses),
        6: ("Conversion", Conversion)
    })
}

def menu():

    print("\n===== MAIN MENU =====")

    for number, (section_name, section_functions) in functions.items():
        print(f"{number} - {section_name}")

    print("0 - Exit")

    try:
        section = int(input("\nChoose section: "))

        if section == 0:
            print("Goodbye!")
            return

        if section not in functions:
            print("Invalid section!")
            return menu()

        section_name, section_functions = functions[section]

        print(f"\n===== {section_name} =====")

        for number, (name, func) in section_functions.items():
            print(f"{number} - {name}")

        choice = int(input("\nChoose function: "))

        if choice not in section_functions:
            print("Invalid function!")
            return menu()

        name, func = section_functions[choice]

        print(f"\nRunning {name}...\n")

        func()

    except ValueError:
        print("Please enter a valid number!")
        return menu()

menu()