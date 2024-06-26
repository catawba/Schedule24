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
    
# all the teacher information
teach = dbt.all()
        # teachers.database structure
          # wname    work name
          # first
          # last
          # namelist  list of teachers teaching joint classes

# all the class information          
clss = dbc.all()
        # classes.database structure
          # name
          # section
          # grades
          # allstudents



app = Flask('__name__')

app.config['SECRET_KEY'] = 'mysecretkey'

class Assignstate(FlaskForm):
    section1 = BooleanField(False)
    section2 = BooleanField(False)
    classname = StringField('Enter the class name')
    submit = SubmitField('Submit')
    
class Assignclass(FlaskForm):
    teacher = StringField('Enter Teacher')
    class1 = StringField('Class 1')
    class2 = StringField('Class 2')
    class3 = StringField('Class 3')
    class4 = StringField('Class 4')
    class5 = StringField('Class 5')
    class6 = StringField('Class 6')
    class7 = StringField('Class 7')
    section1 = BooleanField(False)
    section2 = BooleanField(False)
    classname = StringField('Enter the class name')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/assignclass',methods = ['GET','POST'])
def assignclass():
    classname = False
    section1 = False
    section2 = False
    form = Assignclass()
 
    
    if form.validate_on_submit():
        classname = form.classname.data
        section1 = form.section1.data
        section2 = form.section2.data

        print(classname)
        print(section1)
        print(section2)

        form.classname.data = ''
        form.section1.data = False
        form.section2.data = False
        
    return render_template('assignclasses.html',teach=teach, clss=clss, form=form)
   

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

        print(classname)
        print(section1)
        print(section2)

        form.classname.data = ''
        form.section1.data = False
        form.section2.data = False
        
    return render_template('assignstates.html',teach=teach, clss=clss, form=form, classname=classname,section1=section1,section2=section2)

 
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
    