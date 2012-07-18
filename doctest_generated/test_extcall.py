import test.test_support as test_support

try:
    from collections import UserList
except Exception as e:
    print( "Occured", type(e), e )


try:
    from collections import UserDict
except Exception as e:
    print( "Occured", type(e), e )


try:
    def e(a,b):
        print(a, b)
    #
    def f(*a, **k):
        print(a, support.sortdict(k))
    #
    def g(x, *y, **z):
        print(x, y, support.sortdict(z))
    #
    def h(j=1, a=2, h=3):
        print(j, a, h)
    #
    # Argument list examples
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    f()
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2)
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3)
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, *(4, 5))
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, *[4, 5])
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, *UserList([4, 5]))
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, **{'a':4, 'b':5})
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, *[4, 5], **{'a':6, 'b':7})
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, x=4, y=5, *(6, 7), **{'a':8, 'b': 9})
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, **UserDict(a=4, b=5))
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, *(4, 5), **UserDict(a=6, b=7))
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(1, 2, 3, x=4, y=5, *(6, 7), **UserDict(a=8, b=9))
except Exception as e:
    print( "Occured", type(e), e )


try:
    e(c=4)
except Exception as e:
    print( "Occured", type(e), e )


try:
    g()
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(*())
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(*(), **{})
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(1, 2)
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(1, 2, 3)
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(1, 2, 3, *(4, 5))
except Exception as e:
    print( "Occured", type(e), e )


try:
    class Nothing: pass
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(*Nothing())
except Exception as e:
    print( "Occured", type(e), e )


try:
    class Nothing:
        def __len__(self): return 5
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(*Nothing())
except Exception as e:
    print( "Occured", type(e), e )


try:
    class Nothing():
        def __len__(self): return 5
        def __getitem__(self, i):
            if i<3: return i
            else: raise IndexError(i)
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(*Nothing())
except Exception as e:
    print( "Occured", type(e), e )


try:
    class Nothing:
        def __init__(self): self.c = 0
        def __iter__(self): return self
        def __next__(self):
            if self.c == 4:
                raise StopIteration
            c = self.c
            self.c += 1
            return c
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(*Nothing())
except Exception as e:
    print( "Occured", type(e), e )


try:
    d = {'a': 1, 'b': 2, 'c': 3}
except Exception as e:
    print( "Occured", type(e), e )


try:
    d2 = d.copy()
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(1, d=4, **d)
except Exception as e:
    print( "Occured", type(e), e )


try:
    d == d2
except Exception as e:
    print( "Occured", type(e), e )


try:
    def saboteur(**kw):
        kw['x'] = 'm'
        return kw
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    d = {}
except Exception as e:
    print( "Occured", type(e), e )


try:
    kw = saboteur(a=1, **d)
except Exception as e:
    print( "Occured", type(e), e )


try:
    d
except Exception as e:
    print( "Occured", type(e), e )


try:
    g(1, 2, 3, **{'x': 4, 'y': 5})
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(**{1:2})
except Exception as e:
    print( "Occured", type(e), e )


try:
    h(**{'e': 2})
except Exception as e:
    print( "Occured", type(e), e )


try:
    h(*h)
except Exception as e:
    print( "Occured", type(e), e )


try:
    dir(*h)
except Exception as e:
    print( "Occured", type(e), e )


try:
    None(*h)
except Exception as e:
    print( "Occured", type(e), e )


try:
    h(**h)
except Exception as e:
    print( "Occured", type(e), e )


try:
    dir(**h)
except Exception as e:
    print( "Occured", type(e), e )


try:
    None(**h)
except Exception as e:
    print( "Occured", type(e), e )


try:
    dir(b=1, **{'b': 1})
except Exception as e:
    print( "Occured", type(e), e )


try:
    def f2(*a, **b):
        return a, b
    #
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    d = {}
except Exception as e:
    print( "Occured", type(e), e )


try:
    for i in range(512):
        key = 'k%d' % i
        d[key] = i
except Exception as e:
    print( "Occured", type(e), e )


try:
    a, b = f2(1, *(2,3), **d)
except Exception as e:
    print( "Occured", type(e), e )


try:
    len(a), len(b), b == d
except Exception as e:
    print( "Occured", type(e), e )


try:
    class Foo:
        def method(self, arg1, arg2):
            return arg1+arg2
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    x = Foo()
except Exception as e:
    print( "Occured", type(e), e )


try:
    Foo.method(*(x, 1, 2))
except Exception as e:
    print( "Occured", type(e), e )


try:
    Foo.method(x, *(1, 2))
except Exception as e:
    print( "Occured", type(e), e )


try:
    Foo.method(*(1, 2, 3))
except Exception as e:
    print( "Occured", type(e), e )


try:
    Foo.method(1, *[2, 3])
except Exception as e:
    print( "Occured", type(e), e )


try:
    try:
        silence = id(1, *{})
        True
    except:
        False
    # Expected:
    ## True
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    id(1, **{'foo': 1})
except Exception as e:
    print( "Occured", type(e), e )


try:
    class Name(str):
        def __eq__(self, other):
            try:
                 del x[self]
            except KeyError:
                 pass
            return str.__eq__(self, other)
        def __hash__(self):
            return str.__hash__(self)
    #
except Exception as e:
    print( "Occured", type(e), e )


try:
    x = {Name("a"):1, Name("b"):2}
except Exception as e:
    print( "Occured", type(e), e )


try:
    def f(a, b):
        print(a,b)
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(**x)
except Exception as e:
    print( "Occured", type(e), e )


try:
    def f(a, b):
       pass
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(b=1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    def f(a):
       pass
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(6, a=4, *(1, 2, 3))
except Exception as e:
    print( "Occured", type(e), e )


try:
    def f(a, *, kw):
       pass
except Exception as e:
    print( "Occured", type(e), e )


try:
    f(6, 4, kw=4)
except Exception as e:
    print( "Occured", type(e), e )
