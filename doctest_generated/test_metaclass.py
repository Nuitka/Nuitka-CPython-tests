
try:
    class C:
        def meth(self): print("Hello")
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 4')
    print(C.__class__ is type
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a = C()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 8')
    print(a.__class__ is C
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 11')
    print(a.meth()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class A: pass
    class B: pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    bases = (A, B)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class C(*bases): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 21')
    print(C.__bases__ == bases
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class M(type):
        pass
    class C(metaclass=M):
       def meth(self): print("Hello")
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 31')
    print(C.__class__ is M
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a = C()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 35')
    print(a.__class__ is C
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 38')
    print(a.meth()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    kwds = {'metaclass': M}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class C(**kwds): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 46')
    print(C.__class__ is M
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a = C()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 50')
    print(a.__class__ is C
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class M(type):
       @staticmethod
       def __prepare__(*args, **kwds):
           print("Prepare called:", args, kwds)
           return dict()
       def __new__(cls, name, bases, namespace, **kwds):
           print("New called:", kwds)
           return type.__new__(cls, name, bases, namespace)
       def __init__(cls, *args, **kwds):
           pass
    class C(metaclass=M):
        def meth(self): print("Hello")
    # Expected:
    ## Prepare called: ('C', ()) {}
    ## New called: {}
    #
    # Also pass another keyword.
    #
    class C(object, metaclass=M, other="haha"):
        pass
    # Expected:
    ## Prepare called: ('C', (<class 'object'>,)) {'other': 'haha'}
    ## New called: {'other': 'haha'}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 79')
    print(C.__class__ is M
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 82')
    print(C.__bases__ == (object,)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a = C()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 86')
    print(a.__class__ is C
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    kwds = {'metaclass': type}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class C(**kwds): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 94')
    print(kwds == {'metaclass': type}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    bases = (object,)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    kwds = {'metaclass': M, 'other': 'haha'}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class C(*bases, **kwds): pass
    # Expected:
    ## Prepare called: ('C', (<class 'object'>,)) {'other': 'haha'}
    ## New called: {'other': 'haha'}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 106')
    print(C.__class__ is M
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 109')
    print(C.__bases__ == (object,)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class B: pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    kwds = {'other': 'haha'}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class C(B, metaclass=M, *bases, **kwds): pass
    # Expected:
    ## Prepare called: ('C', (<class 'test.test_metaclass.B'>, <class 'object'>)) {'other': 'haha'}
    ## New called: {'other': 'haha'}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 118')
    print(C.__class__ is M
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 121')
    print(C.__bases__ == (B, object)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class LoggingDict(dict):
        def __setitem__(self, key, value):
            print("d[%r] = %r" % (key, value))
            dict.__setitem__(self, key, value)
    class Meta(type):
       @staticmethod
       def __prepare__(name, bases):
           return LoggingDict()
    class C(metaclass=Meta):
        foo = 2+2
        foo = 42
        bar = 123
    # Expected:
    ## d['__module__'] = 'test.test_metaclass'
    ## d['__qualname__'] = 'C'
    ## d['foo'] = 4
    ## d['foo'] = 42
    ## d['bar'] = 123
    #
    # Use a metaclass that doesn't derive from type.
    #
    def meta(name, bases, namespace, **kwds):
        print("meta:", name, bases)
        print("ns:", sorted(namespace.items()))
        print("kw:", sorted(kwds.items()))
        return namespace
    class C(metaclass=meta):
        a = 42
        b = 24
    # Expected:
    ## meta: C ()
    ## ns: [('__module__', 'test.test_metaclass'), ('__qualname__', 'C'), ('a', 42), ('b', 24)]
    ## kw: []
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 173')
    print(type(C) is dict
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 176')
    print(print(sorted(C.items()))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def prepare(name, bases, **kwds):
        print("prepare:", name, bases, sorted(kwds.items()))
        return LoggingDict()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    meta.__prepare__ = prepare
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class C(metaclass=meta, other="booh"):
       a = 1
       a = 2
       b = 3
    # Expected:
    ## prepare: C () [('other', 'booh')]
    ## d['__module__'] = 'test.test_metaclass'
    ## d['__qualname__'] = 'C'
    ## d['a'] = 1
    ## d['a'] = 2
    ## d['b'] = 3
    ## meta: C ()
    ## ns: [('__module__', 'test.test_metaclass'), ('__qualname__', 'C'), ('a', 2), ('b', 3)]
    ## kw: [('other', 'booh')]
    #
    # The default metaclass must define a __prepare__() method.
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 203')
    print(type.__prepare__()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class M(type):
        @classmethod
        def __prepare__(cls, *args, **kwds):
            d = super().__prepare__(*args, **kwds)
            d["hello"] = 42
            return d
    class C(metaclass=M):
        print(hello)
    # Expected:
    ## 42
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 219')
    print(print(C.hello)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)
