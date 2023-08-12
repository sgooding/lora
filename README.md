# Lora Experiments

## Notes:
    !!! DOES NOT WORK IN WINDOWS 7 !!!

    Bootloader for feather switches to a new device that is not recognized, so the other COM port is always missing.

Works with windows 10.

## Installation

1. Install the adafruit board packages.
  * Adafruit Board Packages
  *  Add the following to Arduino
      File->Preferences->Additional boards manager URLs
    https://adafruit.github.io/arduino-board-index/package_adafruit_index.json

  * Click Board Manager
    Search All->Adafruit
    Install Adaruit AVR Boards by Adafruit

2. Install RadioHead Driver
  * Download RadioHead Driver OR

      http://www.airspayce.com/mikem/arduino/RadioHead/

  * Direct Link Here:

      http://www.airspayce.com/mikem/arduino/RadioHead/RadioHead-1.124.zip

  * Unzip into ~/Arduino

## References:
* LoRa32U4 II Manufacturer: https://www.faranux.com/product/lora32u4-ii-development-board-868mhz-915mhz-lora-module/

* Hope RF Datasheet: https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf


## Experiment 1

### Purpose: 

Try to get TX and RF examples working.

### Steps:

1. Run Window 10
2. Install arduino
3. Install adafruit board manger link
4. Install adafruit boards
5. Install RadioHead drivers.
6. Open Feather9x_TX in arduino.
7. Plug in Tx device.
8. Compile and Upload.
    * Sometimes the device is not able to switch to bootloader - try DOUBLE-clicking reset AFTER clicking Upload in Arduino.
9. If upload success, try connecting Serial Monitor. It should be waiting to send.
10. Follow steps 6-9 with 2nd device and the Feather9x_RX package.
11. Plug in a seconds computer with arduino to initialize serial with other device.
12. Hello world should be sent by TX, received by RX, then relayed back to TX as a response.

### Conclusion:

Appears to be transmitting/receiving correctly.
