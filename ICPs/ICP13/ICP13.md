[Video](https://youtu.be/dcnEMEBzNn0)

[ESP8266 Code](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP13/esp8266LEDandSENSOR.ino) and [Mobile Code](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP13/LED_Control.aia)


## Introduction

In this ICP we work with a new SOC the esp8266mod. We also make it communicate both over web and mobile.

## Objectives

We connect our esp8266 to a sensor and an led and are able to read the sensor and blink the led via web or mobile.

## Approaches/Methods

First we hooked up our chip to the led, took Sayed's code and ran that. We had a few difficulties with our breadboard but after switching to a new breadboard it worked. We then began modifying the code so that it could pull data from a sensor.

## Workflow

Afterwards we worked on the mobile app, creating two buttons, one which can turn the light on or off and another one which can grab the data. However we came to a crossroads here. When, from the website, we try to grab sensor data we load a full html page. But from the mobile app we don't want html, we want just the raw sensor data. This required adjusting the esp8266 code a bit to differentiate these two GET requests.

## Circuit Diagram

![](https://raw.githubusercontent.com/dalders0525/490IoTRoPro/master/ICPs/ICP13/ICP13_Circuit.jpg)

## Parameters

We used an ESP8266MOD, breadboard, wires, led, temperature sensor, phone and a web browser.

## Evaluation

Overall good, it was fun to work with another chip, one that cuts a bit between the arduino and the raspberry pi in terms of complexity.

## Conclusion

A good assignment, just the right amount of challenge.