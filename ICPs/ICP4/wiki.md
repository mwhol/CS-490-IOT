[Here's the video.](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP4/ICP4.mp4?raw=true)

[Here is the code.](https://github.com/mwhol/490IOT/blob/master/ICPs/ICP4/icp4.3.json)

# Introduction

In this assignment we were to set up a basic flow in Node-RED that takes data from a weather api and uses it to tweet.

# Objectives

We were to install Node-RED and then setup a flow such that we pulled the current weather from a weather api and then tweeted it.

# Approaches/Methods

I started by playing around with the debugger a little since I'm not too familiar with javascript. Once I felt I understood the message/payload system a little better, I started setting up the flow.

# Workflow

Once I had the debugger working, I setup a node to manipulate the payload, inserted the weather node, then tested it with the tweet. I had to regenerate api keys for twitter and then it worker!

# Circuit Diagram

![](https://github.com/mwhol/490IOT/raw/master/ICPs/ICP4/Diagram.png)

# Parameters

We used Node-RED, openweather api keys and twitter api keys.

# Evaluation

Good lesson, it took a little bit of playing around to get my api keys working but other than that everything flowed fine.

# Conclusion

The software side is way easier!