def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

operations = {
  "+":addition,
  "-":subtraction,
  "*":multiply,
  "/":divide
}

num_1 = int(input("first num: "))
num_2 = int(input("second num: "))

for operation in operations:
  print(operation)

operation = input("pick an operation from above list of operatoins ")

calculation_function = operations[operation]
answer = calculation_function(num_1,num_2)

print(f"{num_1} {operation} {num_2} = {answer}")


