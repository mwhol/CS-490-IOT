[Video](https://youtu.be/Zz26EXnrD9g)

[Code1](https://github.com/mwhol/490IOT/blob/master/ICPs/IPC8/snippet-1.py), [Code2](https://github.com/mwhol/490IOT/blob/master/ICPs/IPC8/snippet-2.ino)


## Introduction

Having worked with both the arduino and the raspberry pi it is now time to integrate them into one system!

## Objectives

In this assignment we are to connect our raspberry pi to our arduino, then run code on both of those that allows them to talk to each other and also light up an led.

## Approaches/Methods

First, on raspberry pi we enabled I2C and serial and then configured pyserial. Simultaneously we loaded some simple code onto the arduino.

## Workflow

We had one struggle which was with the if statement in our python code. We used `repr()` to to read what exactly the arduino was sending and found out that it was appending a carriage return. Once we controlled for that in our python code then we were rockin' and rollin'.

## Circuit Diagram

![](https://raw.githubusercontent.com/mwhol/490IOT/master/ICPs/IPC8/ICP8Circuit.jpg)

## Parameters

We used a raspberry pi, arduino, a power cord for each, a breadboard, wires, resistors and LEDs.

## Evaluation

This one wasn't too hard since the code was provided.

## Conclusion

Thought this one was interesting in how relatively little code it took to get the raspberry pi and arduino to talk to each other.