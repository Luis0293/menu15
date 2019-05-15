from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/p2')
def p2():
    return render_template('p2.html')

@app.route('/p3')
def p3():
    return render_template('p3.html')




if __name__ == '__main__':
    app.run(debug=True)
