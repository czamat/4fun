# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program untilt he user wants to exit


def add(a, b):
  answer = a + b
  print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
  answer = a - b
  print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
  answer = a * b
  print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
  answer = a / b
  print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
  print("A. Addition")
  print("B. Subtraction")
  print("C. Multiplication")
  print("D. Division")
  print("E. Exit")

  choice = input("Input your choice: ")

  if choice == "A" or choice == "a":
    print("Addition")
    a = int(input("Input first number here: "))
    b = int(input("Input second number here: "))
    add(a, b)

  elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("Input first number here: "))
    b = int(input("Input second number here: "))
    sub(a, b)

  elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("Input first number here: "))
    b = int(input("Input second number here: "))
    mul(a, b)

  elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("Input first number here: "))
    b = int(input("Input second number here: "))
    div(a, b)

  elif choice == "e" or choice == "E":
    print("Program ended")
    quit()