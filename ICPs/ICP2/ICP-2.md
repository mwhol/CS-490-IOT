[Here is the code.](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP2/ICP2.ino)

[Here is the video.](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP2/Part1and2Video.mp4?raw=true)


# Introduction

In this assignment we were to build a basic heartbeat monitor. It has many uses inside the home, especially for the sick or elderly who may use it to make sure that they are not having any kind of health issue.

# Objectives

Our hardware/program needs to be set up so that it can measure your heartbeat and then display that heartbeat on a lcd screen. It should then take that heartbeat and send it to a thingspeak channel of our choice so that we are able to remotely access the data. It should also include a green led for a low and stable heartbeat and a red led for extremely high heartbeat. Lastly, it should have three buttons for reset, and to turn off and turn on the LCD.

# Approaches/Methods

Our approach was to immediately begin wiring, adding each additional component one at a time and backtracking, unwiring and rewiring the last component in case of error. The code was mostly correct so if we encountered repeated errors then we went to the code to try and hunt for the error.

# Workflow

First we began wiring. Because the provided code was already (mostly) correct we began pushing the code as we wired in each individual piece. Originally we started with the LCD then we added the heartbeat monitor, then the ESP8266 and so on.

# Circuit Diagram

![Circuit Diagram](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP2/diagram.png?raw=true)

# Parameters

For this ICP we used an Arduino Uno, breadboard, various resistors and wires, an LED, an LCD module, a heartbeat monitor and an ESP2866 (wifi card).

# Evaluation & Discussion

We had two main problems which held us up on this assignment. One was that the first three (!) lcds we tried were all bad. This led to about an hour of wasted time trying to debug. The second was that in the code the line which sends data to Thingspeak was commented out. This similarly led to about an hour of wasted time trying to debug. Without these two things I am confident we could have finished the assignment.

# Conclusion

Fine assignment, we just had a few problems which really screwed us. I expect the next assignment to go better.