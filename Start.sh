#!/bin/bash

cd ~/Desktop/AlexaIOT-SKILL/
lxterminal -e ./ngrok http 5000

python WeMo.py & python3 Skill.py
