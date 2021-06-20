[Motion Detector video](https://www.youtube.com/watch?v=KDzlHEciy5U) and [Lie Detector video](https://www.youtube.com/watch?v=A7-brLrQSKQ)

[Motion Sensor Code](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP11/motion_sensor/motion_sensor.ino), [Lie Detector Code](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP11/lie_detector/lie_detector.ino)


## Introduction

In this ICP we work with our last new sensor, the motion sensor and also build a basic lie detector with the heartbeat sensor.

## Objectives

We are to setup the arduino with a motion sensor and an led which blinks when motion is detected. Then we setup a basic lie detector using the heartbeat monitor.

## Approaches/Methods

We took an arduino, wired up an led and the PIR motion sensor. Then we wrote a very simple program which lights up the led when the motion sensor is activated.

## Workflow

When we made the lie detector we wired up a heartbeat sensor similar to the last time we used this sensor. Instead of using the code from last time to calculate a proper heartbeats per minute number we just use the raw data from the sensor, and compare it to a baseline. If it's above the baseline the user is probably lying, and if its below they're probably not.

## Circuit Diagram

See the video for wiring.

## Parameters

We used an arduino uno, motion sensor, heartbeat sensor, wires, breadboard and two leds - one red, one green.

## Evaluation

Overall a fine assignment. We had to play around with the motion sensor a bit to get it working but it didn't take too long and it was easy street once we had that.

## Conclusion

Good assignment.