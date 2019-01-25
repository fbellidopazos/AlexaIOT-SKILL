
apodos={
"Fernando":["fair","ferny"],
"Efebeac":["dad","fernando","efebeac"],
"Maria":["mom","maría","maria"],
"IgnacioBP":["nene","ignacioBP"]
}
shortname="Fair"
for i in apodos:
    if(shortname.lower() in apodos[i]):
        print(True)
    break
