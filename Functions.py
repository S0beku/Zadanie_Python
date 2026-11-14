import math
import random
 
 
# ============================================================
# 2. BUILT-IN FUNCTIONS
# ============================================================
 
def builtins_1_test_builtin_functions():
    print("Largest:", max(7, 5, 6, 3, 8, 2))
    print("Smallest:", min(4, 7, 2, 3, 9, 8))
    print("Length of 'computer science':", len("computer science"))
    letter = input("Enter a letter: ")
    print("Letter:", letter)
    print("Integer from '20303':", int("20303"))
    print("Binary representation of 304:", bin(304))
    print("Hexadecimal representation of 304:", hex(304))
    print("Unicode code of €:", ord("€"))
    print("Absolute value of -17:", abs(-17))
 
 
# ============================================================
# 3. USING MODULES
# ============================================================
 
def modules_1_math_module():
    print("Square root of 7:", math.sqrt(7))
    print("Natural logarithm of 5:", math.log(5))
    print("Sine of 90 degrees:", math.sin(math.radians(90)))
 
 
def modules_2_random_dice():
    print("Dice roll:", random.randint(1, 6))
 
 
# ============================================================
# 4. DEFINING A FUNCTION
# ============================================================
 
def defining_1_triangle_area():
    def triangle_area(a, b, c):
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The given sides do not form a triangle.")
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
 
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    print(f"Triangle area: {triangle_area(a, b, c):.2f}")
    for sides in [(3, 4, 5), (5, 12, 13), (7, 24, 25)]:
        print(f"Area for {sides}: {triangle_area(*sides):.2f}")
 
 
def defining_2_sum_digits():
    def sum_digits(number):
        return sum(int(digit) for digit in str(abs(number)))
 
    number = int(input("Enter an integer: "))
    print("Sum of digits:", sum_digits(number))
 
 
def defining_3_points_to_grade():
    def pts_to_grade(points):
        if points >= 18:
            return "Excellent"
        if points >= 14:
            return "Good"
        if points >= 10:
            return "Satisfactory"
        return "Fail"
 
    points = int(input("Enter points: "))
    print("Final grade:", pts_to_grade(points))
 
 
def defining_4_day_name():
    def day_name(day_number):
        days = {
            1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"
        }
        return days.get(day_number, "Invalid day number")
 
    number = int(input("Enter day number (1-7): "))
    print(day_name(number))
 
 
def defining_5_icao_spelling():
    icao = {
        "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta",
        "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
        "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima",
        "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
        "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
        "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
        "Y": "Yankee", "Z": "Zulu"
    }
    name = input("Enter a name: ").upper()
    print(" ".join(icao.get(char, char) for char in name))
 
 
def defining_6_time_string():
    def time_string(hours, minutes, time_format):
        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            raise ValueError("Invalid time.")
        if time_format == "24":
            return f"{hours:02d}:{minutes:02d}"
        if time_format == "12":
            suffix = "am" if hours < 12 else "pm"
            hour12 = hours % 12 or 12
            return f"{hour12}:{minutes:02d}{suffix}"
        raise ValueError("Format must be '12' or '24'.")
 
    tests = [
        (15, 38, "24"), (8, 3, "24"), (0, 5, "24"),
        (11, 15, "12"), (0, 7, "12"), (7, 30, "12"),
        (12, 46, "12"), (13, 10, "12"), (19, 2, "12")
    ]
    for h, m, fmt in tests:
        print(f"time_string({h}, {m}, '{fmt}') = {time_string(h, m, fmt)}")
 
 
# ============================================================
# 5. DIVIDING PROGRAM CODE INTO MODULES
# The worksheet asks for separate .py files. These menu versions
# keep the same functions in this file so every task can run alone.
# ============================================================
 
