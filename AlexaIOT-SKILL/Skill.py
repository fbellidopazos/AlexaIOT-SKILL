from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import random
import logging
import os
import ast
import time
import life360App


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
devices={
"White LED"=[PIN,IP,TYPE,GROUP],
"Green LED"=[PIN,IP,TYPE,GROUP],
"Yellow LED"=[PIN,IP,TYPE,GROUP],
"Curtains"=[PIN,IP,TYPE,GROUP]
}
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


#Intents
@ask.intent('HelloIntent')
def hello():
    hellos=["Hi there","Howdy","May the force be with you","Greetings","Hello World!"]
    return statement(random.choice(hellos))


'''
Intents:
=====================================================================================
1.-life360
2.-Turn On/Off
'''

#life360 Family Location
@ask.intent('LocateIntent')
def life360(Shortname):
    dict=life360App.locate()
    info=["Null","Someone not in the database","Null","-100%","Null"]
#Find if a shortname is in the name then gets the key to which it takes the data and stores it in Info
    for i in apodos:
        if(Shortname.lower() in apodos[i]):
            info=dict[i]

    #Make GPS regions in order to say where someone is at
            if(40.6387>=float(info[1])>=40.637 and -3.571>=float(info[2])>=-3.573):
                info[1]="Home" #CASA
            elif(40.631>=float(info[1])>=40.6285 and -3.584>=float(info[2])>=-3.5839):
                info[1]="Buying groceries" #En La compra
            elif(40.6288>=float(info[1])>=40.6277 and -3.584>=float(info[2])>=-3.5821):
                info[1]="Having A relaxing Cup of Cafe Con Leche at Santo Domingo" #Xarelo/MiaNona etc...
            else:
                info[1]="'Somewhere I dont Know'"
            break
    return statement(Shortname+" "+"is "+info[1]+" With a battery of " + info[3])


#Needed
if __name__ == '__main__':
    #os.system("gnome-terminal -x python AlexaIOT0.py")
    #os.system("python AlexaIOT0.py")
    app.run(debug=True)
