print(f"This is a simple calculator. Let's start!")
num1 = int(input("Give me a number : "))
num2 = float(input("Give me a second number :  "))

while True:
    try:
        operation = input("Select an operation(+, -, *,  /) : ")
        if operation == "+":
            ans = num1 + num2
            
        elif operation == "-":
            ans = num1 - num2
        elif operation == "*":
            ans = num1 * num2
        elif operation == "/":
            ans = num1 / num2
        else:
            print ("Invalid Operation!")
            continue

        print(f"The result is {ans}")
        break
    except ValueError:
        print("Please enter valid numbers!")


