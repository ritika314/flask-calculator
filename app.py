from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    result = ""
    if request.method == 'POST':
        n1 = float(request.form['num1'])
        n2 = float(request.form['num2'])
        op = request.form['operation']
        if op == 'add': result = n1+n2
        elif op == 'subtract': result = n1-n2
        elif op == 'multiply': result = n1*n2
        elif op == 'divide': result = n1/n2 if n2!=0 else "Cannot divide by zero"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)