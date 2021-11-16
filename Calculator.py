#importing modules (time, random)
import time
import random

#This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

#Asks the user the operation the want to perform
operation = input("What operation do you want to peform? MULTIPLICATION DIVISION ADDITION SUBTRACTION: ").lower().strip()

#Asks the user what the numbers are
first_num = float(input("Enter your first number!"))
last_num = float(input("Enter your second number!"))

#Generates and gives the answer
if(operation=="multiplication"):
            
    print(first_num,  "×",  last_num,  "=", multiply(first_num, last_num))
elif(operation=="division"):
           
     print(first_num,  "/",  last_num,  "=", divide(first_num, last_num))
elif(operation=="addition"):
            
     print(first_num,  "+",  last_num,  "=", add(first_num, last_num))
elif(operation=="subtraction"):
            
     print(first_num,  "-",  last_num,  "=", subtract(first_num, last_num))
