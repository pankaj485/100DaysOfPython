from replit import clear


def addition(num_1, num_2):
    return num_1 + num_2


def subtraction(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    return num_1 / num_2


operations = {"+": addition, "-": subtraction, "*": multiply, "/": divide}


def calculator():

    num_1 = float(input("first num: "))

    calculate_again = True

    while calculate_again:
        num_2 = float(input("second num: "))

        for operation in operations:
            print(operation)

        operation = input("pick an operation: ")

        calculation_function = operations[operation]
        answer = calculation_function(num_1, num_2)

        print(f"{num_1} {operation} {num_2} = {answer}")

        re_calc_option = input(
            " type y to do calculation with current answer \n type n to start new operation \n press any other key to exit: "
        )
        if re_calc_option == "y":
            num_1 = answer
        elif re_calc_option == "n":
            clear()
            calculator()
        else:
            calculate_again = False


calculator()
