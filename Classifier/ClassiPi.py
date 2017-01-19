import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Functions and classes for loading and using the Inception model v3.
from libraries import inception

# Load the Inception model so it is ready for classifying images.
try:
  model = inception.Inception()
except FileNotFoundError:
  print ('###### warning ######')
  print ('this script requires inception.maybe_download() executed at least once, running it now')
  inception.maybe_download()
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
    model.close()
    print ('###### error ######')
    sys.exit('you need to specify a valid image')

  # We use the test image that comes with inception model v3 if arg 1 is 'test'
  if sys.argv[1] == 'test':
    image_path = os.path.join(inception.data_dir, 'cropped_panda.jpg')

  if not os.path.exists(image_path):
    model.close()
    print ('###### error ######')
    sys.exit('not a valid file path')

  print ("Classifying image ", image_path)
  print ('###### results ######')
  import warnings
  with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    classify(image_path)

if __name__ == '__main__':
  main()
