from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/math', methods=['POST'])
def math_ops():
    result = ""
    if request.method == 'POST':
        rf = request.form
        ops, num1, num2 = rf["operation"], rf["num1"], rf["num2"]

        match ops:
            case "add":
                result = f"{num1} + {num2} = {int(num1) + int(num2)}"
            case "subtract":
                result = f"{num1} - {num2} = {int(num1) - int(num2)}"
            case "multiply":
                result = f"{num1} * {num2} = {int(num1) * int(num2)}"
            case "divide":
                result = f"{num1} / {num2} = {int(num1) / int(num2)}"
            case "log":
                result = f"log({num1}) base({num2}) = {int(num1) ** (1/int(num2))} "

    return render_template('results.html', result=result)


@app.route('/math-postman', methods=['POST'])
def math_ops1():
    result = "success"
    if request.method == 'POST':
        rf = request.get_json()
        ops, num1, num2 = rf["ops"], rf["num1"], rf["num2"]

        match ops:
            case "add":
                result = f"{num1} + {num2} = {int(num1) + int(num2)}"
            case "subtract":
                result = f"{num1} - {num2} = {int(num1) - int(num2)}"
            case "multiply":
                result = f"{num1} * {num2} = {int(num1) * int(num2)}"
            case "divide":
                result = f"{num1} / {num2} = {int(num1) / int(num2)}"
            case "log":
                result = f"log({num1}) base({num2}) = {int(num1) ** (1/int(num2))} "
            case _:
                result = "Invalid operation"

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
