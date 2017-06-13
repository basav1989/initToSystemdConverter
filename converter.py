import os

class converter:
   def __init__(self):
      self.initFiles = []
      self.systemdFiles = []
   def initialise(self, dir=None):
      # first build existing file list
      if dir is None:
	 lis = os.listdir("/etc/init")
      else:
	 lis = os.listdir(dir)
      for fileName in lis:
	 if fileName.endswith('.conf'):
	    self.initFiles.append(fileName)
	 else:
	    print ("not a init conf file")
   def stats(self):
      print("total initfiles found: %d " % len(self.initFiles))


conv = converter()
conv.initialise("/etc/init")
conv.stats()
