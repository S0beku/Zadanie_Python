# 07 - Arrays
# Section 1 - One dimensional arrays
 
import random
 
 
def arrays_1_4_print_array_elements():
    arr = [2, 3, 7, 5, 4]
 
    print("Array:", arr)
    print("Number of elements:", len(arr))
    print("First element:", arr[0])
    print("Second element:", arr[1])
    print("Last element:", arr[len(arr) - 1])
    print("Penultimate element:", arr[len(arr) - 2])
    print("Sum of first and last:", arr[0] + arr[len(arr) - 1])
    print("Middle element:", arr[len(arr) // 2])
    print("Elements:", *arr)
 
 
def arrays_1_5_modify_array():
    arr = [1, 2, 3, 4, 5]
 
    print("Original array:", arr)
 
    arr[0] = -1
    print("After changing first element:", arr)
 
    arr[-1] += 4
    print("After increasing last element:", arr)
 
    for i in range(1, len(arr) - 1):
        arr[i] *= 2
 
    print("After multiplying middle elements:", arr)
 
 
def arrays_1_6_weekday():
    def weekday(number):
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
 
        if 1 <= number <= 7:
            return days[number - 1]
 
        return "Invalid day number"
 
    for number in [1, 4, 7]:
        print(number, "-", weekday(number))
 
 
def arrays_1_7_shopping_list():
    shopping_list = [
        "milk",
        "bread",
        "eggs",
        "butter",
        "cheese",
        "tomatoes",
        "potatoes",
        "carrots",
        "onions",
        "garlic"
    ]
 
    print("Shopping list:")
 
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")
 
 
def arrays_1_8_computer_games():
    computer_games = [
        "The Witcher 3",
        "Minecraft",
        "Cyberpunk 2077",
        "Red Dead Redemption 2",
        "The Sims 4",
        "Grand Theft Auto V"
    ]
 
    computer_games.sort()
 
    print("Sorted games:")
 
    i = 0
    while i < len(computer_games):
        print(f"{i + 1}. {computer_games[i]}")
        i += 1
 
 
def arrays_1_9_license_plates():
    license_plates = [
        "KR12345",
        "WA12345",
        "KK98765",
        "PO12345",
        "KR54321",
        "GD12345",
        "KK45678"
    ]
 
    print("Plates starting with KR or KK:")
 
    counter = 1
 
    for plate in license_plates:
        if plate.startswith("KR") or plate.startswith("KK"):
            print(f"{counter}. {plate}")
            counter += 1
 
 
def arrays_1_10_test_results():
    test_results = [
        True, False, True, True, False,
        True, True, False, True, True
    ]
 
    total = len(test_results)
    correct = test_results.count(True)
    incorrect = test_results.count(False)
    percentage = correct / total * 100
 
    print("Number of questions:", total)
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print(f"Correct answers percentage: {percentage:.2f}%")
 
 
def arrays_1_11_march_temperature():
    temperatures = [
        5, 3, 2, 4, 6, 8, 7, 3, 1, 0,
        -2, -1, 2, 4, 5, 7, 9, 8, 6, 4,
        3, 1, -1, -3, 0, 2, 4, 6, 7, 5
    ]
 
    average = sum(temperatures) / len(temperatures)
    minimum = min(temperatures)
    maximum = max(temperatures)
    negative = sum(1 for temp in temperatures if temp < 0)
 
    print("Number of measurements:", len(temperatures))
    print(f"Average temperature: {average:.2f}")
    print("Minimum temperature:", minimum)
    print("Maximum temperature:", maximum)
    print("Number of negative temperatures:", negative)
 
 
def arrays_1_12_most_expensive_category():
    categories = [
        "Food",
        "Transport",
        "Rent",
        "Entertainment"
    ]
 
    expenses = [500, 150, 1000, 200]
 
    max_index = expenses.index(max(expenses))
 
    print("Most expensive category:", categories[max_index])
    print("Expense:", expenses[max_index])
 
 
def arrays_1_13_inventory_value():
    prices = [10, 5, 20, 15, 8, 12, 30, 7, 25, 18]
    quantities = [5, 10, 2, 4, 8, 3, 1, 6, 2, 5]
 
    total_value = 0
 
    for i in range(len(prices)):
        total_value += prices[i] * quantities[i]
 
    print("Total inventory value:", total_value)
 
 
def arrays_1_15_bubble_sort():
    def bubble_sort(arr):
        n = len(arr)
 
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
        return arr
 
    car_fuel_consumption = [8.5, 6.2, 9.1, 5.7, 7.3]
    bank_transactions = [120, -50, 300, -20, 80, -100]
 
    print("Car fuel consumption:")
    print(bubble_sort(car_fuel_consumption.copy()))
 
    print("Bank transactions:")
    print(bubble_sort(bank_transactions.copy()))
 
 
def arrays_1_16_builtin_sorting():
    distances = [120, 45, 300, 15, 90]
    daily_temperatures = [12, 18, 7, 21, 15, 9]
    file_names = [
        "document.pdf",
        "image.png",
        "notes.txt",
        "data.csv"
    ]
 
    print("Sorted distances:")
    print(sorted(distances))
 
    print("Temperatures descending:")
    print(sorted(daily_temperatures, reverse=True))
 
    print("Sorted file names:")
    print(sorted(file_names))
 
 
# Section 1 menu
 
def arrays_section_1_menu():
    tasks = {
        "4": arrays_1_4_print_array_elements,
        "5": arrays_1_5_modify_array,
        "6": arrays_1_6_weekday,
        "7": arrays_1_7_shopping_list,
        "8": arrays_1_8_computer_games,
        "9": arrays_1_9_license_plates,
        "10": arrays_1_10_test_results,
        "11": arrays_1_11_march_temperature,
        "12": arrays_1_12_most_expensive_category,
        "13": arrays_1_13_inventory_value,
        "15": arrays_1_15_bubble_sort,
        "16": arrays_1_16_builtin_sorting
    }
 
    print("\n--- One dimensional arrays ---")
 
    for number in tasks:
        print(number + ". " + tasks[number].__name__)
 
    choice = input("Choose a task: ")
 
    if choice in tasks:
        tasks[choice]()
    else:
        print("Invalid task number. Returning to main menu.")
 
 
# Section 2 - Two dimensional arrays
 
 
def arrays_2_2_tic_tac_toe():
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"]
    ]
 
    for row in board:
        print(" ".join(row))
 
 
def arrays_2_3_monthly_expenses():
    monthly_expenses = [
        [500, 200, 100],
        [450, 250, 120],
        [600, 180, 150],
        [550, 220, 130]
    ]
 
    categories = ["Food", "Transport", "Other"]
 
    print("Expenses by category:")
 
    for col in range(len(categories)):
        total = sum(row[col] for row in monthly_expenses)
        print(categories[col] + ":", total)
 
    print("\nExpenses by week:")
 
    for i, week in enumerate(monthly_expenses, start=1):
        print(f"Week {i}: {sum(week)}")
 
    total_monthly = sum(sum(week) for week in monthly_expenses)
 
    print("\nTotal monthly expenses:", total_monthly)
 
 
def arrays_2_4_meal_plan():
    meal_plan = [
        ["Oatmeal", "Chicken", "Salad"],
        ["Eggs", "Rice", "Fish"],
        ["Toast", "Pasta", "Soup"],
        ["Yogurt", "Chicken", "Vegetables"],
        ["Pancakes", "Rice", "Salad"],
        ["Sandwich", "Pizza", "Fruit"],
        ["Cereal", "Soup", "Pasta"]
    ]
 
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
 
    def weekday(number):
        if 1 <= number <= 7:
            return days[number - 1]
 
        return "Invalid day"
 
    def day_meal_plan(number):
        if 1 <= number <= 7:
            print("Meal plan for", weekday(number))
            print("Breakfast:", meal_plan[number - 1][0])
            print("Lunch:", meal_plan[number - 1][1])
            print("Dinner:", meal_plan[number - 1][2])
        else:
            print("Invalid day number.")
 
    for number in range(1, 8):
        day_meal_plan(number)
        print()
 
 
def arrays_2_5_cinema_seating():
    seats = [
        [True, True, False, True, False],
        [False, True, True, False, True],
        [True, False, True, True, False],
        [True, True, False, False, True],
        [False, True, True, True, False]
    ]
 
    total_seats = 0
    available_seats = 0
 
    for row in seats:
        for seat in row:
            total_seats += 1
 
            if seat:
                available_seats += 1
 
    reserved_seats = total_seats - available_seats
 
    print("Total seats:", total_seats)
    print("Available seats:", available_seats)
    print("Reserved seats:", reserved_seats)
 
    positions = [(1, 1), (5, 5), (3, 5)]
 
    for row, col in positions:
        if seats[row - 1][col - 1]:
            status = "Available"
        else:
            status = "Reserved"
 
        print(f"Seat ({row}, {col}): {status}")
 
 
def arrays_2_6_main_diagonal():
    matrix = [
        [2, 4, 6],
        [8, 10, 12],
        [14, 16, 18]
    ]
 
    print("Original matrix:")
 
    for row in matrix:
        print(row)
 
    for i in range(len(matrix)):
        matrix[i][i] = 1
 
    print("\nModified matrix:")
 
    for row in matrix:
        print(row)
 
 
# Section 2 menu
 
def arrays_section_2_menu():
    tasks = {
        "2": arrays_2_2_tic_tac_toe,
        "3": arrays_2_3_monthly_expenses,
        "4": arrays_2_4_meal_plan,
        "5": arrays_2_5_cinema_seating,
        "6": arrays_2_6_main_diagonal
    }
 
    print("\n--- Two dimensional arrays ---")
 
    for number in tasks:
        print(number + ". " + tasks[number].__name__)
 
    choice = input("Choose a task: ")
 
    if choice in tasks:
        tasks[choice]()
    else:
        print("Invalid task number. Returning to main menu.")
 
 
# Section 3 - Practice Makes Perfect
 
 
def practice_3_2_create_arrays():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = list(range(1, 11))
    arr3 = [0] * 10
    arr4 = [random.randint(1, 100) for _ in range(10)]
    arr5 = [4, 0, 3]
    arr6 = [0] * 15
    arr7 = [random.randint(1, 30) for _ in range(10)]
    arr8 = [random.randint(0, 1) for _ in range(20)]
    arr9 = [[False for _ in range(2)] for _ in range(5)]
 
    arrays = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]
 
    for i, arr in enumerate(arrays, start=1):
        print(f"arr{i}:", arr)
 
 
