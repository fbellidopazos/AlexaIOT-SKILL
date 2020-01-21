# AlexaIOT & Skill
## Contents
* ngroks
* ReverseGeoCoder.py
* Skill.py -> Skill
* WeMo(Py3).py -> IOT Fauxmo for Python 3
* WeMo.py ->  IOT Fauxmo
* config.json -> Config file(See configuration)
* gpio_handler.py
* life360.py
* life360App.py
* requirements.txt
* templates.yaml

## Installation
1. Clone Repository
1. Edit config.json(See configuration)
1. Make Amazon Dev and put Skill
1. Set Up raspberrys
1. Open Skill.py for Skill and WeMo(Py3).py for IOT
1. Enjoy

## Configuration
```json
{
  "SKILL": {
    "APODOS" : {
        "<Life360 Name>" : ["<Short Name>","<Short Name>"],
    }
  },
  "WEMO": {
    "LIGHTS": {
      "PIN" : 4,
      "IP" : "<Insert IP>"
    },
    "LIGHTS2": {
      "PIN" : <Insert Pin Number>,
      "IP" : "<Insert IP>"
    }
  },
  "LIFE360": {
    "USER": "<Insert User>",
    "PASS": "<Insert Password>",
    "TOKEN": "cFJFcXVnYWJSZXRyZTRFc3RldGhlcnVmcmVQdW1hbUV4dWNyRUh1YzptM2ZydXBSZXRSZXN3ZXJFQ2hBUHJFOTZxYWtFZHI0Vg=="
  }
}
```
