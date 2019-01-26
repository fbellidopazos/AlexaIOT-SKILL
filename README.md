# Alexa OITPI

## Raspberry Pi - Installation
### Main Hub
1. Clone repository
2. CD to project folder
3. Update and Upgrade ... (sudo apt-get update and sudo apt-get upgrade)
4. sh Install.sh
5. In raspi-config enable RemoteGPIO
6. (Optional) Enable VNC and SSH , for better control when operating and troubleshooting
7. The installation will reboot Raspberry, save everything before

### Remotes
1. (Optional) Install Raspian Lite(Less Space) or Raspian Full
2. Enable autologin, RemoteGPIO and Wait for Network in boot (sudo raspi-config)
3. (Obvious) Configure Network
4. (Optional) Put Static IP

### Lights/Switches
1. Install Relay in Remotes(You do this part)
2. In Config.txt add devices example:
```
<Write How>
```
### As Family
1. Install Life360
2. Put one user in life360App(Username and Password)
3. Work the Coordinates out(Inside Skill.py -- See Example)
```
EXAMPLE

if(40.6387>=float(info[1])>=40.637 and -3.571>=float(info[2])>=-3.573):
          info[1]="Home" #CASA
      elif(40.631>=float(info[1])>=40.6285 and -3.584>=float(info[2])>=-3.5839):
          info[1]="Buying groceries" #En La compra
      elif(40.6288>=float(info[1])>=40.6277 and -3.584>=float(info[2])>=-3.5821):
          info[1]="Having A relaxing Cup of Cafe Con Leche at Santo Domingo" #Xarelo/MiaNona etc...
      else:
          info[1]=RGC.reverseGEO(info[1],info[2])
      break

```
### Once Evertything configured
In Main Hub
1. Cd to project folder
2. sh Start.sh
3. Make  the Alexa App....





## Contents
### Alexa Skill
1. Hellos
2. life360
3. Turn On/Off---Not Done
4.

### Lights/Switches
1. Emulation WeMo Devices lights and Switcher
2. Remote Doorbell

### Remote Doorbell
In progress

##Credits
### Not my stuff:
Thanks to
1. https://github.com/harperreed/life360-python --> Life360
2. https://geopy.readthedocs.io/en/stable/ -->
