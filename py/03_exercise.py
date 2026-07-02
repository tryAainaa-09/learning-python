name = str(input("Enter your name: "))
height = float(input("Enter your height:  "))       #Convert to float

#validation
while True:
    try:
        #if height < 50:
        #    break
        #else:
        #    print("Give me a valid one yar, no one that's small")
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be positive!")
    except ValueError:
        print("Please enter a valid number!")


#output validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} centimeters tall.")
