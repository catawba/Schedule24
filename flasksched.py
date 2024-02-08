from flask import Flask, render_template

app = Flask()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/index/')
def teachers():
    return render_template('teachers.html')

@app.route('/index/teachers/')
def addteachers():
    return render_template('addteachers.html')

@app.route('/index/')
def classes():
    return render_template('classes.html')

@app.route('/index/classes/')
def addclasses():
    return render_template('addclasses.html')

@app.route('/index/')
def states():
    return render_template('states.html')

if '__name__' == '__main__':
    app.run(debug=True)
    