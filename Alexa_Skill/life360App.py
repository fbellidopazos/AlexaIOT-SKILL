from life360 import life360
import json

with open('config.json', 'r') as f:
    config = json.load(f)

def xstr(s):
    if s is None:
        return ''
    return str(s)

def locate():

    # basic authorization hash (base64 if you want to decode it and see the sekrets)
    # this is a googleable or sniffable value. i imagine life360 changes this sometimes.
    authorization_token = config["LIFE360"]["TOKEN"]

    # your username and password (hope they are secure!)
    username = config["LIFE360"]["USER"]
    password = config["LIFE360"]["PASS"]

    #instantiate the API
    api = life360(authorization_token=authorization_token, username=username, password=password)
    if api.authenticate():
        Data={}

        #Grab some circles returns json
        circles =  api.get_circles()

        #grab id
        id = circles[0]['id']

        #Let's get your circle!
        circle = api.get_circle(id)

        #Let's display some goodies

        #print ("Circle name:"+ circle['name'])
        #print ("Members (" + circle['memberCount'] + "):")

        for m in circle['members']:Data[xstr(m['firstName'])] = [xstr(m['location']['name']),xstr( m['location']['latitude']),xstr(m['location']['longitude']),xstr( m['location']['battery'] )+"%"]

    else:
        Data="None"
    return(Data)
