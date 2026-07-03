# for i in range(18):
#     if i == 4:
#         continue
#     if i == 10:
#         continue
#     if i == 14:
#         break
#     print(i)

################################

# for i in range(5):
#     for j in range(4):
#         if j == 2:
#             continue
#         print(f"({i}, {j})")

#################################
# print(f"This is a multiplication generator.")
# x = int(input("Enter a number: "))

# #count = 0
# #num = 0
# for count in range(1, 13):
#     print(f"{count} x {x} = {count * x}")

#################################

print(f"List all the prime numbers.")

count = 20
#prime_numbers = 0

for num in range(2, count + 1):
    is_prime = True
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

#print("Prime numbers up to 20:", prime_numbers)

