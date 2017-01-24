import sys
import signal
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import warnings
import time
from datetime import timedelta

# Functions and classes for loading and using the Inception model v3.
import inception

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

# Making model global
model = None

# Helper-function for classifying and plotting images
def classify(model, image_path=None, image=None):
    #display(Image(image_path))
    if image_path:
        pred = model.classify(image_path=image_path)
    else:
        pred = model.classify(image=image)
    # clear commands
    os.system('cls' if os.name == 'nt' else 'clear')
    print ('###### results ######')
    model.print_scores(pred=pred, k=10, only_first_name=True)

def main():

  # Load the Inception model so it is ready for classifying images.
  try:
    model = inception.Inception()
  except FileNotFoundError:
    print ('###### warning ######')
    print ('this script requires inception.maybe_download() executed at least once, running it now')
    inception.maybe_download()
    model = inception.Inception()
  while True:
    try:
      start_time_camera = time.time()
    
      cam.start() 
      # start and stop prevent the buffer from filling up with more useless frames
      img = cam.get_image()
      cam.stop()
      image = pygame.surfarray.array3d(img)
      image = np.rot90(image, 3)
      end_time_camera = time.time()
      
      start_time = time.time()
      print ("Classifying image from camera...")
      with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        classify(model=model, image=image)
      end_time = time.time()
      time_dif_camera = end_time_camera - start_time_camera
      time_dif = end_time - start_time

      # Print the time-usage.
      print ('###### time usage camera ######')
      print(str(timedelta(seconds=int(round(time_dif_camera)))))
      print ('###### time usage NN ######')
      print(str(timedelta(seconds=int(round(time_dif)))))

      # Save the image that was just classified (for debug)
      im = Image.fromarray(image) 
      im.save(image_path)
    except (KeyboardInterrupt, SystemExit, RuntimeError, SystemError):
      cam.stop()
      model.close()

def exit_gracefully(self, signum, frame):
  # stuff to run when process is closed
  model.close()

if __name__ == '__main__':
  signal.signal(signal.SIGTERM, exit_gracefully)
  main()