def practice_3_3_count_even_numbers():
    arr = [34, 7, 19, 4, 21, 8]
 
    count = 0
    i = 0
 
    while i < len(arr):
        if arr[i] % 2 == 0:
            count += 1
 
        i += 1
 
    print("Array:", arr)
    print("Even numbers:", count)
 
 
def practice_3_4_reverse_array():
    arr = [15, 8, 31, 47, 2, 19]
 
    print("Original:", arr)
    print("Reversed:", arr[::-1])
 
 
def practice_3_5_square_elements():
    arr = [8, 2, 5, 1, 9]
 
    squared = [number ** 2 for number in arr]
 
    print("Original:", arr)
    print("Squared:", squared)
 
 
def practice_3_6_min_max_without_builtin():
    arr = [-15, 8, -31, 47, -2, 19]
 
    minimum = arr[0]
    maximum = arr[0]
 
    for number in arr:
        if number < minimum:
            minimum = number
 
        if number > maximum:
            maximum = number
 
    print("Array:", arr)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
 
 
def practice_3_7_average_for_loop():
    arr = [15, 8, 31, 47, 2, 19]
 
    total = 0
 
    for number in arr:
        total += number
 
    average = total / len(arr)
 
    print("Average:", average)
 
 
def practice_3_8_average_while_loop():
    arr = [15, 8, 31, 47, 2, 19]
 
    total = 0
    i = 0
 
    while i < len(arr):
        total += arr[i]
        i += 1
 
    average = total / len(arr)
 
    print("Average:", average)
 
 
