''' Module containing decorator @buildOnObject.
See  help(buildOnObject)  for more.'''

_notFromBase = object()

def buildOnObject(cls):
  '''decorator buildOnObject:

Usage example:

@buildOnObject
class X(superclass):
  ...

x=X(obj,*rest,**kws)
# calls X.__init__(x, *rest, **kws)
# and attaches all attributes directly to the instance of (decorated) X
# so, if obj had  obj.attr = 12, then x.attr will return 12
# and modifying x.attr will directly modify obj.attr
'''

  class Decorated(cls):
    _baseObjs = {}

    def __init__(self, baseObj, *args, **kws):
      Decorated._baseObjs[self] = baseObj
      type(self).__name__ == cls.__name__ + "("+str(baseObj)+")"
      cls.__init__(self, *args, **kws)

    def _fromBaseObj(self, attr):
      if attr.startswith('__') and attr.endswith('__'):
        return _notFromBase
      return getattr(Decorated._baseObjs.get(self, None), attr, _notFromBase)

    def __getattribute__(self, attr):
      val = Decorated._fromBaseObj(self, attr)
      if val == _notFromBase:
        return cls.__getattribute__(self, attr)
      return val

    def __setattr__(self, attr, value):
      if Decorated._fromBaseObj(self, attr) == _notFromBase:
        cls.__setattr__(self, attr, value)
        return
      setattr(Decorated._baseObjs[self], attr, value)

    def __delattr__(self, attr):
      if Decorated._fromBaseObj(self, attr) == _notFromBase:
        cls.__delattr__(self, attr)
        return
      delattr(Decorated._baseObjs[self], attr)

  return Decorated
