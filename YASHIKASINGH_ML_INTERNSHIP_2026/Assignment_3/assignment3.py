#ASSIGNMENT 3
# Q1: Function to print first 10 natural numbers
def print_natural_numbers():
    for i in range(1, 11):
        print(i)
print("First 10 Natural Numbers:")
print_natural_numbers()
# Q2: Function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    print("Sum =", sum)
n = int(input("\nEnter N: "))
sum_natural_numbers(n)
# Q3: Function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print("Reverse number =", rev)
num = int(input("\nEnter a number to reverse: "))
reverse_number(num)
# Q4: Function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    print("Number of digits =", count)
num = int(input("\nEnter a number to count digits: "))
count_digits(num)
# Q5: Function to check palindrome number
def is_palindrome(num):
    original_num = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if original_num == rev:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
num = int(input("\nEnter a number to check for palindrome: "))
is_palindrome(num)
# Q6:  Function to generate Fibonacci series
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci series up to", n, ":")
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b
n = int(input("\nEnter the limit for Fibonacci series: "))
fibonacci_series(n)

# Q7: Calculator using Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("\nCalculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    print("Result =", divide(a, b))
else:
    print("Invalid Choice")

# Q8:  Create a text file and store student details
file = open("student.txt", "w")

name = input("\nEnter student name: ")
roll_no = input("Enter roll number: ")
marks = input("Enter marks: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details stored successfully.")

# Q9: Read data from a file
file = open("student.txt", "r")
print("\nStudent Details from file:")
for line in file:
    print(line, end='')
file.close()

# Q10: Handle division by zero using exception handling
try:
    a = int(input("\nEnter first number for division: "))
    b = int(input("Enter second number for division: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# Q11: Create a Student class with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


name = input("\nEnter student name for class: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)

print("\nStudent Details using Class:")
s1.display()