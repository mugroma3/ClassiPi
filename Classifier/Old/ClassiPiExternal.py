import sys
import signal
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import warnings
import time
from datetime import timedelta

# Functions and classes for loading and using the Inception model v3.
import inception

image_path = 'image.jpg'

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
      start_time = time.time()
      print ("Classifying image from camera...")
      with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        classify(model=model, image_path=image_path)
      end_time = time.time()
      time_dif = end_time - start_time
      print ('###### time usage NN ######')
      print(str(timedelta(seconds=int(round(time_dif)))))

    except (KeyboardInterrupt, SystemExit, RuntimeError, SystemError):
      model.close()

def exit_gracefully(self, signum, frame):
  # stuff to run when process is closed
  model.close()

if __name__ == '__main__':
  signal.signal(signal.SIGTERM, exit_gracefully)
  main()
