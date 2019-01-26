#!/bin/bash

cd ~/Desktop/AlexaIOT-SKILL/
lxterminal -e ./ngrok http 5000

python AlexaIOT0.py & python3 Skill.py
