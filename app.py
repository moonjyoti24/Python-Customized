from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def square(num):
    return num * num

number = float(input(" Welcome to Moonjyoti's 1st Python Program. Please Enter any numeric Value : "))

sqre = square(number)

print("The Square of a Given Number {0}  = {1}".format(number, sqre))

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')


