''' Module containing  PrintTo  and  SavePrint  contexts. 
Type  help(PrintTo)  once imported.
'''

import sys
from StringIO import StringIO

# with context
class PrintTo(object):
  '''\
Redirects system stdout to given file type object.
Usage:
------
from util.pr2 import PrintTo
with PrintTo('outfile.txt'):
  print "This line is written in outfile.txt"
  func() # and also everything that  func()  is printing.
'''
  def __init__(self, filename):
    self.filename = filename
  def __enter__(self):
    self.file = open(self.filename, 'w')
    self.stdout = sys.stdout
    sys.stdout = self.file
  def __exit__(self, exc_type, exc_value, traceback):
    sys.stdout = self.stdout
    self.file.close()

class displayableStringIO(StringIO):
  def __repr__(self):
    return repr(self.getvalue())
  def __str__(self):
    return str(self.getvalue())
  def close(self):
    pass # self.closed = True

class SavePrint(object):
  '''\
Usage:
------
from util.pr2 import SavePrint
with SavePrint() as resultStr:
  print "This will be retrieved in string resultStr"
  func() # and also anything that is printed here

-- resultStr  is a displayable StringIO object.
To obtain a real string, use either   
  resultStr.getvalue()  or  str(resultStr)  (or equivalent)
'''
  def __enter__(self):
    self.stdout = sys.stdout
    printedString = sys.stdout = displayableStringIO(StringIO)
    return printedString
  def __exit__(self, exc_type, exc_value, traceback):
    sys.stdout = self.stdout
