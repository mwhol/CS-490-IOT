[Video 1](https://github.com/DanielPLongo/DanielLongoIOT/blob/master/Lab1/Lab1Video-1.mp4?raw=true)

[Video 2](https://github.com/DanielPLongo/DanielLongoIOT/blob/master/Lab1/Lab1Video-2.mp4?raw=true)

[The Arduino Code](https://raw.githubusercontent.com/DanielPLongo/DanielLongoIOT/master/Lab1/Lab1FinalCode/Lab1FinalCode.ino)

[The Python Script](https://raw.githubusercontent.com/mwhol/490IOT/master/Labs/Lab1/pull.py)

[The DashBoard](https://io.adafruit.com/mikewholey/dashboards/490lab1)

# Introduction

IOT is extremely useful in the home and as an always on device. In this lab we integrate many different sensors into one device to monitor conditions within the home and on an individual and warn them if it appears that anything dangerous is happening. We do this through the use of hardware (LEDs and buzzers) and through software (an AdaFruit dashboard).

# Objectives

In this assignment we were to take our previous weather station and augment it with a heartbeat monitor, some buttons to control the device and buzzers/LEDs to warn us whenever we had a dangerous reading from one of our sensors. We also create a new dashboard in a cloud service other than ThingSpeak (we chose AdaFruit) and wrote code to send to send our data to that service.

# Approaches/Methods

Unfortunately we did not have a heartbeat monitor but we have done everything else. We approached this problem by taking our existing weather station code and modifying it. First we added tolerances for each sensor and wrote a function which would check to ensure that we were within tolerances. If not, we blink an LED, set off a buzzer and display a warning on our LCD. A small python script was also written in order to pull our data from ThingSpeak and send it to AdaFruit. Because that script pulls data from the most recent data package we sent to ThingSpeak and we were sending data after every individual sensor, we modified our arduino code to collect all our sensor's data and then send one big packet with data for all of them. Once that was function we were able to forward that data to Adafruit much more easily.

![](https://github.com/mwhol/490IOT/raw/master/Labs/Lab1/Lab1.2.png)
_Our dashboard._

# Workflow

Much of the code was available through the code we wrote for ICP3. We weren't able to add the heartbeat code from ICP2 because we did not have a heartbeat monitor so instead we started incorporating our warning lights, buzzers and on/off switch. While Dan was doing that I was refactoring the arduino code to make our packets to ThingSpeak incorporate all our sensor data and writing a small python script to pull data from ThingSpeak and send it to AdaFruit. Dan then wrote more arduino code to test that our values were in acceptable ranges and then alert the user if not and to incorporate the buttons to create an on/off switch. While he did this I set up the dashboard in Adafruit to display our data.

![](https://github.com/mwhol/490IOT/raw/master/Labs/Lab1/Lab1.1.png)
_python script running and a modification to our Arduino data sending code_

# Circuit Diagram

![](https://github.com/mwhol/490IOT/raw/master/Labs/Lab1/Precautionpic.jpg)

![](https://github.com/mwhol/490IOT/raw/master/Labs/Lab1/Safepic.jpg)

![](https://github.com/mwhol/490IOT/raw/master/Labs/Lab1/Warningpic.jpg)

# Parameters

In this assignment we used an Arduino Uno, a temperature/humidity sensor, a dust sensor, a UV sensor, a light sensor and a barometer as our sensors. We also used an ESP8266, buttons, buzzers, an LCD screen, green and red LEDs, resistors, wires and a breadboard. ThingSpeak was used to transmit our data and then a small python script was used to pull that data and then push it to AdaFruit.

# Evaluation & Discussion

Since this is basically an extension of ICP3, it was very helpful to have that code already. It was a bit rocky because we did not have a heartbeat monitor and did not have very much time to work on it but Dan & I were able to get much of it done.

# Conclusion

It was fun to extend our weather station even further, to play around with another IO dashboard, to write a little python to assist us. It wasn't fun to do it on such a tight time schedule so we'll plan for that next time.