def practice_3_9_longest_name():
    names = [
        "Genowefa",
        "Onufry",
        "Celestyna",
        "Alojzy",
        "Pankracy"
    ]
 
    longest = names[0]
 
    for name in names:
        if len(name) > len(longest):
            longest = name
 
    print("Longest name:", longest)
 
 
def practice_3_10_star_function():
    def star(number):
        print("*" * number)
 
    for number in [2, 6, 4, 9, 7]:
        star(number)
 
 
def practice_3_11_compare_arrays():
    def compare(array1, array2):
        if array1 == array2:
            return True
 
        return False
 
    examples = [
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2], [1, 2, 3]),
        ([5, 6], [5, 6])
    ]
 
    for first, second in examples:
        print(first, second, "->", compare(first, second))
 
 
def practice_3_12_missing_numbers():
    array1 = [4, 36, 12, 28, 9, 44, 5]
    array2 = [5, 1, 36]
 
    missing = []
 
    for number in array1:
        if number not in array2:
            missing.append(number)
 
    print("Numbers missing from second array:", missing)
 
 
def practice_3_13_bubble_sort():
    def bubble_sort(arr):
        arr = arr.copy()
 
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
        return arr
 
    arrays = [
        [5, 2, 8, 1, 9],
        [10, 4, 7, 3, 6],
        [20, 15, 30, 5, 10]
    ]
 
    for arr in arrays:
        print("Original:", arr)
        print("Sorted:", bubble_sort(arr))
 
 
