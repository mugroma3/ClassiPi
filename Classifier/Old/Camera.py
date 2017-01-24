import sys
import signal
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import time
from datetime import timedelta

import pygame
import pygame.camera
import pygame.surfarray

from PIL import Image
import numpy as np

image_path = 'image.jpg'

# getting image from camera
pygame.camera.init()
# pygame.camera.list_camera() #Camera detected or not
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start();

def main():
  while True:
    try:
      print ('Saving image from camera...')
      start_time_camera = time.time()

      img = cam.get_image()
      pygame.image.save(img, image_path)
      
      end_time_camera =time.time()
      time_dif_camera = end_time_camera - start_time_camera

      # Print the time-usage.
      os.system('cls' if os.name == 'nt' else 'clear')
      print ('###### time usage camera ######')
      print(str(timedelta(seconds=int(round(time_dif_camera)))))
    except (KeyboardInterrupt, SystemExit, RuntimeError, SystemError):
      cam.stop()

def exit_gracefully(self, signum, frame):
  # stuff to run when process is closed
  cam.stop()

if __name__ == '__main__':
  signal.signal(signal.SIGTERM, exit_gracefully)
  main()
