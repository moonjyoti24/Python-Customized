from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Moonjyoti's 1st Python Web Program to get the Square of any number you input!"

import math
# Take the number as input    
number = int(input('Enter a number to get its square '))
 
# Define a function to calculate Square
def calculateSquare(num):
    return num*num
 
# print the output
print("Square of ",number, "is ", calculateSquare(number))
