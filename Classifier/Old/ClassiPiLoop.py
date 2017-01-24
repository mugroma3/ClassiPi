import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import time
from datetime import timedelta

# Functions and classes for loading and using the Inception model v3.
import inception

# Helper-function for classifying and plotting images
def classify(model, image_path):
    #display(Image(image_path))
    pred = model.classify(image_path=image_path)
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
    print ('###### input ######')
    line = input()
    if line:
      start_time = time.time()

      if not line:
        print ('###### error ######')
        print('you need to specify a valid image')
        continue
      
      if line == 'quit':
        break

      # We use the test image that comes with inception model v3 if arg 1 is 'test'
      if line == 'test':
        image_path = os.path.join(inception.data_dir, 'cropped_panda.jpg')
      else:
        image_path = line

      if not os.path.exists(image_path):
        print ('###### error ######')
        print('not a valid file path')
        continue

      print ("Classifying image ", image_path)
      print ('###### results ######')
      import warnings
      with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        classify(model, image_path)
      end_time = time.time()
      time_dif = end_time - start_time
      # Print the time-usage.
      print ('###### time usage ######')
      print(str(timedelta(seconds=int(round(time_dif)))))
    else:
      break
  model.close()

if __name__ == '__main__':
  main()
