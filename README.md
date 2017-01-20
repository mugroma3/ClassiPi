# ClassiPi <img src="/logo.png" width="60" alt="logo" />


A robot that can understand what's in front of it thanks to a convolutional neural network (Inception model V3 by Google).

Everything runs on [Raspberry Pi 1](https://www.raspberrypi.org/products/model-b/) using [Raspbian](https://www.raspbian.org/) and a webcam.

![Inception V3 Architecture](inceptionV3Architecture.png)
Inception model V3 is a CNN by Google that takes weeks to train on a computer with 8 Tesla K40 GPUs and is impossible to train it on an ordinary PC. We will instead download the pre-trained Inception model and use it to classify images with a very simple python script. 
We also provide a continuous stream of pictures capturing them from a webcam. The classification of what the robot is looking at is provided on a screen and used to look around to find a target object. 
