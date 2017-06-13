import os

class tokenizer:
   def __init__(self):
      self.initFiles = []
      self.systemdFiles = []
      self.directory = ""
      self.eventMap = {}
   def initialise(self, dir=None):
      # first build existing file list
      if dir is None:
	 lis = os.listdir("/etc/init")
      else:
	 lis = os.listdir(dir)
      self.directory = dir
      for fileName in lis:
	 if fileName.endswith('.conf'):
	    self.initFiles.append(fileName)
	 else:
	    print ("not a init conf file")
   def generateEventDependencyMap(self):
      for conf in self.initFiles:
	 name = os.path.join(self.directory, conf)
	 hdl = open(name)
         print hdl.read()
   def stats(self):
      print("total initfiles found: %d " % len(self.initFiles))

class converter:
   def __init__(self):
      self.tokenizer = tokenizer()
   def initialise(self):
      self.tokenizer.initialise("/etc/init")
   def trace(self):
      self.tokenizer.generateEventDependencyMap()
      self.tokenizer.stats()

conv = converter()
conv.initialise()
conv.trace()
