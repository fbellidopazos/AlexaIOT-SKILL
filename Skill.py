from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import random
import logging
import os
import ast
import time
import life360App
import modules.ReverseGeoCoder as RGC

#Notes:
#=========================
#Hace acciones No imprime por pantalla
#Hacer Raspberry Pi
#
#

#Raspberry GPIO
#===================
#Type 0 -> LED
#Type 1 -> Curtains,...
#Type 2 ->
'''
with open('Config.txt', 'r') as f:
    Devices = ast.literal_eval(f.read())
'''
apodos={
"Fernando":["fair","ferny"],
"Efebeac":["dad","fernando","efebeac"],
"Maria":["mom","maria","maria"],
"IgnacioBP":["nene","ignacioBP"]
}


app=Flask(__name__)
ask = Ask(app,'/test')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

'''
Mandatory Section:
=====================================================================================
1.-Opening
2.-Help
'''
#Opening
@ask.launch
def launcher():
    hellos=["Hi there","Howdy","May the force be with you","Greetings","Hello World!"]
    msg=random.choice(hellos)+"......................What would you like to do?"+render_template("help")
    return question(msg)



@ask.intent('AMAZON.HelpIntent')
def help():
    return question(render_template("help"))





'''
Intents:
=====================================================================================
1.-Hellos
2.-life360
3.-Turn On/Off---Not Done
'''
@ask.intent('HelloIntent')
def hello():
    hellos=["Hi there","Howdy","May the force be with you","Greetings","Hello World!"]
    return statement(random.choice(hellos))

#life360 Family Location
@ask.intent('LocateIntent')
def life360(Shortname):
    dict=life360App.locate()
    info=["Null","Someone not in the database","Null","-100%","Null"]
#Find if a shortname is in the name then gets the key to which it takes the data and stores it in Info
    for i in apodos:
        if(Shortname.lower() in apodos[i]):
            info = dict[i]
            break
    return statement(Shortname+" is at "+ info[0] if info[0]!="" else RGC.reverseGEO(info[1],info[2]) +" With a battery of " + info[3])


'''MANDATORY'''
if __name__ == '__main__':
    #os.system("gnome-terminal -x python AlexaIOT0.py")
    #os.system("python AlexaIOT0.py")
    app.run(debug=True)
