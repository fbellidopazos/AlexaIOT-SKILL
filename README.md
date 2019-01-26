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
