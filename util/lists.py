'''Module of following extended list types:
  - ShiftedList: x=ShiftedList([1,2,3], start=1)  <-- sets starting index of list
                 (we get back list type if shift=0) 

  - CycleList: you can reference list items by any integer index, 
               real index calculated by modulo of current list length
        '''

import sys

class _IdxMachinateList(list):
  def modify(self, idx):
    return idx
  def __getitem__(self, idx):
    return list.__getitem__(self, self.modify(idx))
  def __setitem__(self, idx, value):
    return list.__setitem__(self, self.modify(idx), value)
  def __getslice__(self, start, end):
    if start==0 and end==sys.maxint: # [:]
      return self.__class__(self)
    return list.__getslice__(self, self.modify(start), self.modify(end))
  def __setslice__(self, start, end, value):
    return list.__setslice__(self, self.modify(start), self.modify(end), value)

class ShiftedList(_IdxMachinateList):
  def __init__(self, iterable=[], shift=0):
    _IdxMachinateList.__init__(self, iterable)
    self.start = shift
  def shift(self, num):
    self.start += num
  def modify(self, idx):
    return (idx - self.start)

class CycleList(_IdxMachinateList):
  def modify(self, idx):
    if self:
      return (idx % len(self))
    return idx
  def __getslice__(self, start, end):
    if end==sys.maxint:
      if start==0: # [:]
        return CycleList(self)
      start = self.modify(start)
      end = len(self)
    return [ self[i] 
               for i in range(start, end) ]
  def __setslice__(self, start, end, value):
    _start = self.modify(start)
    _end = self.modify(end)
    list.__setslice__(self, _start, _end, value)
