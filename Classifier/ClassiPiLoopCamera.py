import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import time
from datetime import timedelta

# Functions and classes for loading and using the Inception model v3.
import inception

import pygame
import pygame.camera

image_path = 'image.jpg'

# Helper-function for classifying and plotting images
def classify(model, image_path):
    #display(Image(image_path))
    pred = model.classify(image_path=image_path)
    # clear commands
    os.system('cls' if os.name == 'nt' else 'clear')
    print ('###### results ######')
    model.print_scores(pred=pred, k=10, only_first_name=True)

def main():
  # getting image from camera
  pygame.camera.init()
  img = 0
  #pygame.camera.list_camera() #Camera detected or not
  cam = pygame.camera.Camera("/dev/video0",(640,480))
  
  # Load the Inception model so it is ready for classifying images.
  try:
    model = inception.Inception()
  except FileNotFoundError:
    print ('###### warning ######')
    print ('this script requires inception.maybe_download() executed at least once, running it now')
    inception.maybe_download()
    model = inception.Inception()
  while True:
    print ('###### input ######')
    start_time = time.time()
    
    #os.remove(image_path)
    cam.start()
    if img == 0:
      img = cam.get_image()
    else:
      img = cam.get_image(img)
    pygame.image.save(img,image_path)
    cam.stop()

    if not os.path.exists(image_path):
      print ('###### error ######')
      print('not a valid file path')
      continue

    print ("Classifying image ", image_path)
    
    import warnings
    with warnings.catch_warnings():
      warnings.simplefilter("ignore")
      classify(model, image_path)
    end_time = time.time()
    time_dif = end_time - start_time
    # Print the time-usage.
    print ('###### time usage ######')
    print(str(timedelta(seconds=int(round(time_dif)))))

  model.close()

if __name__ == '__main__':
  main()
