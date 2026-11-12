import random
import math


# ============================================================
# 1. INTERACTIVE AND SCRIPT MODES
# ============================================================

def interactive_1_bmi_calculator():
    height = input('Enter your height in cm: ')
    weight = input('Enter your weight in kg: ')
    height = int(height)
    weight = int(weight)
    bmi = weight / (height / 100) ** 2
    bmi = round(bmi, 2)
    print('Your BMI is', bmi)
    print('Check on the Internet if your BMI is ok!!')


def interactive_2_five_dice_rolls():
    print("Dice rolling simulator")
    for i in range(5):
        dice_roll = random.randint(1, 6)
        print(dice_roll, end=" ")


# ============================================================
# 3. VARIABLES
# ============================================================

def variables_2_add_three_numbers():
    number1 = 71
    number2 = 14
    number3 = 66
    result = number1 + number2 + number3
    print('Number 1: ', number1)
    print('Number 2: ', number2)
    print('Number 3: ', number3)
    print('The result of summation: ', result)


def variables_3_swap_values():
    x = 7
    y = 34
    z = 0
    print("Before swapping: x=", x, "y=", y)
    z = x
    x = y
    y = z
    print("After swapping: x=", x, "y=", y)


def variables_4_kmh_to_ms():
    speed_kmh = 70
    speed_ms = (speed_kmh * 1000) / 3600
    print(speed_kmh, "km/h = ", speed_ms, "m/s")


def variables_5_rectangle_diagonal():
    a = 5
    b = 10
    diagonal = math.sqrt(a ** 2 + b ** 2)
    print("Diagonal of rectangle with sides equal to ", a, " and ", b, " is equal to ", diagonal)


def variables_7_hemisphere_population():
    total = 8000000000
    north = 7200000000
    south = total - north
    print("World population: ", total)
    print("Northern Hemisphere: ", north)
    print("Northern Hemisphere in %: ", north / total * 100)
    print("Southern Hemisphere: ", south)
    print("Southern Hemisphere in %: ", south / total * 100)


def variables_8_average_grade():
    math_grade = 5
    art = 4
    music = 5
    history = 3
    average = (math_grade + art + music + history) / 4
    print("Average grade is", average)


# ============================================================
# 4. OUTPUT FORMATTING
# ============================================================

def formatting_1_student_introduction():
    name = "Adam"
    age = 18
    height = 180
    agein6 = age + 6
    print(f"My name is {name}.\n I am {age} years old, and my height is {height} cm.\n In 6 years I will be {agein6} years old.")


def formatting_2_family_income():
    father_income = 5450
    mother_income = 4920
    family_members = 5
    total_income = father_income + mother_income
    income_per_person = total_income / family_members
    print(f'Total family income is {total_income}, and income per person is {income_per_person}')


def formatting_3_arithmetic_equations():
    a = 3
    b = 5
    print(f'{a}+{b}={a + b}')
    print(f'{a}-{b}={a - b}')
    print(f'{a}*{b}={a * b}')
    print(f'{a}/{b}={a / b}')


# ============================================================
# 5. DATA INPUT
# ============================================================

def input_1_first_and_last_name():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = first_name + ' ' + last_name
    print(f'Your first name is {first_name} and your last name is {last_name}')
    print(f'And your full name is {full_name}')


def input_2_cube_volume_and_surface_area():
    cube_side_string = input('Enter cube side: ')
    cube_side = int(cube_side_string)
    cube_volume = cube_side ** 3
    cube_surface_area = (cube_side ** 2) * 6
    print(f'The volume of a cube with side {cube_side} is {cube_volume}')
    print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')


def input_3_cuboid_volume_and_surface_area():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    volume = a * b * c
    area = (a * b) * 2 + (a * c) * 2 + (b * c) * 2
    print(f'Cuboid with sides {a}, {b}, {c} has volume {volume} and area {area}')


def input_4_calculate_vat():
    amount = float(input('Amount='))
    vat = amount / 100 * 23
    print(f'Vat of {amount:.2f} is equal to {vat:.2f}')


def input_5_calculate_discount():
    price = float(input('Price='))
    discount = int(input('Discount='))
    reduction = price / 100 * discount
    total = price - reduction
    print(f'Price is {price:.2f}, Discount is {discount}, so reduction is {reduction:.2f} and total will be {total:.2f}')


# ============================================================
# 6. STRING OPERATIONS
# ============================================================

def strings_1_count_name_characters():
    name = 'Anna'
    surname = 'May'
    characters_in_name = len(name)
    fullname = name + " " + surname
    print(f'Your name has {characters_in_name} characters')
    print(f'Your surname has {len(surname)} characters')
    print(f'Your full name has {len(fullname)}')


def strings_2_print_initials():
    name = 'George'
    surname = 'Bush'
    print(name[0] + surname[0])


def strings_3_university_abbreviation():
    university = "Krakow University of Economics"
    words = university.split()
    print(words[0][0] + words[1][0] + words[3][0])


