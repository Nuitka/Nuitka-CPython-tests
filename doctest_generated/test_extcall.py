import test.support as support

try:
    from collections import UserList
except Exception as e:
    print("Occurred", type(e), e)


try:
    from collections import UserDict
except Exception as e:
    print("Occurred", type(e), e)


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
    print("Occurred", type(e), e)


try:
    print('Line 23')
    print(f()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 26')
    print(f(1)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 29')
    print(f(1, 2)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 32')
    print(f(1, 2, 3)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 35')
    print(f(1, 2, 3, *(4, 5))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 38')
    print(f(1, 2, 3, *[4, 5])
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 41')
    print(f(*[1, 2, 3], 4, 5)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 44')
    print(f(1, 2, 3, *UserList([4, 5]))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 47')
    print(f(1, 2, 3, *[4, 5], *[6, 7])
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 50')
    print(f(1, *[2, 3], 4, *[5, 6], 7)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 53')
    print(f(*UserList([1, 2]), *UserList([3, 4]), 5, *UserList([6, 7]))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 59')
    print(f(1, 2, 3, **{'a':4, 'b':5})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 62')
    print(f(1, 2, **{'a': -1, 'b': 5}, **{'a': 4, 'c': 6})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 67')
    print(f(1, 2, **{'a': -1, 'b': 5}, a=4, c=6)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 72')
    print(f(1, 2, 3, *[4, 5], **{'a':6, 'b':7})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 75')
    print(f(1, 2, 3, x=4, y=5, *(6, 7), **{'a':8, 'b': 9})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 78')
    print(f(1, 2, 3, *[4, 5], **{'c': 8}, **{'a':6, 'b':7})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 81')
    print(f(1, 2, 3, *(4, 5), x=6, y=7, **{'a':8, 'b': 9})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 85')
    print(f(1, 2, 3, **UserDict(a=4, b=5))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 88')
    print(f(1, 2, 3, *(4, 5), **UserDict(a=6, b=7))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 91')
    print(f(1, 2, 3, x=4, y=5, *(6, 7), **UserDict(a=8, b=9))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 94')
    print(f(1, 2, 3, *(4, 5), x=6, y=7, **UserDict(a=8, b=9))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 103')
    print(e(c=4)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 109')
    print(g()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 115')
    print(g(*())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 121')
    print(g(*(), **{})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 127')
    print(g(1)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 130')
    print(g(1, 2)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 133')
    print(g(1, 2, 3)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 136')
    print(g(1, 2, 3, *(4, 5))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    class Nothing: pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 141')
    print(g(*Nothing())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    class Nothing:
        def __len__(self): return 5
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 150')
    print(g(*Nothing())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    class Nothing():
        def __len__(self): return 5
        def __getitem__(self, i):
            if i<3: return i
            else: raise IndexError(i)
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 162')
    print(g(*Nothing())
    )

except Exception as e:
    print("Occurred", type(e), e)


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
    print("Occurred", type(e), e)


try:
    print('Line 176')
    print(g(*Nothing())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    d = {'a': 1, 'b': 2, 'c': 3}
except Exception as e:
    print("Occurred", type(e), e)


try:
    d2 = d.copy()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 184')
    print(g(1, d=4, **d)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 187')
    print(d == d2
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def saboteur(**kw):
        kw['x'] = 'm'
        return kw
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    d = {}
except Exception as e:
    print("Occurred", type(e), e)


try:
    kw = saboteur(a=1, **d)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 199')
    print(d
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 204')
    print(g(1, 2, 3, **{'x': 4, 'y': 5})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 210')
    print(f(**{1:2})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 216')
    print(h(**{'e': 2})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 222')
    print(h(*h)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 228')
    print(dir(*h)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 234')
    print(None(*h)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 240')
    print(h(**h)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 246')
    print(dir(**h)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 252')
    print(None(**h)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 258')
    print(dir(b=1, **{'b': 1})
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f2(*a, **b):
        return a, b
    #
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    d = {}
except Exception as e:
    print("Occurred", type(e), e)


try:
    for i in range(512):
        key = 'k%d' % i
        d[key] = i
except Exception as e:
    print("Occurred", type(e), e)


try:
    a, b = f2(1, *(2,3), **d)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 275')
    print(len(a), len(b), b == d
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    class Foo:
        def method(self, arg1, arg2):
            return arg1+arg2
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    x = Foo()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 284')
    print(Foo.method(*(x, 1, 2))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 287')
    print(Foo.method(x, *(1, 2))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 290')
    print(Foo.method(*(1, 2, 3))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 293')
    print(Foo.method(1, *[2, 3])
    )

except Exception as e:
    print("Occurred", type(e), e)


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
    print("Occurred", type(e), e)


try:
    print('Line 309')
    print(id(1, **{'foo': 1})
    )

except Exception as e:
    print("Occurred", type(e), e)


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
    print("Occurred", type(e), e)


try:
    x = {Name("a"):1, Name("b"):2}
except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a, b):
        print(a,b)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 331')
    print(f(**x)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 338')
    print(f(1)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 344')
    print(f(1, 2)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a, b=1): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 350')
    print(f(1, 2, 3)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(*, kw): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 356')
    print(f(1, kw=3)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(*, kw, b): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 362')
    print(f(1, 2, 3, b=3, kw=3)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a, b=2, *, kw): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 368')
    print(f(2, 3, 4, kw=4)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 377')
    print(f()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a, b): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 383')
    print(f()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a, b, c): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 389')
    print(f()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a, b, c, d, e): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 395')
    print(f()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(a, b=4, c=5, d=5): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 401')
    print(f(c=12, b=9)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(*, w): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 410')
    print(f()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(*, a, b, c, d, e): pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 416')
    print(f()
    )

except Exception as e:
    print("Occurred", type(e), e)
