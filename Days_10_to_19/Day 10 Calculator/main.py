from replit import clear
from art import logo

#adding
def add(n1, n2):
  return n1 + n2

#subtracting
def subtract(n1,n2):
  return n1 - n2

#mulitplying
def multiple(n1,n2):
  return n1 * n2

#dividing
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiple,
  "/": divide
}


def calculator ():
  print(logo)
  num1 = float(input("Pick the first number?:\n"))
  
  for i in operations:
    print(i)
  yes_continue = True
  while yes_continue:
    operation_sym = input("Pick an operator:\n")
    num2 = float(input("What's the next number?:\n"))
    answer = operations[operation_sym](num1, num2)
    print(f"{num1} {operation_sym} {num2} = {answer}")
    response = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.\n")
    if response == 'n':
      yes_continue = False
      calculator()
    else:
      num1 = answer
      

calculator()
  
