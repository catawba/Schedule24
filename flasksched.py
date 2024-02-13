from flask import Flask, render_template
from tinydb import TinyDB, Query

dbc = TinyDB('classes.json')
dbs = TinyDB('states.json')
dbt = TinyDB('teachers.json')

class Teacher():
    def __init__(self,
                 wname="",
                 first="",
                 last="",
                 namelist=[]
                 ) -> None:
          # this is a list to check for multiple teachers linked together
        self.wname=wname   # KCanty work name for this teacher BCantyJBagwellJCary
        self.first=first
        self.last=last
        self.namelist=namelist
    

teach = []
for t in dbt:
    teach.append(t)
    
clss = []
for c in dbc:
    clss.append(c)
    


app = Flask('__name__')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/teachers/')
def teachers():  
    
    return render_template('teachers.html', teachinfo=teach)

@app.route('/index/addteachers')
def addteachers():
    return render_template('addteachers.html')

@app.route('/index/')
def classes():
    return render_template('classes.html', classinfo=clss)

@app.route('/index/addclasses/')
def addclasses():
    return render_template('addclasses.html')

@app.route('/index/')
def states():
    return render_template('states.html')


dbc.close()
dbt.close()
dbs.close()

if __name__ == '__main__':
    app.run(debug=True)
    