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
        
def crudclasses(db):
    more = True
    while more:
        classname = input("Enter Class Name: ")
        gradelist = input("Enter grade list comma seperated: ")
        glist=gradelist.split(',')         
        entireclass = input("Entire Class taught <y/n>: ")
        if entireclass == 'y':
            eclass = True
        else:
            eclass = False
            
        saveclass = input("Save the class <y/n>: ")
        print()
        if saveclass == 'y':
            db.insert({'name':classname,
           'grades':glist,
           'allclass':eclass})
            print('class saved')
        else:
            print('class discarded')
            
        cmore = input("Enter another class <y/n>? ")
        if cmore != 'y':
            more = False


   
def crudteachers(db):
    more = True
    while more:
        firstname = input("Enter First Name: ")
        lastname = input("Enter Last Name: ")
        wname = firstname[0:2]+lastname
        namelist = [wname]
        
        saveteacher = input("Save <y/n>: ")
        print()
        if saveteacher == 'y':
            db.insert({'wname':wname,
           'first':firstname,
           'last':lastname,
           'namelist':namelist})
            print('teacher saved')
        else:
            print('teacher discarded')
            
        cmore = input("Enter another teacher <y/n>? ")
        if cmore != 'y':
            more = False


def crudstates(db):
    more = True
    while more:
        print('States')
        cname = input("Enter Class Name: ")
        tname = input("Enter Teacher Name: ")
        color = 0       
        clist = input("Enter Conflict list: ")
        conlist = clist.split(',')
        conflictnum = 0
        wname = tname+'_'+cname
        conlist.append(wname)
      
        savestate = input("Save <y/n>: ")
        print()
        if savestate == 'y':
            db.insert({'cname':cname,
           'tname':tname,
           'wname':wname,
           'color':color,
           'conlist':conlist})
            print('state saved')
        else:
            print('state discarded')
            
        cmore = input("Enter another state <y/n>? ")
        if cmore != 'y':
            more = False

def menu():
    print()
    print("Main Menu")
    print("==================")
    print("Add <t>eachers")
    print("Add <c>lasses")
    print("Add <s>tates")
    print("<l>oad states")
    print("e<x>it")
    ch = input("Enter choice: ")
    print()
    print()
    return ch
 
# main
more = True
while more:
    choice = menu()
    if choice == 't':
        #-------- teachers
        crudteachers(dbt)

    elif choice == 'c':
        #-----------classes
        crudclasses(dbc)

    elif choice == 's':
        #--------- states
        crudstates(dbs)
    
    elif choice == 'l':
        # load states from teachers and classes
        pass
    
    elif choice == 'x':
        # exit
        more = False           
 
for state in dbs:
    print(state)
    
for classes in dbc:
    print(classes)
    
for teacher in dbt:
    print(teacher)


if False:
    #empty all databases
    dbc.truncate()
    dbt.truncate()
    dbs.truncate()
    
if True: 
    dbc.close()
    dbt.close()
    dbs.close()
  
