import sys
import tensorflow as tf
import numpy as np
import os

# Functions and classes for loading and using the Inception model v3.
import inception

print ('Tensorflow version ', tf.__version__)

inception.maybe_download()

# Load the Inception model so it is ready for classifying images.
model = inception.Inception()

# Helper-function for classifying and plotting images
def classify(image_path):
    #display(Image(image_path))
    pred = model.classify(image_path=image_path)
    model.print_scores(pred=pred, k=10, only_first_name=True)

def main():
  if len(sys.argv) >= 2:
    image_path = sys.argv[1]
  else:
    print ('###### error ###### you need to specify a valid image')
    sys.exit(1)
  if not os.path.exists(file_path):
    print ('###### error ###### not a valid file path')
    sys.exit(1)

  # We use the test image that comes with inception model v3 if arg 1 is 'test'
  if sys.argv[1] == 'test':
    image_path = os.path.join(inception.data_dir, 'cropped_panda.jpg')

  print ("Classifying image ", image_path)
  print ('###### results ######')
  classify(image_path)

if __name__ == '__main__':
  main()