def modules_1_converters():
    def cm_to_inches(cm):
        return cm / 2.54
 
    def feet_inches_to_cm(feet, inches):
        return (feet * 12 + inches) * 2.54
 
    cm = float(input("Centimeters: "))
    print(f"{cm} cm = {cm_to_inches(cm):.2f} inches")
    feet = int(input("Feet: "))
    inches = float(input("Additional inches: "))
    print(f"{feet} ft {inches} in = {feet_inches_to_cm(feet, inches):.2f} cm")
 
 
def modules_2_keyboard_employee():
    def input_string(message):
        return input(message)
 
    def input_integer(message):
        return int(input(message))
 
    def input_real(message):
        return float(input(message))
 
    def input_boolean(message):
        return input(message).strip().lower() == "y"
 
    first_name = input_string("First name: ")
    last_name = input_string("Last name: ")
    age = input_integer("Age: ")
    salary = input_real("Salary: ")
    hide_salary = input_boolean("Hide salary? (y/n): ")
 
    print("\nEMPLOYEE RECORD")
    print("===============")
    print("Name:", first_name, last_name)
    print("Age:", age)
    if not hide_salary:
        print("Salary:", salary)
 
 
def modules_3_draw_square():
    import turtle
 
    def draw_square(length):
        for _ in range(4):
            turtle.forward(length)
            turtle.right(90)
 
    screen = turtle.Screen()
    screen.bgcolor("lightgreen")
    pen = turtle.Turtle()
    pen.speed(5)
    draw_square(100)
    pen.hideturtle()
    screen.mainloop()
 
 
