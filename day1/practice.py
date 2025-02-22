# Write a program to find the greatest of three numbers:
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if num1 > num2 and num1 > num3:
    print(num1, "is greater number")
elif num2>num1 and num2 > num3:
    
    print(num2, "is greater number")
elif num3 > num1 and num3 > num2:
    print(num3, "is greater")
else:
    print("All three are equal numbers")
    
# ------------------------------------------------------------------------------------------------

# check if a year is leap or not:

year = int(input("Enter a year to check leap or not"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
    print(f"{year} is a Leap Year")
else: 
    print(f"{year} is not a Leap Year")

# ------------------------------------------------------------------------------------------------

# grade of a student based on the marks they score:

marks = int(input("Enter marks"))
if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 80 and marks <=89:
    print("Grade B")
elif marks >= 70 and marks <=79:
    print("Grade C")
elif marks < 70:
    print("Fail")
else:
    print("Not a number")

# --------------------------------------------------------------------------------------------

# program to check if three sides length form a valid triangle:

a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the length of side 3: "))
if (a+b) > c and (b+c) > a and (a+c) > b:
    print("It will form a valid triangle")
else:
    print("It will not form a valid triangle")