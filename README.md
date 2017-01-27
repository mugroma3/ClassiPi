# ClassiPi <img src="/logo.png" width="60" alt="logo" />


A robot that can understand what's in front of it thanks to a convolutional neural network (Inception model V3 by Google).

Everything runs with Python3 on Raspberry Pi 3 with a usb webcam.

![Inception V3 Architecture](inceptionV3Architecture.png)
Inception model V3 is a CNN by Google trained using ImageNet and impossible to train on an ordinary PC. We instead download the pre-trained Inception model and use it to classify images with a very simple python script. 
We provide a continuous stream of pictures capturing them from a webcam and the classification of what the robot is looking at is provided on a screen and also used to look around in order to find a target object. 
