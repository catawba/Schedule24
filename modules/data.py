# data.py
from tinydb import TinyDB, Query

import os
teachpath = os.path.join("C:\\",'Users','KyleC','VSCodeProjects','Schedule24','teachers.json')
classpath = os.path.join("C:\\",'Users','KyleC','VSCodeProjects','Schedule24','classes.json')
statepath = os.path.join("C:\\",'Users','KyleC','VSCodeProjects','Schedule24','states.json')


dbt = TinyDB(teachpath)
dbc = TinyDB(classpath)
dbs = TinyDB(statepath)


for state in dbs:
    print(state['name'])
    #for t in dbt:
     #   print(t['first'])
        

    



dbt.close()
dbc.close()
