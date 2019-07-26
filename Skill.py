# IMPORTS
# =============================================================================================================================
from flask import Flask, render_template                
from flask_ask import Ask, statement, question, session     
import random
import life360App as lf
import ReverseGeoCoder as RGC
import json
from gpio_handler import gpio_handler


# GLOBAL VARIABLES
# =============================================================================================================================
app = Flask(__name__)                    #Initializing the app
ask = Ask(app, '/Tester_JSON.py')                     #Initializing Alexa functionality around app


with open('config.json', 'r') as f:
    config = json.load(f)

apodos = config['SKILL']['APODOS']
'''
devices={}
for i in config["WEMO"]:
    devices[i] = gpio_handler(int(config["WEMO"][i]["PIN"]), str(config["WEMO"][i]["IP"]))
'''
# MAIN INTENT
# =============================================================================================================================
@ask.launch
def launcher():
    hellos=["Hi there","Howdy","May the force be with you","Greetings","Hello World!"]
    msg=random.choice(hellos)
    return question(msg)

    
@ask.intent('AMAZON.HelpIntent')
def help():
    return question(render_template("help"))


@ask.intent('AMAZON.FallbackIntent')
def fallback():
    return statement(render_template("fallback"))   
    
# SKILL INTENT
# =============================================================================================================================
# Hello
@ask.intent('HelloIntent')
def hello():
    hellos=["Hi there","Howdy","May the force be with you","Greetings","Hello World!"]
    return statement(random.choice(hellos))

# life360 Family Location
@ask.intent('LocateIntent')
def life360(shortname):
    location_dictionary=lf.locate()
    info=["Null","Someone not in the database","Null","-100%","Null"]
    for i in apodos:
        if(shortname.lower() in apodos[i]):
            info=location_dictionary[str(i)]
            break
    
    place=info[0] if info[0]!="" else RGC(info[1],info[2])

    return statement(f"{shortname} is at {place} with a battery of {info[3]}")
    # return statement(shortname+" is at "+ place +" With a battery of " + info[3])


@ask.intent('OnIntent')
def turn_on(device_name):
    if device_name.upper() in devices:
        devices[device_name.upper()].on()
        return statement(f"{device_name} is ON")
    else:
        return statement(f"{device_name} Not available or configured")


@ask.intent('OffIntent')
def turn_off(device_name):
    if device_name.upper() in devices:
        devices[device_name].off()
        return statement(f"{device_name} is OFF")
    else:
        return statement(f"{device_name} Not available or configured")
    

# RUN
# =============================================================================================================================
if __name__ == '__main__':
    app.run(debug=True)
