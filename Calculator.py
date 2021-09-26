#importing modules (time, random)
import time
import random

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


#Main conversation
print("Hi fellow human,")
time.sleep(1)
print("")
print("I am a simple calculator!")
time.sleep(1)
print("")
time.sleep(1)
print("Give me a try!")
time.sleep(1)
print(":)")

#Asks the user the operation the want to perform
operation = input("What operation do you want to peform (you will get answers of all operations)? MULTIPLICATION DIVISION ADDITION SUBTRACTION: ")

#Asks the user what the numbers are
first_num = float(input("Enter your first number!"))
last_num = float(input("Enter your second number!"))


#Fancy stuff
print("Generating usable data........")
time.sleep(0.5)
print("")
print("Getting output ready........")
time.sleep(0.5)
print("")

#Generates usable data for the operation and gives the answer

while True:
        if(operation=="MULTIPLICATION" or "Multiplication" or "multiplication"):
            
            operation = "multiplication"
            print(first_num,  "×",  last_num,  "=", multiply(first_num, last_num))
        elif(operation=="DIVISION" or "Division" or "division"):
        
            operation = "division"    
            print(first_num,  "/",  last_num,  "=", divide(first_num, last_num))
        elif(operation=="ADDITION" or "Addition" or "addition"):
        
            operation = "addition"      
            print(first_num,  "+",  last_num,  "=", add(first_num, last_num))
        elif(operation=="SUBTRACTION" or "Subtraction" or "subtraction"):
            
            operation = "subtraction"  
            print(first_num,  "-",  last_num,  "=", subtract(first_num, last_num))

#Last conversation   
print("")
print("Hope you enjoyed me!")
print("If you wish to use me again, just rerun the project!")
time.sleep(1)
print("")
print("Until then,")
time.sleep(1)
print("BYE!")
time.sleep(1)
print("")
print(":)")