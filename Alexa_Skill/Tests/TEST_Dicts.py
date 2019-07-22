import json

with open('config.json', 'r') as f:
    config = json.load(f)


class gpio_handler(object):
    def __init__(self, pin_number,ip):
        self.pin=int(pin_number)

    def on(self):
        print(str(self.pin)+" IS ON")

    def off(self):
        print(str(self.pin)+" IS OFF")
    def __str__(self):
        return(f"PIN : {self.pin}")



devices={

}

for i in config["WEMO"]:
    devices[i]=gpio_handler(int(config["WEMO"][i]["PIN"]),str(config["WEMO"][i]["IP"]))

print(devices.keys())