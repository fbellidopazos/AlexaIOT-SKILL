apodos={
"Fernando Bellido Pazos":["Fair","Ferny"],
"Efebeac":["Dad","Fernando"],
"Maria":["Mom","María"],
"IgnacioBP":["Nene"]
}

x="No"
for i in apodos:
    for k in range(len(apodos[i])):
        if(x==apodos[i][k]):
            print("Found")
            break
