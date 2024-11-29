"""
CP1404 - Practical 10
Ashton Jack Stewart
Flask demonstration
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1> Hello World! :) <h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def convert_to_calcius(C_temperature):
    """Convert a celcius temperature input to Farenheit"""
    F_temperature = C_temperature * 1.8 + 32
    return F_temperature

if __name__ == '__main__':
    app.run()