def strings_4_employee_information():
    employee = "Mr. John May, born on 1998-02-16"
    print(f'Name: {employee[4:8]}')
    print(f'Surname: {employee[9:12]}')
    print(f'Born: {employee[22:]}')
    print(f'Initials: {employee[4] + employee[9]}')


def strings_5_format_phone_number():
    phone = input('Enter phone number: ')
    if len(phone) != 9 or not phone.isdigit():
        print("Please enter exactly 9 digits.")
        return
    chunks = [phone[i:i + 3] for i in range(0, len(phone), 3)]
    print(f'{chunks[0]}-{chunks[1]}-{chunks[2]}')


def strings_6_character_numeric_representations():
    characters = ['a', 'b', 'z', 'A', 'B', 'Z', '1', '=', '+', '€']
    for char in characters:
        print(f'{char} {ord(char)}')


def strings_7_name_character_codes():
    name = 'Grzegorz'
    for char in name:
        print(f'The letter {char} has a code {ord(char)}')


def strings_8_count_letters_between():
    first = input('Enter first letter: ')
    last = input('Enter last letter: ')
    if len(first) != 1 or len(last) != 1:
        print("Please enter one character each.")
        return
    first_letter_code = ord(first.upper())
    last_letter_code = ord(last.upper())
    number_of_letters = abs(last_letter_code - first_letter_code) - 1
    print(f'Between {first} and {last} is {number_of_letters} letters')


def strings_9_character_codes_to_word():
    print(chr(67), chr(111), chr(111), chr(108), chr(33))


def strings_10_string_manipulation():
    movie = "The Lord of the Rings: The Return of the King"
    print('Number of characters: ', len(movie))
    print("Upper case: ", movie.upper())
    print("Lower case: ", movie.lower())
    print("Number of 'e' in movie ", movie.count("e"))
    print("Lord in the text is at ", movie.find("Lord"))
    print("Dragon in the text is at ", movie.find("dragon"))


# ============================================================
# 7. BINARY OPERATIONS
# ============================================================

def binary_1_check_tax_exemption():
    age = int(input('Enter age: '))
    no_tax = age < 26
    print(f'Exemption from paying taxes: {no_tax}')


def binary_2_check_password_length():
    password = input('Enter password: ')
    password_ok = len(password) >= 8
    print(f'Password length is valid: {password_ok}')


def binary_3_check_even_number():
    number = int(input('Enter number: '))
    even = number % 2 == 0
    print(f'Number is even: {even}')


def binary_4_check_tree_cutting_eligibility():
    circumference = int(input("Enter tree circumference in cm: "))
    tree_ok = circumference / math.pi >= 50
    print(f'Tree can be cut down: {tree_ok}')


def binary_5_check_krakow_registration():
    car_number = input('Enter car registration number: ').upper()
    is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"
    print(f'Car is from Krakow: {is_krakow}')


def binary_6_check_vehicle_speed():
    speed = int(input("Enter vehicle speed: "))
    speed_valid = speed > 40 and speed < 140
    print(f'Speed is valid: {speed_valid}')


def binary_7_generate_random_number():
    for i in range(0, 5):
        random_number = random.randint(5, 10)
        print(random_number)


def binary_8_roll_three_dice():
    dice_roll_1 = random.randint(1, 6)
    dice_roll_2 = random.randint(1, 6)
    dice_roll_3 = random.randint(1, 6)
    total = dice_roll_1 + dice_roll_2 + dice_roll_3
    print(f'First dice: {dice_roll_1}\nSecond dice: {dice_roll_2}\nThird dice: {dice_roll_3}\nTotal: {total}')


def binary_9_check_special_dice_number():
    roll = random.randint(1, 6)
    is_special = roll == 1 or roll == 6
    print(f'Dice rolled: {roll}\nSpecial number (1 or 6): {is_special}')


def binary_10_dice_guessing_game():
    computer = random.randint(1, 6)
    you = int(input('Choose a number from 1 to 6: '))
    win = computer == you
    print(f'You won: {win}')


# ============================================================
# 8. PRACTICE MAKES PERFECT
# ============================================================

def practice_1_circle_area_and_circumference():
    r = int(input("Enter radius: "))
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    print(f'Area: {area}, Circumference: {circumference}')


