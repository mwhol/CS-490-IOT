Here are the videos: [1](https://youtu.be/BrFBOaLmuo0), [2](https://youtu.be/94BD3tL5t-c).

Here is the code: [Celsius to Fahrenheit custom node](https://github.com/mwhol/490IOT/tree/master/ICPs/ICP6/CelstoFahr), [Blinking Light](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP6/Part1Code.txt), [Traffic Light](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP6/Part2.json).

## Introduction

Node-Red is useful at creating IOT frontends. In this ICP we make a custom node and integrate Node-RED and arduino.

## Objectives

Our first objective was to use Node-Red to blink an led on and off, and our second objective was to extend that to a traffic light system.

## Approaches/Methods

I started right in on the assignment. First thing was that while dan worked on the led blinking on and off I began working on making a traffic light. That required figuring out how to make a function that could keep state and so know which light was lit up _and_ send different messages to each of the arduino pins. Once I figured that out, the assignment was basically done.

## Workflow

The hardest part was figuring out the function for the traffic light. Once realizing that we can use _context.level_ as a modulo counter and how to build multiple messages in a function we were set.

## Circuit Diagram

![](https://github.com/mwhol/490IOT/raw/master/ICPs/ICP6/Part1pic.PNG)
***
![](https://github.com/mwhol/490IOT/raw/master/ICPs/ICP6/CircuitPic.jpg)
![](https://github.com/mwhol/490IOT/raw/master/ICPs/ICP6/Part2.PNG)

## Parameters

Node-Red - we made use of the inject interval node, a function node, and arduino nodes.

## Evaluation

Node-Red seems pretty useful, and this assignment started to draw the connections for how it will be used in the second half of this class to control a robot.

## Conclusion

Overall a good assignment!