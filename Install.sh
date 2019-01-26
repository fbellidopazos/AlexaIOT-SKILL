#!/bin/bash
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
sudo apt install python3-gpiozero
sudo apt install pigpio
pip install -r Requirements.txt
sudo systemctl enable pigpiod
sudo raspi-config
sudo reboot
