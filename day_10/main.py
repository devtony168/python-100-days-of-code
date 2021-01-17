from replit import clear
from art import logo

#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(): 
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  end_of_calculation = False

  while not end_of_calculation: 
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    answer = input(f"Type 'y' to continue calculating with {first_answer}, or 'n' to start a new calculation: ")
    if answer == 'n':
      end_of_calculation = True
      clear()
      calculator()
    num1 = first_answer

calculator()