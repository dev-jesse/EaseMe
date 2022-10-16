from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/einsteinchat')
def EinsteinChat():
    return render_template('einsteinchat.html')