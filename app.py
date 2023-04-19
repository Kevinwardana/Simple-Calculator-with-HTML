from flask import Flask, render_template, url_for, request
app = Flask(__name__)
@app.route("/",methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/operation_result/', methods=['POST'])
def operation_result():
    error = None
    result = None
    first_input = request.form['Input1']
    second_input = request.form['Input2']
    operation = request.form['operation']
    try:
        input1 = float(first_input)
        input2 = float(second_input)
        if operation == "+":
            result = input1 + input2
        elif operation == "-":
            result = input1 - input2
        elif operation == "/":
            result = input1 / input2 
        elif operation == "*":
            result = input1 * input2
        else:
            operation = "%"
            result = input1 % input2
        return render_template('ndex.html',input1=input1,input2=input2,operation=operation,result=result,calculation_success=True)
    except ZeroDivisionError:
        return render_template('index.html',input1=input1,input2=input2,operation=operation,result="Bad Input",calculation_success=False,error="You cannot divide by zero")
    except ValueError:
        return render_template('index.html',input1=first_input,input2=second_input,operation=operation, result="Bad Input",calculation_success=False,error="Cannot perform numeric operations with provided input")
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)    