def practice_3_14_unique_elements():
    arr = [2, 3, 2, 5, 8, 1, 9, 8]
 
    unique = []
 
    for number in arr:
        if number not in unique:
            unique.append(number)
 
    print("Original:", arr)
    print("Unique:", unique)
 
 
def practice_3_15_occurs():
    def occurs(number, array):
        return number in array
 
    array = [15, 38, 7, 23, 14]
 
    try:
        number = int(input("Enter a number: "))
        print(occurs(number, array))
    except ValueError:
        print("Invalid input.")
 
 
def practice_3_16_single_element_tuple():
    value = ("computation",)
 
    print(value)
    print(type(value))
 
 
def practice_3_17_reverse_tuple():
    numbers = (10, 20, 30, 40, 50)
 
    print("Original:", numbers)
    print("Reversed:", numbers[::-1])
 
 
def practice_3_18_nested_tuple():
    data = ("Seven", [10, 20, 30], (5, 15, 25))
 
    print(data[0])
    print(data[1][2])
 
 
def practice_3_19_count_tuple_occurrences():
    numbers = (50, 20, 40, 50, 30, 50)
 
    try:
        value = int(input("Enter a number: "))
        print("Occurrences:", numbers.count(value))
    except ValueError:
        print("Invalid input.")
 
 
