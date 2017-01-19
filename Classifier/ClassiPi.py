#%matplotlib inline
#import matplotlib.pyplot as plt
import sys
import tensorflow as tf
import numpy as np
import os

#from util import Util
#u = Util()

# Functions and classes for loading and using the Inception model.
import inception

tf.__version__

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
    image_path = ''
  
  print ("Classifying image", image_path)
  print ('###### results ######')
  classify(image_path)


if __name__ == '__main__':
  main()


