''' Python terminal call of functions without parenthesis.
Module contains:
  - class WithoutParenthesis
  - Without()
'''

class WithoutParenthesis(object):
'''  
 usage:
In python terminal, you can call a function without parenthesis, 
if it has no arguments:

>>> @Without()
... def f():
...   print "Hey"
...
>>> f
Hey

equivalently,
>>> def func():
...   pass
...
>>> f = WithoutParenthesis(func)
'''
  def __init__(self, noArgFunc):
    self._func = noArgFunc
    for attr in dir(noArgFunc):
      try:
        setattr(self, attr, getattr(noArgFunc, attr))
      except TypeError: # __class__ cannot be <type 'function'>
        pass
  def __repr__(self):
    self._func()
    return ''
  def __call__(self, *args, **kws):
    self._func(*args, **kws)

def Without():
  return WithoutParenthesis

Without.__doc__ = WithoutParenthesis.__doc__