def practice_3_20_myarrays_functions():
    class MyArrays:
 
        @staticmethod
        def second_largest(arr):
            unique = sorted(set(arr))
 
            if len(unique) < 2:
                return None
 
            return unique[-2]
 
        @staticmethod
        def difference(arr):
            return max(arr) - min(arr)
 
        @staticmethod
        def median(arr):
            sorted_arr = sorted(arr)
            n = len(sorted_arr)
 
            if n % 2 == 1:
                return sorted_arr[n // 2]
 
            return (
                sorted_arr[n // 2 - 1] +
                sorted_arr[n // 2]
            ) / 2
 
        @staticmethod
        def min_max(arr):
            return [min(arr), max(arr)]
 
        @staticmethod
        def to_string(arr):
            return "-".join(str(number) for number in arr)
 
    numbers = [7, 3, 8, 5, 2]
 
    print("Array:", numbers)
    print("Second largest:", MyArrays.second_largest(numbers))
    print("Difference:", MyArrays.difference(numbers))
    print("Median:", MyArrays.median(numbers))
    print("Minimum and maximum:", MyArrays.min_max(numbers))
    print("String:", MyArrays.to_string(numbers))
 
 
def practice_3_21_count_greater():
    arr = [2.5, 7.8, 1.2, 9.4, 5.6]
 
    try:
        value = float(input("Enter a number: "))
 
        count = 0
 
        for number in arr:
            if number > value:
                count += 1
 
        print("Numbers greater than", value, ":", count)
 
    except ValueError:
        print("Invalid input.")
 
 
def practice_3_22_even_odd_separation():
    arr = [7, 4, 9, 2, 8, 3, 6, 1]
 
    even = []
    odd = []
 
    for number in arr:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
 
    result = even + odd
 
    print("Original:", arr)
    print("Even first, odd after:", result)
 
 
def practice_3_23_subset():
    array1 = [2, 4]
    array2 = [1, 2, 3, 4, 5]
 
    is_subset = True
 
    for number in array1:
        if number not in array2:
            is_subset = False
            break
 
    print("First array:", array1)
    print("Second array:", array2)
    print("Is subset:", is_subset)
 
 
def practice_3_24_random_element():
    def rand_elem(array):
        return random.choice(array)
 
    numbers = [10, 20, 30, 40, 50]
 
    print("Array:", numbers)
 
    for _ in range(5):
        print(rand_elem(numbers))
 
 
def practice_3_25_mytext_functions():
    class MyText:
 
        @staticmethod
        def count_words(text):
            return len(text.split())
 
        @staticmethod
        def longest_to_shortest(text):
            return sorted(
                text.split(),
                key=len,
                reverse=True
            )
 
        @staticmethod
        def alphabetical(text):
            return sorted(
                text.split(),
                key=str.lower
            )
 
    text = "An apple a day keeps the doctor away"
 
    print("Text:", text)
    print("Word count:", MyText.count_words(text))
    print("Longest to shortest:", MyText.longest_to_shortest(text))
    print("Alphabetical:", MyText.alphabetical(text))
 
 
def practice_3_26_matplotlib_line():
    try:
        import matplotlib.pyplot as plt
 
        x = [1, 8]
        y = [3, 10]
 
        plt.plot(x, y, marker="o")
        plt.title("Line from (1, 3) to (8, 10)")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()
 
    except ImportError:
        print("Install matplotlib using: python -m pip install matplotlib")
 
 
def practice_3_27_plot_function():
    try:
        import matplotlib.pyplot as plt
 
        x = list(range(-10, 11))
        y = [value ** 2 - 3 for value in x]
 
        plt.plot(x, y)
        plt.title("f(x) = x² - 3")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.show()
 
    except ImportError:
        print("Install matplotlib using: python -m pip install matplotlib")
 
 
def practice_3_28_plot_sine():
    try:
        import matplotlib.pyplot as plt
        import math
 
        degrees = list(range(0, 361))
        values = [math.sin(math.radians(x)) for x in degrees]
 
        plt.plot(degrees, values)
        plt.title("Sine function")
        plt.xlabel("Degrees")
        plt.ylabel("sin(x)")
        plt.grid(True)
        plt.show()
 
    except ImportError:
        print("Install matplotlib using: python -m pip install matplotlib")
 
 
def practice_3_29_print_2d_array():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
 
    for row in matrix:
        print(*row)
 
 
def practice_3_30_sum_last_column():
    matrix = [
        [7, 3, 7, 9, 0],
        [2, 9, 0, 1, 5],
        [3, 8, 6, 4, 7],
        [8, 7, 1, 1, 5]
    ]
 
    total = 0
 
    for row in matrix:
        total += row[-1]
 
    print("Sum of last column:", total)
 
 
def practice_3_31_create_2d_array():
    def create_2d_arr(x, y):
        return [[0 for _ in range(y)] for _ in range(x)]
 
    matrix = create_2d_arr(3, 5)
 
    for row in matrix:
        print(row)
 
 
def practice_3_32_multiplication_table():
    size = 5
 
    for i in range(1, size + 1):
        row = []
 
        for j in range(1, size + 1):
            row.append(i * j)
 
        print(*row)
 
 
def practice_3_33_matrix_min_max():
    matrix = [
        [-38, 19],
        [5, 40],
        [-7, 11],
        [29, 16]
    ]
 
    minimum = matrix[0][0]
    maximum = matrix[0][0]
 
    min_position = (0, 0)
    max_position = (0, 0)
 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
 
            if value < minimum:
                minimum = value
                min_position = (i, j)
 
            if value > maximum:
                maximum = value
                max_position = (i, j)
 
    print("Minimum:", minimum)
    print("Minimum position:", min_position)
 
    print("Maximum:", maximum)
    print("Maximum position:", max_position)
 
 
def practice_3_34_swap_rows():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
 
    print("Before:")
 
    for row in matrix:
        print(row)
 
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
 
    print("\nAfter:")
 
    for row in matrix:
        print(row)
 
 
def practice_3_35_swap_columns():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
 
    print("Before:")
 
    for row in matrix:
        print(row)
 
    for row in matrix:
        row[0], row[-1] = row[-1], row[0]
 
    print("\nAfter:")
 
    for row in matrix:
        print(row)
 
 
def practice_3_36_identity_matrix():
    def identity_matrix(n):
        matrix = []
 
        for i in range(n):
            row = []
 
            for j in range(n):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
 
            matrix.append(row)
 
        return matrix
 
    for size in [3, 5, 8]:
        print(f"\nIdentity matrix {size}x{size}:")
 
        for row in identity_matrix(size):
            print(row)
 
 
def practice_3_37_transpose_matrix():
    def transpose_matrix(matrix):
        return [
            [matrix[row][col] for row in range(len(matrix))]
            for col in range(len(matrix[0]))
        ]
 
    matrices = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10]
        ],
        [
            [5, 6, 7, 8]
        ]
    ]
 
    for matrix in matrices:
        print("\nOriginal:")
 
        for row in matrix:
            print(row)
 
        print("Transposed:")
 
        for row in transpose_matrix(matrix):
            print(row)
 
 
