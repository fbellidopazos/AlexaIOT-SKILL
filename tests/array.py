
FAUXMOS = [
    ['Green LED', 4,"192.168.1.59"],
    ['Yellow LED',17,"192.168.1.39"],
    ['Blue LED',17,"192.168.1.39"]
]

with open("Config.txt") as textFile:
    lines = [line.split() for line in textFile]
print (lines[1])