def practice_2_temperature_converter():
    celsius = int(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    kelvin = celsius + 273.15
    print(f'Fahrenheit: {fahrenheit}, Kelvin: {kelvin}')


def practice_3_convert_height_to_feet_inches():
    cm = 170
    calc = cm / 30.48
    feet = int(calc)
    inch = (calc - feet) * 12
    print(f'I am {cm}cm tall, i.e. {feet} feet and {inch} inches')


def practice_4_extract_swift_bank_and_country():
    swift = input('Enter swift: ')
    if len(swift) not in (8, 11):
        print("A SWIFT code should contain 8 or 11 characters.")
        return
    print(f'Bank Code: {swift[0:4]}')
    print(f'Country Code: {swift[4:6]}')


def practice_5_calculate_company_transport_cost():
    distance = int(input('Enter distance in km: '))
    fuel_price = float(input('Enter fuel price per liter: '))
    fuel_consumption = float(input('Enter fuel consumption per 100km: '))
    total_fuel_consumption = distance * (fuel_consumption / 100)
    total_cost = total_fuel_consumption * fuel_price
    print(f'Total fuel consumption: {total_fuel_consumption}')
    print(f'Total cost: {total_cost}')


def practice_6_decimal_to_binary_hexadecimal():
    number = int(input("Enter a number: "))
    binary = bin(number)
    hexadecimal = hex(number)
    print(f'In binary this number is: {binary}\nIn hexadecimal this number is {hexadecimal}')


# ============================================================
# FUNCTION MENU
# The menu uses section and assignment numbers from the worksheet.
# ============================================================

functions = {
    1: ("Interactive and Script Modes", {
        1: ("BMI Calculator", interactive_1_bmi_calculator),
        2: ("Five Dice Rolls", interactive_2_five_dice_rolls),
    }),

    3: ("Variables", {
        2: ("Add Three Numbers", variables_2_add_three_numbers),
        3: ("Swap Variable Values", variables_3_swap_values),
        4: ("Convert km/h to m/s", variables_4_kmh_to_ms),
        5: ("Rectangle Diagonal", variables_5_rectangle_diagonal),
        7: ("Hemisphere Population", variables_7_hemisphere_population),
        8: ("Average Grade", variables_8_average_grade),
    }),

    4: ("Output Formatting", {
        1: ("Student Introduction", formatting_1_student_introduction),
        2: ("Family Income", formatting_2_family_income),
        3: ("Arithmetic Equations", formatting_3_arithmetic_equations),
    }),

    5: ("Data Input", {
        1: ("First and Last Name", input_1_first_and_last_name),
        2: ("Cube Volume and Surface Area", input_2_cube_volume_and_surface_area),
        3: ("Cuboid Volume and Surface Area", input_3_cuboid_volume_and_surface_area),
        4: ("Calculate VAT", input_4_calculate_vat),
        5: ("Calculate Discount", input_5_calculate_discount),
    }),

    6: ("String Operations", {
        1: ("Count Name Characters", strings_1_count_name_characters),
        2: ("Print Initials", strings_2_print_initials),
        3: ("University Abbreviation", strings_3_university_abbreviation),
        4: ("Employee Information", strings_4_employee_information),
        5: ("Format Phone Number", strings_5_format_phone_number),
        6: ("Character Numeric Representations", strings_6_character_numeric_representations),
        7: ("Name Character Codes", strings_7_name_character_codes),
        8: ("Count Letters Between", strings_8_count_letters_between),
        9: ("Character Codes to Word", strings_9_character_codes_to_word),
        10: ("String Manipulation", strings_10_string_manipulation),
    }),

    7: ("Binary Operations", {
        1: ("Check Tax Exemption", binary_1_check_tax_exemption),
        2: ("Check Password Length", binary_2_check_password_length),
        3: ("Check Even Number", binary_3_check_even_number),
        4: ("Check Tree Cutting Eligibility", binary_4_check_tree_cutting_eligibility),
        5: ("Check Krakow Registration", binary_5_check_krakow_registration),
        6: ("Check Vehicle Speed", binary_6_check_vehicle_speed),
        7: ("Generate Random Numbers", binary_7_generate_random_number),
        8: ("Roll Three Dice", binary_8_roll_three_dice),
        9: ("Check Special Dice Number", binary_9_check_special_dice_number),
        10: ("Dice Guessing Game", binary_10_dice_guessing_game),
    }),

    8: ("Practice Makes Perfect", {
        1: ("Circle Area and Circumference", practice_1_circle_area_and_circumference),
        2: ("Temperature Converter", practice_2_temperature_converter),
        3: ("Convert Height to Feet and Inches", practice_3_convert_height_to_feet_inches),
        4: ("Extract SWIFT Bank and Country Codes", practice_4_extract_swift_bank_and_country),
        5: ("Calculate Company Transport Cost", practice_5_calculate_company_transport_cost),
        6: ("Decimal to Binary and Hexadecimal", practice_6_decimal_to_binary_hexadecimal),
    }),
}


def menu():
    while True:
        print("\n===== MAIN MENU =====")

        for section_number, (section_name, section_functions) in functions.items():
            print(f"{section_number} - {section_name}")

        print("0 - Exit")

        try:
            section = int(input("\nChoose section: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if section == 0:
            print("Goodbye!")
            return

        if section not in functions:
            print("Invalid section!")
            continue

        section_name, section_functions = functions[section]

        print(f"\n===== {section_name} =====")

        for assignment_number, (name, func) in section_functions.items():
            print(f"{assignment_number} - {name}")

        try:
            choice = int(input("\nChoose function: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice not in section_functions:
            print("Invalid function!")
            continue

        name, func = section_functions[choice]

        print(f"\nRunning {name}...\n")
        func()
        return


if __name__ == "__main__":
    menu()
