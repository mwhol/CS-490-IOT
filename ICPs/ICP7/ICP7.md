[Video](https://youtu.be/1pPCsiZEDnI)

[Code](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP7/icp7code.json)

## Introduction

This if our first ICP with the raspberry pi, in it we setup and get a basic introduction to how to with node-red on the raspberry pi.

## Objectives

In this assignment we were to take our arduino/node-red traffic light and convert it to run on the raspberry pi. In addition we also add a twitter node so that our flow also tweets.

## Approaches/Methods

Our approach first involved hooking up the raspberry pi to our screen, mouse and keyboard. Once we had gotten NOOBS up and working, we enabled VNC and then set a static ip, so we could unplug and replug the device in as we choose.

## Workflow

Once we had the raspberry pi setup, we VNC'd into the raspberry pi and setup a flow very similar to the arduino traffic light. Also we added a tweet node to the red light led, so that every three seconds we would send a tweet. Then we hooked up a very basic circuit with three leds on the breadboard and connected them to the pi.

## Circuit Diagram

![](https://raw.githubusercontent.com/mwhol/490IOT/master/ICPs/ICP7/ICP7Circuit.jpg)

## Parameters

This assignment required a raspberry pi, microsd card, sd card converter, a screen, mouse and keyboard along with micro-usb charging cord, breadboard, wires, resistors and leds.

## Evaluation

Overall, I thought this assignment went very smoothly. Our only real hitch was setting the pi's ip address to be static so that we wouldn't have concerns about restarting it.

## Conclusion

Good assignment, I had a little familiarity with the raspberry pi but didn't know it was quite as powerful as it ended up being.