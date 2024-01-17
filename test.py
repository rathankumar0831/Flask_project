from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show():
    return render_template("calc.html")

@app.route("/math", methods = ["POST"])
def calculator_test():
    ops = request.form['operation']
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    if (ops == 'add'):
        r = num1 + num2
        return f'the addition of {num1} and {num2} is {r}'
    elif (ops == 'subtract'):
        r = num1 - num2
        return f'the subtract of {num1} and {num2} is {r}'
    elif (ops == 'multiply'):
        r = num1 * num2
        return f'the multiply of {num1} and {num2} is {r}'
    elif (ops == 'divide'):
        r = num1 / num2
        return f'the divide of {num1} and {num2} is {r}'



if __name__ == "__main__":
    app.run(host='0.0.0.0')