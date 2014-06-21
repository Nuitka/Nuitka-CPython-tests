from test.test_descrtut import defaultdict,defaultdict2,sortdict
import pprint

try:
    class property(object):

        def __init__(self, get, set=None):
            self.__get = get
            self.__set = set

        def __get__(self, inst, type=None):
            return self.__get(inst)

        def __set__(self, inst, value):
            if self.__set is None:
                raise AttributeError("this attribute is read-only")
            return self.__set(inst, value)
    #
    # Now let's define a class with an attribute x defined by a pair of methods,
    # getx() and setx():
    #
    class C(object):

        def __init__(self):
            self.__x = 0

        def getx(self):
            return self.__x

        def setx(self, x):
            if x < 0: x = 0
            self.__x = x

        x = property(getx, setx)
    #
    # Here's a small demonstration:
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    a = C()
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.x = 10
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a.x)
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.x = -10
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a.x)
except Exception as e:
    print( "Occured", type(e), e )


try:
    del property  # unmask the builtin
except Exception as e:
    print( "Occured", type(e), e )


try:
    property
except Exception as e:
    print( "Occured", type(e), e )


try:
    class C(object):
        def __init__(self):
            self.__x = 0
        def getx(self):
            return self.__x
        def setx(self, x):
            if x < 0: x = 0
            self.__x = x
        x = property(getx, setx)
    #
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    a = C()
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.x = 10
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a.x)
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.x = -10
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a.x)
except Exception as e:
    print( "Occured", type(e), e )

try:
    class C:

        @staticmethod
        def foo(x, y):
            print("staticmethod", x, y)
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    C.foo(1, 2)
except Exception as e:
    print( "Occured", type(e), e )


try:
    c = C()
except Exception as e:
    print( "Occured", type(e), e )


try:
    c.foo(1, 2)
except Exception as e:
    print( "Occured", type(e), e )


try:
    class C:
        @classmethod
        def foo(cls, y):
            print("classmethod", cls, y)
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    C.foo(1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    c = C()
except Exception as e:
    print( "Occured", type(e), e )


try:
    c.foo(1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    class D(C):
        pass
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    D.foo(1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    d = D()
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.foo(1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    class E(C):
        @classmethod
        def foo(cls, y): # override C.foo
            print("E.foo() called")
            C.foo(y)
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    E.foo(1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    e = E()
except Exception as e:
    print( "Occured", type(e), e )


try:
    e.foo(1)
except Exception as e:
    print( "Occured", type(e), e )

try:
    print(D().m()) # "DCBA"
except Exception as e:
    print( "Occured", type(e), e )

try:
    class A:    # implicit new-style class
        def save(self):
            print("called A.save()")
    class B(A):
        pass
    class C(A):
        def save(self):
            print("called C.save()")
    class D(B, C):
        pass
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    D().save()
except Exception as e:
    print( "Occured", type(e), e )


try:
    class A(object):  # explicit new-style class
        def save(self):
            print("called A.save()")
    class B(A):
        pass
    class C(A):
        def save(self):
            print("called C.save()")
    class D(B, C):
        pass
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    D().save()
except Exception as e:
    print( "Occured", type(e), e )

try:
    print(defaultdict)              # show our type
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(type(defaultdict))        # its metatype
except Exception as e:
    print( "Occured", type(e), e )


try:
    a = defaultdict(default=0.0)    # create an instance
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a)                        # show the instance
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(type(a))                  # show its type
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a.__class__)              # show its class
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(type(a) is a.__class__)   # its type is its class
except Exception as e:
    print( "Occured", type(e), e )


try:
    a[1] = 3.25                     # modify the instance
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a)                        # show the new value
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a[1])                     # show the new item
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a[0])                     # a non-existent item
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.merge({1:100, 2:200})         # use a dict method
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(sortdict(a))              # show the result
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(sorted(a.keys()))
except Exception as e:
    print( "Occured", type(e), e )


try:
    a['print'] = print              # need the print function here
except Exception as e:
    print( "Occured", type(e), e )


try:
    exec("x = 3; print(x)", a)
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(sorted(a.keys(), key=lambda x: (str(type(x)), x)))
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a['x'])
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.default = -1
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a["noway"])
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.default = -1000
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a["noway"])
except Exception as e:
    print( "Occured", type(e), e )


try:
    'default' in dir(a)
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.x1 = 100
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.x2 = 200
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(a.x1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    d = dir(a)
except Exception as e:
    print( "Occured", type(e), e )


try:
    'default' in d and 'x1' in d and 'x2' in d
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(sortdict(a.__dict__))
except Exception as e:
    print( "Occured", type(e), e )

try:
    type([])
except Exception as e:
    print( "Occured", type(e), e )


try:
    [].__class__
except Exception as e:
    print( "Occured", type(e), e )


try:
    list
except Exception as e:
    print( "Occured", type(e), e )


try:
    isinstance([], list)
except Exception as e:
    print( "Occured", type(e), e )


try:
    isinstance([], dict)
except Exception as e:
    print( "Occured", type(e), e )


try:
    isinstance([], object)
except Exception as e:
    print( "Occured", type(e), e )


try:
    pprint.pprint(dir(list))    # like list.__dict__.keys(), but sorted
except Exception as e:
    print( "Occured", type(e), e )


try:
    a = ['tic', 'tac']
except Exception as e:
    print( "Occured", type(e), e )


try:
    list.__len__(a)          # same as len(a)
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.__len__()              # ditto
except Exception as e:
    print( "Occured", type(e), e )


try:
    list.append(a, 'toe')    # same as a.append('toe')
except Exception as e:
    print( "Occured", type(e), e )


try:
    a
except Exception as e:
    print( "Occured", type(e), e )

try:
    a = defaultdict2(default=0.0)
except Exception as e:
    print( "Occured", type(e), e )


try:
    a[1]
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.default = -1
except Exception as e:
    print( "Occured", type(e), e )


try:
    a[1]
except Exception as e:
    print( "Occured", type(e), e )


try:
    a.x1 = 1
except Exception as e:
    print( "Occured", type(e), e )

try:
    class A:
        def foo(self):
            print("called A.foo()")
    #
    class B(A):
        pass
    #
    class C(A):
        def foo(self):
            B.foo(self)
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    C().foo()
except Exception as e:
    print( "Occured", type(e), e )


try:
    class C(A):
        def foo(self):
            A.foo(self)
except Exception as e:
    print( "Occured", type(e), e )


try:
    C().foo()
except Exception as e:
    print( "Occured", type(e), e )
