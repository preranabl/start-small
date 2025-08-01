from flask import Flask, render_template
import os
# Load environment variables from .env file (optional)
from dotenv import load_dotenv  # For .env file support

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')

@app.route('/hello')
def hello():
    """Render the hello page with name from environment variable"""
    name = os.getenv('NAME', 'Guest')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5001)