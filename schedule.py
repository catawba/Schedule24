# schedule.py  main program to create class schedule

from tinydb import TinyDB,Query


# --------- open databases
if True:
    dbc = TinyDB("classes.json")
    dbt = TinyDB("teachers.json")
    dbs = TinyDB("states.json")
    
class State:
    def __init__(self,name="",tname="",color=0,conlist=None) -> None:
        if conlist is None:
            conlist = []
        self.name = name  # Algeba2 name of the class
        self.tname = tname # KCanty teacher's name
        self.color = color # 3 map color ie green is 3
        self.conlist=conlist # list containing conflicts with other classes  can't be taught at the same time can's have the same color
        
        
    def conflictnum(self):  # count the number of conflicts for map coloring
        return len(self.conlist)
    
    def wname(self):        
        return self.name+"%"+self.tname
    

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




       
class Sclass():
    def __init__(self,
                 name="",
                 section="",
                 grades=None,
                 allstudents=False):
        if grades==None:  # class is available for 9th,10th graders
            grades=[]
        self.name=name     # Algebra2 class name
        self.section=section  # a,b section name, KCantyAlgebra2a
        self.allstudents=allstudents
        

# main

#--------- classes
dbc.insert({'name':'Algebra2',
           'tname':'KCanty',
           'color':3,
           'conlist':['KCanty_Algebra2','KBond_English2'],
           'conflictnum':2,
           'wname':'KCanty_Algebra2'})

#-------- teachers
dbt.insert({'wname':'KCanty',
           'first':'Kyle',
           'last':'Canty',
           'namelist':['KCanty']})
dbt.insert({'wname':'JBagwell%JCary%BCanty',
           'first':'MultFirst',
           'last':'MultLast'
           'namelist':['JBagwell','JCary','BCanty']})
mestate = State(name='Algebra2a',
           tname='KCanty',
           color=3,
           conlist=['Algebra2b%KCanty','English2a%Bond'])    

#-----------classes
dbc.insert({'name':'KCanty_Algebra2',
           'section':None,
           'grades':['10','11']})  

dbc.insert({'name':'KCanty_Math7',
           'section':'a',
           'grades':['7'],
           'allstudents':True})          
                  

meteacher = Teacher('KCanty',
                    'Kyle',
                    'Canty',
                    ['KCanty']) 
dbt.insert({meteacher})

memult = Teacher('JBagwellJCaryBCanty',
                 'JoanneJoeBlake',
                 'BCC',
                 ['JBagwell','JCary','BCanty','KCanty'])   


if meteacher.wname in memult.namelist:
    print('conflict found')

if True: 
    dbc.close()
    dbt.close()
    dbs.close()
  