def practice_3_38_flatten_arrays():
    matrices = [
        [
            [2, 3],
            [1, 5]
        ],
        [
            [5, 0, 3, 7, 5],
            [9, 0, 9, 1, 2]
        ],
        [
            [2, 1],
            [3, 5],
            [7, 4],
            [2, 6]
        ]
    ]
 
    for matrix in matrices:
        flattened = []
 
        for row in matrix:
            for number in row:
                flattened.append(number)
 
        print("Original matrix:")
 
        for row in matrix:
            print(row)
 
        print("Flattened:", flattened)
        print()
 
 
# Section 3 menu
 
def arrays_section_3_menu():
    tasks = {
        "2": practice_3_2_create_arrays,
        "3": practice_3_3_count_even_numbers,
        "4": practice_3_4_reverse_array,
        "5": practice_3_5_square_elements,
        "6": practice_3_6_min_max_without_builtin,
        "7": practice_3_7_average_for_loop,
        "8": practice_3_8_average_while_loop,
        "9": practice_3_9_longest_name,
        "10": practice_3_10_star_function,
        "11": practice_3_11_compare_arrays,
        "12": practice_3_12_missing_numbers,
        "13": practice_3_13_bubble_sort,
        "14": practice_3_14_unique_elements,
        "15": practice_3_15_occurs,
        "16": practice_3_16_single_element_tuple,
        "17": practice_3_17_reverse_tuple,
        "18": practice_3_18_nested_tuple,
        "19": practice_3_19_count_tuple_occurrences,
        "20": practice_3_20_myarrays_functions,
        "21": practice_3_21_count_greater,
        "22": practice_3_22_even_odd_separation,
        "23": practice_3_23_subset,
        "24": practice_3_24_random_element,
        "25": practice_3_25_mytext_functions,
        "26": practice_3_26_matplotlib_line,
        "27": practice_3_27_plot_function,
        "28": practice_3_28_plot_sine,
        "29": practice_3_29_print_2d_array,
        "30": practice_3_30_sum_last_column,
        "31": practice_3_31_create_2d_array,
        "32": practice_3_32_multiplication_table,
        "33": practice_3_33_matrix_min_max,
        "34": practice_3_34_swap_rows,
        "35": practice_3_35_swap_columns,
        "36": practice_3_36_identity_matrix,
        "37": practice_3_37_transpose_matrix,
        "38": practice_3_38_flatten_arrays
    }
 
    print("\n--- Practice Makes Perfect ---")
 
    for number, function in tasks.items():
        print(number + ". " + function.__name__)
 
    choice = input("Choose a task: ")
 
    if choice in tasks:
        tasks[choice]()
    else:
        print("Invalid task number. Returning to main menu.")


def menu():
    sections = {
        "1": ("One dimensional arrays", arrays_section_1_menu),
        "2": ("Two dimensional arrays", arrays_section_2_menu),
        "3": ("Practice Makes Perfect", arrays_section_3_menu)
    }
 
    print("\n========== ARRAYS ==========")
 
    for number, (name, _) in sections.items():
        print(f"{number}. {name}")
 
    print("0. Exit")
 
    choice = input("\nChoose a section: ")
 
    if choice == "0":
        print("Goodbye!")
        return

    if choice in sections:
        sections[choice][1]()
    else:
        print("Invalid section number.")
 
 
if __name__ == "__main__":
    menu()