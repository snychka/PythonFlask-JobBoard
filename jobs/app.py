from flask import Flask,render_template
app = Flask(__name__)

# http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')