def modules_4_draw_figures():
    import turtle
 
    def draw_square(length):
        for _ in range(4):
            turtle.forward(length)
            turtle.right(90)
 
    def draw_triangle(length):
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
 
    def draw_rectangle(length_a, length_b):
        for side in (length_a, length_b, length_a, length_b):
            turtle.forward(side)
            turtle.right(90)
 
    screen = turtle.Screen()
    screen.bgcolor("lightgreen")
    pen = turtle.Turtle()
    pen.speed(5)
 
    def move_to(x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
 
    move_to(-250, 100)
    draw_square(70)
    move_to(-100, 100)
    draw_square(100)
    move_to(50, 100)
    draw_triangle(90)
    move_to(180, 100)
    draw_triangle(110)
    move_to(-150, -100)
    draw_rectangle(120, 70)
    move_to(50, -100)
    draw_rectangle(90, 50)
 
    pen.hideturtle()
    screen.mainloop()
 
 
# ============================================================
# 7. PRACTICE MAKES PERFECT
# ============================================================
 
def practice_1_month_name():
    def month(n):
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return months[n - 1] if 1 <= n <= 12 else "Invalid month number"
 
    n = int(input("Enter month number: "))
    print(f"The name of month {n} is {month(n)}")
 
 
def practice_2_count_letter():
    def count_letter(text, letter):
        return text.lower().count(letter.lower())
 
    text = "You never get a second chance to make a first impression"
    letter = input("Letter to count (Enter for e): ") or "e"
    print(text)
    print(f"The number of letter '{letter}': {count_letter(text, letter)}")
 
 
def practice_3_number_in_range():
    def in_range(number, x, y):
        return x <= number <= y
 
    number = int(input("A number: "))
    x = int(input("Range start: "))
    y = int(input("Range end: "))
    print(f"Number {number} in the range <{x},{y}>: {'yes' if in_range(number, x, y) else 'no'}")
 
 
def practice_4_hide_card_number():
    def hide(card_number):
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Card number must contain exactly 16 digits.")
        return card_number[:2] + "*" * 10 + card_number[-4:]
 
    card = input("Enter 16-digit card number (default 5290312400019022): ") or "5290312400019022"
    print(hide(card))
 
 
def practice_5_valid_binary():
    def is_binary(binary_number):
        return len(binary_number) > 0 and all(char in "01" for char in binary_number)
 
    value = input("Enter a binary number: ")
    print(is_binary(value))
 
 
def practice_6_minimum_coins():
    def minimum_coins(amount_to_pay):
        if amount_to_pay < 0:
            raise ValueError("Amount cannot be negative.")
        count = 0
        for coin in (5, 2, 1):
            count += amount_to_pay // coin
            amount_to_pay %= coin
        return count
 
    amount = int(input("Amount to pay (PLN): "))
    print("Minimum number of coins:", minimum_coins(amount))
 
 
def practice_7_sum_even_or_odd_digits():
    def sum_selected_digits(number, even):
        digits = (int(d) for d in str(abs(number)))
        return sum(d for d in digits if (d % 2 == 0) == even)
 
    number = int(input("Enter an integer: "))
    even = input("Sum even digits? (y/n): ").strip().lower() == "y"
    print("Sum:", sum_selected_digits(number, even))
 
 
def practice_8_count_negative_even():
    def count_negative_even(x, y):
        return sum(1 for number in range(x, y + 1) if number < 0 and number % 2 == 0)
 
    x = int(input("Range start: "))
    y = int(input("Range end: "))
    if x > y:
        x, y = y, x
    print("Negative even numbers:", count_negative_even(x, y))
 
 
def practice_9_has_negative():
    def has_negative(n1, n2, n3):
        return n1 < 0 or n2 < 0 or n3 < 0
 
    numbers = [float(input(f"Number {i}: ")) for i in range(1, 4)]
    print(has_negative(*numbers))
 
 
def practice_10_asterisks_with_slashes():
    def asterisks(n):
        return "/".join("*" for _ in range(max(0, n)))
 
    n = int(input("Enter n: "))
    print(asterisks(n))
 
 
def practice_11_numbers_to_string():
    def numbers_to_string(n):
        return "".join(str(number) for number in range(1, max(0, n) + 1))
 
    n = int(input("Enter n: "))
    print(numbers_to_string(n))
 
 
def practice_12_calculator_function():
    def calculate(number1, number2, operator):
        if operator == "+":
            return number1 + number2
        if operator == "-":
            return number1 - number2
        if operator == "*":
            return number1 * number2
        if operator == "%":
            return number1 % number2
        if operator == "**":
            return number1 ** number2
        raise ValueError("Unsupported operator.")
 
    a = float(input("First number: "))
    b = float(input("Second number: "))
    operator = input("Operator (+, -, *, %, **): ")
    print("Result:", calculate(a, b, operator))
 
 
def practice_13_room_occupancy():
    def at_least_three_people(detector):
        people = 0
        maximum = 0
        for sign in detector:
            if sign == "+":
                people += 1
                maximum = max(maximum, people)
            elif sign == "-":
                people -= 1
                if people < 0:
                    raise ValueError("A person cannot leave an empty room.")
        return maximum >= 3
 
    detector = input("Enter detector sequence (+/-): ")
    print(at_least_three_people(detector))
 
 
def practice_14_fibonacci():
    def fibonacci(n):
        if n < 1:
            raise ValueError("n must be at least 1.")
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a
 
    n = int(input("Enter n: "))
    print(fibonacci(n))
 
 
def practice_15_palindrome():
    def is_palindrome(text):
        return text == text[::-1]
 
    text = input("Enter text: ")
    print(is_palindrome(text))
 
 
def practice_16_remove_spaces():
    def remove_spaces(sentence):
        return sentence.replace(" ", "")
 
    sentence = input("Enter a sentence: ")
    print(remove_spaces(sentence))
 
 
def practice_17_sum_repeated_digits():
    def sum_repeated_digits(number):
        digits = str(abs(number))
        return sum(int(digit) for digit in set(digits) if digits.count(digit) > 1)
 
    number = int(input("Enter an integer: "))
    print(sum_repeated_digits(number))
 
 
def practice_18_nth_prime():
    def nth_prime(n):
        if n < 1:
            raise ValueError("n must be at least 1.")
        found = 0
        candidate = 1
        while found < n:
            candidate += 1
            if all(candidate % divisor != 0 for divisor in range(2, int(math.sqrt(candidate)) + 1)):
                found += 1
        return candidate
 
    n = int(input("Which prime number (n): "))
    print(nth_prime(n))
 
 
def practice_19_difference_max_min():
    def difference(number1, number2, number3):
        return max(number1, number2, number3) - min(number1, number2, number3)
 
    values = [float(input(f"Number {i}: ")) for i in range(1, 4)]
    print("Difference:", difference(*values))
 
 
def practice_20_acronym():
    def acronym(name):
        return "".join(word[0].upper() for word in name.split() if word)
 
    name = input("Enter a name or phrase: ")
    print(acronym(name))
 
 
def practice_21_valid_password():
    def valid_password(password):
        return len(password) >= 6 and len(set(password)) == len(password)
 
    password = input("Enter password: ")
    print(valid_password(password))
 
 
def practice_22_evaluate_plus_minus():
    def evaluate(expression):
        if not expression:
            raise ValueError("Expression cannot be empty.")
        total = 0
        sign = 1
        for char in expression:
            if char == "+":
                sign = 1
            elif char == "-":
                sign = -1
            elif char.isdigit():
                total += sign * int(char)
            else:
                raise ValueError("Use only single digits, + and -.")
        return total
 
    expression = input("Enter expression (e.g. 2+3-4): ")
    print("Result:", evaluate(expression))
 
 
def practice_23_sum_divisible_numbers():
    def sum_numbers(x, y):
        if x > y:
            x, y = y, x
        return sum(number for number in range(x, y + 1)
                   if number % 2 == 0 and number % 3 == 0 and number % 4 != 0)
 
    x = int(input("Range start: "))
    y = int(input("Range end: "))
    print("Sum:", sum_numbers(x, y))
 
 
def practice_24_separate_characters():
    def separate_characters(text):
        return "-".join(text)
 
    text = input("Enter text: ")
    print(separate_characters(text))
 
 
def practice_25_validate_product_code():
    def valid_product_code(product_code):
        return (len(product_code) == 4 and product_code.isdigit()
                and int(product_code[3]) == sum(int(d) for d in product_code[:3]) % 7)
 
    code = input("Enter 4-digit product code: ")
    print(valid_product_code(code))
 
 
def practice_26_longest_dice_streak():
    def longest_dice_streak(dice):
        if not dice:
            return 0
        longest = current = 1
        best_value = dice[0]
        current_value = dice[0]
        for value in dice[1:]:
            if value == current_value:
                current += 1
            else:
                current_value = value
                current = 1
            if current > longest:
                longest = current
                best_value = current_value
        return best_value
 
    dice = input("Enter dice results (digits 1-6): ")
    if not dice or any(char not in "123456" for char in dice):
        print("Enter a non-empty sequence containing only digits 1-6.")
    else:
        print("Value with the longest consecutive streak:", longest_dice_streak(dice))
 
 
def practice_27_factorial_recursion():
    def factorial(n):
        if n < 0:
            raise ValueError("n cannot be negative.")
        if n <= 1:
            return 1
        return n * factorial(n - 1)
 
    n = int(input("Enter n: "))
    print(f"{n}! =", factorial(n))
 
 
def practice_28_sum_natural_recursion():
    def sum_natural(n):
        if n < 1:
            return 0
        return n + sum_natural(n - 1)
 
    n = int(input("Enter n: "))
    print("Sum from 1 to n:", sum_natural(n))
 
 
def practice_29_power_recursion():
    def power(x, n):
        if n < 0:
            return 1 / power(x, -n)
        if n == 0:
            return 1
        return x * power(x, n - 1)
 
    x = float(input("Enter base x: "))
    n = int(input("Enter exponent n: "))
    print("Result:", power(x, n))
 
 
# ============================================================
# MENU
# ============================================================
 
sections = {
    2: ("Built-in Functions", {
        1: ("Test built-in functions", builtins_1_test_builtin_functions),
    }),
    3: ("Using Modules", {
        1: ("Math module", modules_1_math_module),
        2: ("Random number / dice", modules_2_random_dice),
    }),
    4: ("Defining a Function", {
        3: ("Triangle area (Heron's formula)", defining_1_triangle_area),
        4: ("Sum of digits", defining_2_sum_digits),
        5: ("Points to grade", defining_3_points_to_grade),
        6: ("Day name", defining_4_day_name),
        7: ("ICAO phonetic alphabet", defining_5_icao_spelling),
        8: ("Time string", defining_6_time_string),
    }),
    5: ("Dividing Program Code into Modules", {
        2: ("Converters", modules_1_converters),
        3: ("Keyboard input and employee record", modules_2_keyboard_employee),
        4: ("Draw a square with turtle", modules_3_draw_square),
        5: ("Draw square, triangle and rectangle", modules_4_draw_figures),
    }),
    7: ("Practice Makes Perfect", {
        3: ("Month name", practice_1_month_name),
        4: ("Count a letter in text", practice_2_count_letter),
        5: ("Check whether number is in range", practice_3_number_in_range),
        6: ("Hide credit card number", practice_4_hide_card_number),
        7: ("Validate binary number", practice_5_valid_binary),
        8: ("Minimum number of coins", practice_6_minimum_coins),
        9: ("Sum even or odd digits", practice_7_sum_even_or_odd_digits),
        10: ("Count negative even numbers", practice_8_count_negative_even),
        11: ("Check whether any number is negative", practice_9_has_negative),
        12: ("Asterisks separated by slashes", practice_10_asterisks_with_slashes),
        13: ("Numbers from 1 to n as a string", practice_11_numbers_to_string),
        14: ("Calculator function", practice_12_calculator_function),
        15: ("Room occupancy detector", practice_13_room_occupancy),
        16: ("Nth Fibonacci value", practice_14_fibonacci),
        17: ("Check palindrome", practice_15_palindrome),
        18: ("Remove spaces from sentence", practice_16_remove_spaces),
        19: ("Sum repeated digits", practice_17_sum_repeated_digits),
        20: ("Nth prime number", practice_18_nth_prime),
        21: ("Difference between max and min", practice_19_difference_max_min),
        22: ("Acronym", practice_20_acronym),
        23: ("Validate password", practice_21_valid_password),
        24: ("Evaluate plus/minus expression", practice_22_evaluate_plus_minus),
        25: ("Sum numbers divisible by 2 and 3 but not 4", practice_23_sum_divisible_numbers),
        26: ("Separate characters with dashes", practice_24_separate_characters),
        27: ("Validate product code", practice_25_validate_product_code),
        28: ("Longest consecutive dice streak", practice_26_longest_dice_streak),
        29: ("Factorial using recursion", practice_27_factorial_recursion),
        30: ("Sum natural numbers using recursion", practice_28_sum_natural_recursion),
        31: ("Power using recursion", practice_29_power_recursion),
    }),
}
 
 
def menu():
    while True:
        print("\n========== FUNCTIONS ==========")
        for section_number, (section_name, _) in sections.items():
            print(f"{section_number}. {section_name}")
        print("0. Exit")
 
        try:
            section_choice = int(input("Choose section: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue
 
        if section_choice == 0:
            print("Goodbye!")
            return
 
        if section_choice not in sections:
            print("Invalid section number.")
            continue
 
        section_name, tasks = sections[section_choice]
        print(f"\n--- {section_name} ---")
        for task_number, (task_name, _) in tasks.items():
            print(f"{task_number}. {task_name}")
        print("0. Back to main menu")
 
        try:
            task_choice = int(input("Choose task: "))
        except ValueError:
            print("Invalid input. Returning to main menu.")
            continue
 
        if task_choice == 0:
            continue
 
        if task_choice not in tasks:
            print("Invalid task number. Returning to main menu.")
            continue
 
        task_name, task_function = tasks[task_choice]
        print(f"\nRunning: {task_name}\n")
        try:
            task_function()
        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)
        return
 
 
if __name__ == "__main__":
    menu()