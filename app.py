from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/hello')
def hello():
   
    name = os.getenv('NAME', 'Guest')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)