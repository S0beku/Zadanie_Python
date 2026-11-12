import random
import time


# ============================================================
# 1. DECISION STATEMENT
# Assignment numbers match the Control Structures worksheet.
# ============================================================

def decision_3_speed_limit():
    speed_limit = 140
    car_speed = int(input("Enter car speed (km/h): "))
    if car_speed > speed_limit:
        print(f"Your speed is {car_speed} km/h")
        print("Warning: speed limit exceeded!!")
    else:
        print("Speed limit not exceeded.")


def decision_4_payment_terminal():
    account_balance = 500
    total_payment = float(input("Enter total value of purchases: "))
    if total_payment <= account_balance:
        print("Payment completed")
        print(f"Remaining balance: {account_balance - total_payment:.2f} PLN")
    else:
        print("No funds")


def decision_5_test_passed():
    total_tasks = 20
    tasks_ok = int(input("Enter number of correctly completed tasks (0-20): "))
    test_passed = tasks_ok >= total_tasks * 0.5
    if test_passed:
        print("Congratulations! You passed the test.")
    else:
        print("Unfortunately, you failed the test.")


def decision_6_even_or_odd():
    number = int(input("Enter number: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


def decision_7_employee_salary():
    basic_salary = 5000
    bonus_percent = float(input("Enter bonus percentage (0 if no bonus): "))
    total_salary = basic_salary + basic_salary * bonus_percent / 100
    print(f"Basic salary: {basic_salary:.2f} PLN")
    print(f"Bonus: {bonus_percent:g}%")
    print(f"Total salary: {total_salary:.2f} PLN")


# ============================================================
# 2. MULTIPLE CONDITIONS
# ============================================================

def multiple_2_clothing_sizes():
    size = input("Enter size symbol (S/M/L/XL): ").strip().upper()
    if size == "S":
        print("S: Small size")
    elif size == "M":
        print("M: Medium size")
    elif size == "L":
        print("L: Large size")
    elif size == "XL":
        print("XL: Extra large size")
    else:
        print("Incorrect symbol")


def multiple_3_driving_modes():
    driving_mode = input("Enter driving mode (A/M/E): ").strip().upper()
    distance = float(input("Enter distance in km: "))
    if driving_mode == "A":
        fuel_consumption = 7
    elif driving_mode == "M":
        fuel_consumption = 9
    elif driving_mode == "E":
        fuel_consumption = 6
    else:
        print("Incorrect driving mode")
        return
    total_consumption = distance * fuel_consumption / 100
    print(f"Total fuel consumption over {distance:g} km in mode {driving_mode} is {total_consumption:g} liters")


def multiple_4_simple_calculator():
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operator = input("Enter operation (+, -, *, /): ").strip()
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 == 0:
            print("Cannot divide by zero")
            return
        result = number1 / number2
    else:
        print("Unknown operator")
        return
    print(f"{number1:g} {operator} {number2:g} = {result:g}")


def multiple_5_year_quarter():
    month = int(input("Enter month number (1..12): "))
    if month < 1 or month > 12:
        print("Invalid month")
        return
    if month >= 10:
        quarter = 4
    elif month >= 7:
        quarter = 3
    elif month >= 4:
        quarter = 2
    else:
        quarter = 1
    print(f"Month {month} is in quarter {quarter}")


def multiple_6_number_sign():
    number = float(input("Enter a number: "))
    if number > 0:
        print(f"Number {number:g} is positive")
    elif number < 0:
        print(f"Number {number:g} is negative")
    else:
        print("Number is 0")


# ============================================================
# 3. LOGICAL OPERATORS
# ============================================================

def logical_2_login_password():
    login = "joe"
    password = "abcd"
    entered_login = input("Login: ")
    entered_password = input("Password: ")
    if login == entered_login and password == entered_password:
        print("You are logged in")
    else:
        print("Incorrect login or password!!")


def logical_3_age_discount():
    age = int(input("Enter your age: "))
    if age < 18 or age >= 65:
        print("Discount available")
    else:
        print("No discount")


def logical_4_at_least_one_not_negative():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if not x < 0 or not y < 0:
        print(f"At least one of the numbers {x} and {y} is not negative")
    else:
        print("Both numbers are negative")


def logical_5_days_in_month():
    month = int(input("Enter month number (1..12): "))
    if month in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    elif month in (4, 6, 9, 11):
        days = 30
    elif month == 2:
        days = 28
    else:
        print("Invalid month")
        return
    print(f"Month {month} has {days} days")


def logical_6_valid_day_in_month():
    month = int(input("Enter month number (1..12): "))
    day = int(input("Enter the day number of the month: "))
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_days = 31
    elif month in (4, 6, 9, 11):
        max_days = 30
    elif month == 2:
        max_days = 28
    else:
        print("Invalid month")
        return
    if 1 <= day <= max_days:
        print(f"Day {day} for month {month} is correct")
    else:
        print(f"Day {day} for month {month} is incorrect")


# ============================================================
# 4. ITERATION OVER A SEQUENCE (FOR LOOPS)
# ============================================================

def iteration_3_practice_six_times():
    for i in range(6):
        print("Practice makes perfect!")


def iteration_4_university_spaced():
    university = "Krakow University of Economics"
    university_expanded = ""
    for char in university:
        university_expanded += char + " "
    print(university)
    print(university_expanded.rstrip())


def iteration_5_caesar_cipher():
    plain_text = "The early bird catches the worm"
    encrypted_text = ""
    for char in plain_text:
        if "a" <= char <= "y" or "A" <= char <= "Y":
            encrypted_text += chr(ord(char) + 1)
        elif char == "z":
            encrypted_text += "a"
        elif char == "Z":
            encrypted_text += "A"
        else:
            encrypted_text += char
    print("Original:", plain_text)
    print("Encrypted:", encrypted_text)


def iteration_6_sum_five_to_ten():
    total = 0
    for i in range(5, 11):
        total += i
    print(f"Sum is {total}")


def iteration_7_sum_even_one_to_ten():
    total = 0
    for i in range(1, 11):
        if i % 2 != 0:
            continue
        total += i
    print(f"Sum of even numbers in the range <1,10> is {total}")


def iteration_8_unit_fractions():
    for i in range(1, 11):
        print(f"1/{i} = {1 / i}")


# ============================================================
# 5. CONDITIONAL ITERATION (WHILE LOOPS)
# ============================================================

def conditional_3_greeting_nonempty_name():
    name = ""
    while name == "":
        name = input("Enter your name: ").strip()
    print(f"Hello {name}")


def conditional_4_guessing_game():
    number_to_guess = random.randint(1, 100)
    user_guess = 0
    print("Guess the number between 1 and 100!")
    while user_guess != number_to_guess:
        user_guess = int(input("Enter your guess: "))
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")


def conditional_5_sum_and_average_until_zero():
    total_sum = 0
    count = 0
    while True:
        number = int(input("Enter a number (0 to stop): "))
        if number == 0:
            break
        total_sum += number
        count += 1
    print(f"The total sum of the numbers is: {total_sum}")
    if count > 0:
        print(f"The arithmetic mean is: {total_sum / count}")
    else:
        print("No numbers were entered.")


def conditional_6_sum_even_using_while():
    n = int(input("Enter N: "))
    i = 1
    sum_even = 0
    while i <= n:
        if i % 2 == 0:
            sum_even += i
        i += 1
    print(f"The sum of even numbers from 1 to {n} is: {sum_even}")


def conditional_7_countdown_last_five_in_words():
    number = int(input("Enter countdown starting number: "))
    words = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}
    while number > 0:
        if number <= 5:
            print(words[number])
        else:
            print(number)
        number -= 1
    print("Zero!")


def conditional_8_atm_with_pin():
    pin = "1234"
    balance = 1000.0
    attempts = 0
    while attempts < 3:
        entered_pin = input("Enter PIN: ")
        if entered_pin == pin:
            break
        print("Incorrect PIN")
        attempts += 1
    else:
        print("Card blocked after three incorrect PIN attempts.")
        return

    while True:
        print("\\nATM MENU")
        print("1 - Check balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Check PIN")
        print("5 - Change PIN")
        print("0 - Exit ATM")
        choice = input("Choose option: ")

        if choice == "1":
            print(f"Balance: {balance:.2f} PLN")
        elif choice == "2":
            amount = float(input("Deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit completed")
            else:
                print("Amount must be positive")
        elif choice == "3":
            amount = float(input("Withdrawal amount: "))
            if 0 < amount <= balance:
                balance -= amount
                print("Withdrawal completed")
            else:
                print("Invalid amount or insufficient funds")
        elif choice == "4":
            print("PIN is set and contains four digits." if len(pin) == 4 and pin.isdigit() else "PIN is invalid")
        elif choice == "5":
            old_pin = input("Enter current PIN: ")
            if old_pin == pin:
                new_pin = input("Enter new 4-digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed")
                else:
                    print("PIN must contain exactly four digits")
            else:
                print("Incorrect current PIN")
        elif choice == "0":
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid option")


# ============================================================
# 6. PRACTICE MAKES PERFECT
# ============================================================

def practice_2_count_vowels_with_while():
    text = input("Enter text: ")
    vowels = "aeiouyAEIOUY"
    count = 0
    i = 0
    while i < len(text):
        if text[i] in vowels:
            count += 1
        i += 1
    print(f"Number of vowels: {count}")


def practice_3_house_lighting():
    light_switch1 = input("Switch 1 on? (y/n): ").strip().lower() == "y"
    light_switch2 = input("Switch 2 on? (y/n): ").strip().lower() == "y"
    bulbs_on = 0
    if light_switch1:
        bulbs_on += 1
    if light_switch2:
        bulbs_on += 2
    print(f"Number of bulbs illuminating the house: {bulbs_on}")


def practice_4_password_minimum_length():
    new_password = input("Enter new password: ")
    if len(new_password) < 12:
        print("Password too short (min. 12 chars)")
    else:
        print("Password length is valid")


def practice_5_thermometer():
    temperature = float(input("Enter temperature in Celsius: "))
    if temperature > 35:
        message = "It is extremely hot"
    elif temperature > 30:
        message = "It is hot"
    elif temperature >= 15:
        message = "It is warm"
    elif temperature >= 0:
        message = "It is cold"
    else:
        message = "Warning, frost"
    print(f"{temperature:g}°C: {message}")


def practice_6_parking_fee():
    hours = float(input("Enter number of parking hours: "))
    if hours <= 0:
        print("Parking time must be greater than zero")
    elif hours <= 2:
        fee = 5
        print(f"Parking fee: {fee} PLN")
    elif hours <= 6:
        fee = 15
        print(f"Parking fee: {fee} PLN")
    else:
        fee = 20
        print(f"Parking fee: {fee} PLN")


def practice_7_age_group():
    age = int(input("Enter your age: "))
    if age < 0:
        print("Invalid age")
    elif age < 13:
        print("Child")
    elif age <= 19:
        print("Teen")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")


def practice_8_both_people_adults():
    person1_name = input("Enter first person name: ")
    person1_age = int(input("Enter first person age: "))
    person2_name = input("Enter second person name: ")
    person2_age = int(input("Enter second person age: "))
    if person1_age >= 18 and person2_age >= 18:
        print(f"Both {person1_name} and {person2_name} are adults")
    else:
        print(f"Either {person1_name} or {person2_name} is not an adult")


def practice_9_polish_female_name():
    name = input("Enter name: ").strip()
    if name.lower().endswith("a"):
        print(f"{name} -- Polish female name")
    else:
        print(f"{name} does not end in 'a'")


def practice_10_dog_age():
    human_age = float(input("Enter the dog's age in human years: "))
    if human_age < 0:
        print("Age cannot be negative")
        return
    if human_age <= 2:
        dog_age = human_age * 10.5
    else:
        dog_age = 2 * 10.5 + (human_age - 2) * 4
    print(f"The dog's age in dog's years is {dog_age:g} years.")


def practice_11_price_reduction():
    previous_price = 200.0
    current_price = 140.0
    if previous_price <= 0:
        print("Previous price must be positive")
        return
    reduction = (previous_price - current_price) / previous_price * 100
    print(f"Current product price: {current_price:.2f}")
    print(f"Previous product price: {previous_price:.2f}")
    if reduction >= 10:
        print("Buy the product!!")
        print(f"Product price reduced by {reduction:.0f}%")
    else:
        print(f"Price reduction is {reduction:.0f}%; no purchase recommendation")


def practice_12_bulk_discount():
    count = int(input("Number of products purchased: "))
    price = float(input("Product price: "))
    if count < 0 or price < 0:
        print("Count and price cannot be negative")
        return
    total = 0
    for i in range(1, count + 1):
        if i > 2:
            total += price * 0.75
        else:
            total += price
    print(f"Amount to pay: {total:.2f}")


def practice_13_highway_speed():
    speed_limit_min = 40
    speed_limit_max = 140
    car_speed = int(input("Enter car speed: "))
    if car_speed < speed_limit_min or car_speed > speed_limit_max:
        print("Warning: invalid car speed!!")
    else:
        print("Car speed is valid")


def practice_14_influencer():
    facebook = input("Facebook account? (y/n): ").strip().lower() == "y"
    twitter = input("Twitter account? (y/n): ").strip().lower() == "y"
    instagram = input("Instagram account? (y/n): ").strip().lower() == "y"
    accounts = int(facebook) + int(twitter) + int(instagram)
    if accounts >= 2:
        print("You are a good influencer!")
    else:
        print("You are not a good influencer.")


def practice_15_ean13():
    ean = input("Enter EAN-13 article number: ").strip()
    if len(ean) == 13 and ean.isdigit():
        print("Article number is correct")
        if ean.startswith("590"):
            print("Article manufactured in Poland")
    else:
        print("Article number is incorrect")


def practice_16_washing_machine():
    program = input("Select washing program: (j)acket, (u)nderwear, (s)hoes: ").strip().lower()
    extra_rinse = input("Extra rinse? (y/n): ").strip().lower() == "y"
    extra_spin = input("Extra spin? (y/n): ").strip().lower() == "y"
    if program == "j":
        total_washing_time = 40
    elif program == "u":
        total_washing_time = 70
    elif program == "s":
        total_washing_time = 20
    else:
        print("Unknown washing program")
        return
    if extra_rinse:
        total_washing_time += 15
    if extra_spin:
        total_washing_time += 9
    print(f"Total washing time: {total_washing_time} minutes")


def practice_17_time_24_to_12():
    time_24 = input("Enter time (24-hour format, hh:mm): ").strip()
    try:
        hour_text, minute_text = time_24.split(":")
        hour = int(hour_text)
        minute = int(minute_text)
    except ValueError:
        print("Invalid time format")
        return
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        print("Invalid time")
        return
    suffix = "am" if hour < 12 else "pm"
    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12
    print(f"Time in 12-hour format: {hour_12}:{minute:02d}{suffix}")


def practice_18_coordinate_quadrant():
    x = float(input("x = "))
    y = float(input("y = "))
    if x == 0 and y == 0:
        location = "the origin (0,0)"
    elif x == 0:
        location = "the Y axis"
    elif y == 0:
        location = "the X axis"
    elif x > 0 and y > 0:
        location = "the first quadrant"
    elif x < 0 and y > 0:
        location = "the second quadrant"
    elif x < 0 and y < 0:
        location = "the third quadrant"
    else:
        location = "the fourth quadrant"
    print(f"Point P({x:g},{y:g}) is in {location} of the coordinate system")


def practice_19_three_question_survey():
    interested = input("Are you interested in computer science? (y/n): ").strip().lower() == "y"
    games = input("Do you like playing computer games? (y/n): ").strip().lower() == "y"
    instagram = input("Do you have an Instagram account? (y/n): ").strip().lower() == "y"
    print("\\nSURVEY RESULTS")
    print("Interested in computer science:", "Yes" if interested else "No")
    print("Playing computer games:", "Yes" if games else "No")
    print("Has an Instagram account:", "Yes" if instagram else "No")


def practice_20_decimal_to_binary_manual():
    number = int(input("Enter decimal number (non-negative): "))
    if number < 0:
        print("Please enter a non-negative integer")
        return
    if number == 0:
        binary = "0"
    else:
        remainders = ""
        value = number
        while value > 0:
            remainders += str(value % 2)
            value //= 2
        binary = remainders[::-1]
    print(f"{number}(10) = {binary}(2)")


def practice_21_minimum_coins():
    amount = int(input("Enter the amount in PLN: "))
    if amount < 0:
        print("Amount cannot be negative")
        return
    print(f"The amount of PLN {amount} in coins:")
    for coin in (5, 2, 1):
        count = amount // coin
        amount %= coin
        print(f"{coin} PLN coins: {count}")


def practice_22_three_five_bingo():
    for number in range(1, 31):
        if number % 3 == 0 and number % 5 == 0:
            print("BINGO", end=" ")
        elif number % 3 == 0:
            print("THREE", end=" ")
        elif number % 5 == 0:
            print("FIVE", end=" ")
        else:
            print(number, end=" ")
    print()


def practice_23_multiplication_table():
    number = int(input("Enter number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


def practice_24_star_diamond():
    for i in range(1, 6):
        print("* " * i)
    for i in range(4, 0, -1):
        print("* " * i)


def practice_25_repeated_digit_pattern():
    for i in range(1, 10):
        print(str(i) * i)


def practice_26_payment_card_pin():
    correct_pin = "0805"
    attempts = 0
    while attempts < 3:
        entered_pin = input("Enter the PIN code: ")
        if entered_pin == correct_pin:
            print("PIN correct. Payment card unlocked.")
            return
        print("Incorrect...")
        attempts += 1
    print("Sorry, your payment card has been blocked.")


def practice_27_numeric_keyboard_while():
    i = 6
    while i >= 0:
        j = 1
        while j <= 3:
            print(i + j, end=" ")
            j += 1
        print()
        i -= 3


def practice_28_fibonacci_first_twenty():
    first = 0
    second = 1
    for i in range(20):
        print(first, end=" ")
        first, second = second, first + second
    print()


def practice_29_first_n_primes():
    n = int(input("How many prime numbers should be printed? "))
    if n <= 0:
        print("Enter a number greater than zero")
        return
    found = 0
    candidate = 2
    print("Prime numbers:", end=" ")
    while found < n:
        is_prime = True
        divisor = 2
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            print(candidate, end=" ")
            found += 1
        candidate += 1
    print()


def practice_30_lottery_coupon():
    for row in range(1, 8):
        for column in range(7):
            number = row + column * 7
            print(number, end=" ")
        print()


def practice_31_twenty_random_numbers():
    for i in range(20):
        print(random.randint(5, 10), end=" ")
    print()


# ============================================================
# MENU
# Select a worksheet section, then its assignment number.
# Invalid menu input returns to the main menu.
# After an assignment runs, the program ends.
# ============================================================

functions = {
    1: ("Decision Statement", {
        3: ("Check motorway speed limit", decision_3_speed_limit),
        4: ("Credit card payment terminal", decision_4_payment_terminal),
        5: ("Check whether a test is passed", decision_5_test_passed),
        6: ("Check even or odd number", decision_6_even_or_odd),
        7: ("Calculate employee salary and bonus", decision_7_employee_salary),
    }),
    2: ("Multiple Conditions", {
        2: ("Clothing sizes", multiple_2_clothing_sizes),
        3: ("Car driving modes and fuel consumption", multiple_3_driving_modes),
        4: ("Simple calculator", multiple_4_simple_calculator),
        5: ("Quarter of the year", multiple_5_year_quarter),
        6: ("Positive, negative or zero", multiple_6_number_sign),
    }),
    3: ("Logical Operators", {
        2: ("Check login and password", logical_2_login_password),
        3: ("Age discount eligibility", logical_3_age_discount),
        4: ("At least one number is not negative", logical_4_at_least_one_not_negative),
        5: ("Number of days in a month", logical_5_days_in_month),
        6: ("Check if a calendar day is valid", logical_6_valid_day_in_month),
    }),
    4: ("Iteration Over a Sequence", {
        3: ("Print practice sentence six times", iteration_3_practice_six_times),
        4: ("Print university name with spaces", iteration_4_university_spaced),
        5: ("Caesar cipher (shift letters by one)", iteration_5_caesar_cipher),
        6: ("Sum numbers from 5 to 10", iteration_6_sum_five_to_ten),
        7: ("Sum even numbers from 1 to 10", iteration_7_sum_even_one_to_ten),
        8: ("Print fractions from 1/1 to 1/10", iteration_8_unit_fractions),
    }),
    5: ("Conditional Iteration", {
        3: ("Ask for a non-empty name", conditional_3_greeting_nonempty_name),
        4: ("Number guessing game", conditional_4_guessing_game),
        5: ("Sum and average numbers until zero", conditional_5_sum_and_average_until_zero),
        6: ("Sum even numbers using while", conditional_6_sum_even_using_while),
        7: ("Countdown with final five numbers in words", conditional_7_countdown_last_five_in_words),
        8: ("ATM with PIN check and PIN change", conditional_8_atm_with_pin),
    }),
    6: ("Practice Makes Perfect", {
        2: ("Count vowels using while", practice_2_count_vowels_with_while),
        3: ("House lighting with two switches", practice_3_house_lighting),
        4: ("Password minimum length", practice_4_password_minimum_length),
        5: ("Electronic thermometer", practice_5_thermometer),
        6: ("Parking fee calculator", practice_6_parking_fee),
        7: ("Age group", practice_7_age_group),
        8: ("Check whether two people are adults", practice_8_both_people_adults),
        9: ("Check Polish female name ending", practice_9_polish_female_name),
        10: ("Dog age conversion", practice_10_dog_age),
        11: ("Product price reduction recommendation", practice_11_price_reduction),
        12: ("Shopping discount for more than two products", practice_12_bulk_discount),
        13: ("Highway speed validation", practice_13_highway_speed),
        14: ("Good influencer (social media accounts)", practice_14_influencer),
        15: ("Validate EAN-13 and Polish origin", practice_15_ean13),
        16: ("Washing machine time calculator", practice_16_washing_machine),
        17: ("Convert 24-hour time to 12-hour time", practice_17_time_24_to_12),
        18: ("Find coordinate quadrant or axis", practice_18_coordinate_quadrant),
        19: ("Three-question survey", practice_19_three_question_survey),
        20: ("Convert decimal to binary manually", practice_20_decimal_to_binary_manual),
        21: ("Represent amount with fewest coins", practice_21_minimum_coins),
        22: ("THREE, FIVE and BINGO", practice_22_three_five_bingo),
        23: ("Multiplication table", practice_23_multiplication_table),
        24: ("Star pattern", practice_24_star_diamond),
        25: ("Repeated digit pattern", practice_25_repeated_digit_pattern),
        26: ("Payment card PIN with three attempts", practice_26_payment_card_pin),
        27: ("Numeric keyboard using while loops", practice_27_numeric_keyboard_while),
        28: ("First twenty Fibonacci numbers", practice_28_fibonacci_first_twenty),
        29: ("Find first N prime numbers", practice_29_first_n_primes),
        30: ("Lottery coupon", practice_30_lottery_coupon),
        31: ("Twenty random numbers from 5 to 10", practice_31_twenty_random_numbers),
    }),
}


def menu():
    while True:
        print("\\n========== MAIN MENU ==========")
        for section_number, (section_name, section_functions) in functions.items():
            print(f"{section_number} - {section_name}")
        print("0 - Exit")

        try:
            section_choice = int(input("\\nChoose section: "))
        except ValueError:
            print("Please enter a number. Try again.")
            continue

        if section_choice == 0:
            print("Goodbye!")
            return

        if section_choice not in functions:
            print("Section does not exist. Try again.")
            continue

        section_name, section_functions = functions[section_choice]
        print(f"\\n========== {section_name} ==========")
        for assignment_number, (assignment_name, function) in section_functions.items():
            print(f"{assignment_number} - {assignment_name}")

        try:
            assignment_choice = int(input("\\nChoose assignment number: "))
        except ValueError:
            print("Please enter a number. Returning to main menu.")
            continue

        if assignment_choice not in section_functions:
            print("Assignment does not exist. Returning to main menu.")
            continue

        assignment_name, selected_function = section_functions[assignment_choice]
        print(f"\\nRunning: {assignment_name}\\n")
        selected_function()
        return


if __name__ == "__main__":
    menu()