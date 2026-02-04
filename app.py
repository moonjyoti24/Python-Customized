from flask import Flask
import os
import math

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Moonjyoti's 1st Python Web Program to get the Square of any number you input!"

# Take the number as input    
number = int(input('Enter a number to get its square '))
 
# Define a function to calculate Square
def calculateSquare(num):
    return num*num
 
# print the output
print("Square of ",number, "is ", calculateSquare(number))

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')


