################### Making Calculator(not tkinter) ####################

# multiplication
def multiply(a, b):
    return a * b


# addition
def add(a, b):
    return a + b


# subtraction
def subtract(a, b):
    return a - b


# devision
def divide(a, b):
    return a / b


print("SELECT OPERATION")
print("1.Multiplication")
print("2.Addition")
print("3.Subtraction")
print("4.Division")

while True:
    choice = input("Enter your choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            print(str("You have chose MULTIPLICATION"))

        elif choice == '2':
            print(str("You have chose ADDITION"))

        elif choice == '3':
            print(str("You have chose DIVISION"))

        elif choice == '4':
            print(str("You have chose DIVISION"))

        else:
            print("Invalid Input!")
            break


        if choice == '1':
            order1 = int(input("Enter your first number to Multiply: "))
            order2 = int(input("Enter your second number to Multiply: "))
            print(order1, "*", order2, "=", multiply(order1, order2))


        elif choice == '2':
            order3 = int(input("Enter your first number to Add: "))
            order4 = int(input("Enter your sencond number to Add: "))
            print(order3, "+", order4, "=", add(order3, order4))

        elif choice == '3':
            order5 = int(input("Enter your first number to Subtract: "))
            order6 = int(input("Enter your sencond number to Subtract: "))
            print(order5, "-", order6, "=", subtract(order5, order6))

        elif choice == '4':
            order7 = int(input("Enter your first number to Divide: "))
            order8 = int(input("Enter your sencond number to Divide: "))
            print(order7, "/", order8, "=", divide(order7, order8))


        choice2 = input("To continue press 1: ")

        if choice2 == '1':
            continue
        else:
            break

        break
    else:
        print("Invalid Input")

