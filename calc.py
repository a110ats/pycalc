from time import sleep as sl
print("@A110ATS")
while True:
    sl(2)
    print("\nEnter 'add' to add two numbers\n\nEnter 'subtract' to subtract two numbers\n\nEnter 'multiply' to multiply two numbers\n\nEnter 'divide' to divide two numbers\n\nOr, Enter 'quit' to Terminate the program...\n\n")
    user = input(": ")

    if user == "quit" or 'terminate' or 'exit':
        break
    elif user == 'add':
        num1 = float(input("Input a Number: "))
        num2 = float(input("Input another Number: "))
        rslt = int(num1 + num2)
        sl(0.75)
        print("\nAnswer: %s\n_____________" % rslt)
    elif user == 'subtract':
        num1 = float(input("Input a Number: "))
        num2 = float(input("Input another Number: "))
        rslt = int(num1 - num2)
        sl(0.75)
        print("\nAnswer: %s\n_____________" % rslt)
    elif user == 'multiply':
        num1 = float(input("Input a Number: "))
        num2 = float(input("Input another Number: "))
        rslt = int(num1 * num2)
        sl(0.75)
        print("\nAnswer: %s\n_____________" % rslt)
    elif user == 'divide':
        num1 = float(input("Input a Number: "))
        num2 = float(input("Input another Number: "))
        rslt = (num1 / num2)  # int in divide may raise an error
        sl(0.75)
        print("\nAnswer: %s\n_____________" % rslt)
    else:
        sl(1)
        print("UNKNOWN INPUT")
