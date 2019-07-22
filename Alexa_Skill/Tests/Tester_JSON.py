import json

with open('config.json', 'r') as f:
    config = json.load(f)



print(config["LIFE360"]["USER"])
print(config["LIFE360"]["PASS"])
print(config["LIFE360"]["TOKEN"])

for i in config["WEMO"]:
    print(i)
    print(config["WEMO"][i]["PIN"])
    print(config["WEMO"][i]["IP"])

print(config["SKILL"]["APODOS"]["Fernando"][0])