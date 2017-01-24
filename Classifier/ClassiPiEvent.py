import sys
import signal
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import time
from datetime import timedelta

# Functions and classes for loading and using the Inception model v3.
import inception

import pyinotify

model = 0

class ProcessTransientFile(pyinotify.ProcessEvent):
    # Load the Inception model so it is ready for classifying images.
    try:
      model = inception.Inception()
    except FileNotFoundError:
      print ('###### warning ######')
      print ('this script requires inception.maybe_download() executed at least once, running it now')
      inception.maybe_download()
      model = inception.Inception()

    def process_IN_MODIFY(self, event):
        # We have explicitely registered for this kind of event.
        print (event.pathname, ' -> written')
        main(model, event.pathname)

    def process_default(self, event):
        # Implicitely IN_CREATE and IN_DELETE are watched too. You can
        # ignore them and provide an empty process_default or you can
        # process them, either with process_default or their dedicated
        # method (process_IN_CREATE, process_IN_DELETE) which would
        # override process_default.
        # print 'default: ', event.maskname
        main(model, 'test')



# Helper-function for classifying and plotting images
def classify(model, image_path):
    #display(Image(image_path))
    pred = model.classify(image_path=image_path)
    model.print_scores(pred=pred, k=10, only_first_name=True)

def main(model, path):
  start_time = time.time()
  if not path:
    print ('###### error ######')
    print('you need to specify a valid image')
    return

  # We use the test image that comes with inception model v3 if arg 1 is 'test'
  if path == 'test':
    print ('###### test ######')
    image_path = os.path.join(inception.data_dir, 'cropped_panda.jpg')
  else:
    image_path = path

  if not os.path.exists(image_path):
    print ('###### error ######')
    print('not a valid file path')
    return

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

def exit_gracefully(self, signum, frame):
  # stuff to run when process is closed
  model.close()

if __name__ == '__main__':
  signal.signal(signal.SIGTERM, exit_gracefully)
  wm = pyinotify.WatchManager()
  notifier = pyinotify.Notifier(wm)
  # In this case you must give the class object (ProcessTransientFile)
  # as last parameter not a class instance.
  wm.watch_transient_file('/tmp/image_to_classify.jpg', pyinotify.IN_MODIFY, ProcessTransientFile)
  notifier.loop()




