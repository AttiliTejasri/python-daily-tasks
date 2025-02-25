
# implement a menu-driven program where the user can
# choose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit
def find_square(num):
    return num ** 2

def find_cube(num):
    return num ** 3

while True:
    print("\nMenu:")
    print("1. Find the square of a number")
    print("2. Find the cube of a number")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        num = float(input("Enter a number: "))
        print(f"The square of {num} is {find_square(num)}")
    elif choice == '2':
        num = float(input("Enter a number: "))
        print(f"The cube of {num} is {find_cube(num)}")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        
# Print all numbers from 1 to 100 that are divisible by 3 and 5
# using a for loop
print("Numbers divisible by 3 and 5 from 1 to 100:")

for num in range(1, 101):  
    if num % 3 == 0 and num % 5 == 0:  
        print(num)
        
        
# Write a program to calculate the factorial of a number using
# a while loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    while n > 1:
        result *= n
        n -= 1  

    return result


num = int(input("Enter a number: "))

print(f"The factorial of {num} is {factorial(num)}")

# Check if a given number is a prime number using a for
# loop
def is_prime(n):
    if n < 2:
        return False  

    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False  

    return True 

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")