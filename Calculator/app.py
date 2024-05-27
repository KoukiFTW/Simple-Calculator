from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']

    # Check if the expression is empty
    if not expression.strip():
        return render_template('calculator.html', error="Please input numbers")

    try:
        result = eval(expression)
        return render_template('calculator.html', result=result)
    except Exception as e:
        return render_template('calculator.html', error="Invalid expression")

if __name__ == '__main__':
    app.run(debug=True)
