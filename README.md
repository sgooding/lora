# Lora Experiments

Install Arduino 1.6.11? Does NOT see to upload using windows 7, not sure why.
DOES NOT WORK IN WINDOWS 7
Bootloader for feather switches to a new device that is not recognized, so the other COM port is always missing.

Not an issue in windows 10.

Install Arduino 1.6.11? Does NOT see to upload using windows 7, not sure why.


Add the following to Arduino
File->Preferences->Additional boards manager URLs
https://adafruit.github.io/arduino-board-index/package_adafruit_index.json

Click Board Manager
Search All->Adafruit
Install Adaruit AVR Boards by Adafruit

Download and Install Windows 7 drivers
https://learn.adafruit.com/adafruit-arduino-ide-setup/windows-driver-installation

Download RadioHead Driver
http://www.airspayce.com/mikem/arduino/RadioHead/

Unzip into ~/Arduino

References:
https://www.faranux.com/product/lora32u4-ii-development-board-868mhz-915mhz-lora-module/

Hope RF Datasheet
https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf

