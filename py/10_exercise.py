# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Sarah")  # Calling the function with an argument

#Function with return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

#print(greet("Sarah"))  

#Default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Burris "))  # Uses the default title
print(greet_with_title("John", "Dr."))  # Overrides the default title
