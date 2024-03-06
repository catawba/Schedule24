from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length

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
    

teach = dbt.all()
  
clss = []
for c in dbc:
    clss.append(c)
    


app = Flask('__name__')

app.config['SECRET_KEY'] = 'mysecretkey'

class Assignstate(FlaskForm):
    section1 = BooleanField(False)
    section2 = BooleanField(False)
    classname = StringField('Enter the class name')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/assignstate',methods = ['GET','POST'])
def assignstates():
    classname = False
    section1 = False
    section2 = False
    form = Assignstate()
    
    if form.validate_on_submit():
        classname = form.classname.data
        section1 = form.section1.data
        section2 = form.section2.data
        
        
    
        form.classname.data = ''
        form.section1.data = False
        form.section2.data = False
        
    return render_template('assignstates.html',form=form,classname=classname,section1=section1,section2=section2)

@app.route('/teachers/')
def teachers():  
    return render_template('teachers.html', teach=teach)

@app.route('/index/addteachers')
def addteachers():
    return render_template('addteachers.html')

@app.route('/index/classes')
def classes():
    return render_template('classes.html', classinfo=clss)

@app.route('/index/addclasses/')
def addclasses():
    return render_template('addclasses.html')

@app.route('/index/states/')
def states():
    return render_template('states.html', classinfo=clss)


dbc.close()
dbt.close()
dbs.close()

if __name__ == '__main__':
    app.run(debug=True)
    