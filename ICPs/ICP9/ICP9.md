[Video](https://youtu.be/GTLrpg6atOg)

[Arduino Code](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP9/sketch_mar22a.ino), [Phone Code](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP9/ControlTheArduinoLED.apk)


## Introduction

In this ICP we begin connecting our phones to IOT as a system of control.

## Objectives

We are to setup the arduino with a sensor and an led, create a phone app with MIT AI2, and then control the led with the app and read data from sensor over the phone.

## Approaches/Methods

We began by hooking up the LED and the bluetooth while programming the app. That part came together pretty quickly.

## Workflow

However, once we hooked up the light sensor and tried to read the data into the app we had constant problems. For some reason we could not read pure numbers and were instead getting random unicode characters appended to our numbers. In order to fix this we (1) changed the arduino, (2) changed the light sensor, (3) changed the computer which was compiling the code, (4) changed the code multiple times including baud rate changes. Only once we borrowed a temperature sensor from another group did everything come together and just work.

## Circuit Diagram

![](https://raw.githubusercontent.com/mwhol/490IOT/master/ICPs/ICP9/ICP9Circuit.jpg)

## Parameters

We used an arduino uno, light sensor, led, wires, resistor, breadboard, android phone and the MIT AI2 app we created.

## Evaluation

The assignment would have been totally fine if it had worked. However we were plagued by hardware problems.

## Conclusion

It was a fine assignment, interesting to see how easy it is to make a phone app with MIT AI2.