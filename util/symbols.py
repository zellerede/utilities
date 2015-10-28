'''Module for symbols.
After module import, to get symbols created in current namespace, call
  addSymbolsTo(globals())

Usage example

import util.symbols as sym
sym.addSymbolsTo(globals())

romanNumbers = sym.Symbols('I','II','III','IV','V','VI','VII','VIII','IX','X')
print III, repr(X)
print romanNumbers
'''
from lists import ShiftedList

class Symbol(object):
  _globals = globals()
  def __init__(self, name, idx):
    self.name = name
    self.index = idx
  def __repr__(self):
    return "(symbol)%s" % self.name
  def __str__(self):
    return self.name
  def __lt__(self, other):
    return self.index < other.index

def Symbols(*symbols,**instructions):
  ''' use  addSymbolsTo(globals())  or  addSymbolsTo(locals()) before first usage '''

  idx = instructions.get('start', 1)
  symGroup = ShiftedList(shift=idx)
  for sym in symbols:
    Symbol._globals[sym] = Symbol(sym, idx)
    symGroup.append( Symbol._globals[sym] )
    idx += 1
  return symGroup

def addSymbolsTo(namespace):
  ''' This method is needed before usage of Symbols if module is imported. 
Usage:  addSymbolsTo(globals())
    or  addSymbolsTo(locals()) '''
  Symbol._globals = namespace 
