# Create a function to print first 10 natural numbers.
def naturalno(n):
    for i in range(11):
        print(i)
# function call
naturalno(10)

# Create a function to calculate sum of first N natural numbers.
def sum(n):
    s = 0
    for i in range(n+1):
        s+=i
    print("Sum of first n natural no. is",s)
# function call
sum(11)

# Create a function to reverse a number
def reverse(n):
    s = 0
    while n>0:
        digit = n % 10
        s = s*10 + digit
        n = n // 10
    return s
# function call
print(reverse(123456))

# Create a function to count digits in a number.
def count(n):
    s = 0
    while n>0:
        s+=1
        n = n // 10
    return s
# function call
print(count(12345))

# Create a function to check palindrome number.
def palindrome(n):
    original = n
    s = 0
    while n>0:
        digit = n % 10
        s = s*10 + digit
        n = n // 10
    return original == s
# function call
print(palindrome(123)) 

# Create a function to generate Fibonacci series.
def fib(n):
    d1 = 0
    d2 = 1
    print(d1,end=",")
    print(d2,end=",")
    s = n-2
    while s>0:
        d3 = d1 + d2
        print(d3,end=",")
        d1 = d2 
        d2 = d3
        s-=1
# function call
fib(8)


# calculater using function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:
    case 1:
        result = add(num1, num2)
    case 2:
        result = subtract(num1, num2)
    case 3:
        result = multiply(num1, num2)
    case 4:
        result = divide(num1, num2)
    case _:
        result = "Invalid choice"

print("Result =", result)

# Create a text file and store student details.
with open("student.txt","w") as file:
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    file.write("Name: " + name + "\n")
    file.write("Roll No: " + roll + "\n")
    file.write("Course: " + course + "\n")
print("Student details saved successfully.")

# Read data from a file.
with open("student.txt", "r") as file:
    data = file.read()
    print(data)

# Handle division by zero using exception handling. 
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Program execution completed.")

# Create a Student class with name and marks. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s1 = Student("Angel", 95)
s2 = Student("Rahul", 88)
s1.display()
print()
s2.display()