from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', '/square', methods=['GET'])

def hello():
    return "Welcome to Moonjyoti's Webpage!"
    
def squarenumber():
    num = request.args.get('num')

    if num is None:  # No number entered, show input form
        return render_template('squarenum.html')
    elif num.strip() == '':  # Empty input
        return "<h1>Invalid number. Please enter a number.</h1>"
    try:
        square = int(num) ** 2
        return render_template('answer.html', squareofnum=square, num=num)
    except ValueError:
        return "<h1>Invalid input. Please enter a valid number.</h1>"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')


