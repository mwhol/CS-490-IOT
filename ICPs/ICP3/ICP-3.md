Here's the video: [Part 1](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP3/ICP3Video1.mp4?raw=true) and [Part 2](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP3/ICP3Video2.mp4?raw=true).

[Here is the code.](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP3/weatherstationcode.ino)

# Introduction

In this assignment we were to make a basic weather monitor including several different sensors.

# Objectives

We were to connect up the following sensors: Humidity/Temperature sensor, Barometer, Dust Sensor, Light Sensor, UV Sensor. Following that we connected an LCD screen and a wifi module and then displayed our data on the LCD while transmitting it to the ThingSpeak server.

# Approaches/Methods

We started our approach by wiring up each sensor and testing it one by one, then connecting the LCD and wifi, integrating some code from our last ICP into this one to make sure it worked with the temperature sensor. After that was successful we began integrating the code into one large program.

# Workflow

After getting all the components working, we took last ICP's code and copied out the relevant portions for the LCD and the wifi card. we changed `updatebeat()` into a generic function which accepted a char corresponding to the relevant field in our thingspeak server and a value which we passed to that thingspeak field. Then in the code driving each sensor we changed our `Serial.print()`'s into `lcd.print()`'s and began testing them, adding one at a time. Once that was all working we were done.

# Circuit Diagram

## Temperature Sensor

![](https://github.com/mwhol/490IOT/raw/master/ICPs/ICP3/490IOT/Temperature%20Sensor.jpg)

## Barometer

![](https://github.com/mwhol/490IOT/raw/master/ICPs/ICP3/490IOT/Barometer.png)

## Dust

![](https://github.com/mwhol/490IOT/raw/master/ICPs/ICP3/490IOT/Dust.jpg)

## Light Sensor

![](https://github.com/mwhol/490IOT/raw/master/ICPs/ICP3/490IOT/Light%20Sensor.jpg)

# Parameters

We used an Arduino Uno, an LCD Module, an ESP8266, a breadboard, wires and the following sensors: Humidity/Temperature sensor, Barometer, Dust Sensor, Light Sensor, UV Sensor.

# Evaluation

Good lesson, it took us a little bit longer than it should have but all in all I thought it was good. We should've hooked up the SDA/SCL connections a bit differently to start with but since we thought they couldn't share we wandered into the weeds a bit. We also went for the bonus and used the UV sensor and integrated everything into one big program instead of doing them as 5 separate programs.

# Conclusion

Fun class, I really enjoyed doing the wiring on this one and the coding was pretty fun too. 👍 