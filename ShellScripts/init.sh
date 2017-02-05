#!/bin/sh
cd ~/ClassiPi/Classifier/
forever stopall
forever start ~/ClassiPi/ClassiPiMonitor/bin/www
python3  ~/ClassiPi/Classifier/ClassiPiLoopCamera.py
