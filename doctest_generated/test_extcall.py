import test.support as support

try:
    from collections import UserList
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    from collections import UserDict
except Exception as __e:
    print("Occurred", type(__e), __e)


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
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 23')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 26')
    print(f(1)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 29')
    print(f(1, 2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 32')
    print(f(1, 2, 3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 35')
    print(f(1, 2, 3, *(4, 5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 38')
    print(f(1, 2, 3, *[4, 5])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 41')
    print(f(*[1, 2, 3], 4, 5)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 44')
    print(f(1, 2, 3, *UserList([4, 5]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 47')
    print(f(1, 2, 3, *[4, 5], *[6, 7])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 50')
    print(f(1, *[2, 3], 4, *[5, 6], 7)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 53')
    print(f(*UserList([1, 2]), *UserList([3, 4]), 5, *UserList([6, 7]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 59')
    print(f(1, 2, 3, **{'a':4, 'b':5})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 62')
    print(f(1, 2, **{'a': -1, 'b': 5}, **{'a': 4, 'c': 6})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 67')
    print(f(1, 2, **{'a': -1, 'b': 5}, a=4, c=6)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 72')
    print(f(1, 2, a=3, **{'a': 4}, **{'a': 5})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 77')
    print(f(1, 2, 3, *[4, 5], **{'a':6, 'b':7})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 80')
    print(f(1, 2, 3, x=4, y=5, *(6, 7), **{'a':8, 'b': 9})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 83')
    print(f(1, 2, 3, *[4, 5], **{'c': 8}, **{'a':6, 'b':7})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 86')
    print(f(1, 2, 3, *(4, 5), x=6, y=7, **{'a':8, 'b': 9})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 90')
    print(f(1, 2, 3, **UserDict(a=4, b=5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 93')
    print(f(1, 2, 3, *(4, 5), **UserDict(a=6, b=7))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 96')
    print(f(1, 2, 3, x=4, y=5, *(6, 7), **UserDict(a=8, b=9))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 99')
    print(f(1, 2, 3, *(4, 5), x=6, y=7, **UserDict(a=8, b=9))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 108')
    print(e(c=4)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 114')
    print(g()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 120')
    print(g(*())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 126')
    print(g(*(), **{})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 132')
    print(g(1)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 135')
    print(g(1, 2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 138')
    print(g(1, 2, 3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 141')
    print(g(1, 2, 3, *(4, 5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class Nothing: pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 146')
    print(g(*Nothing())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class Nothing:
        def __len__(self): return 5
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 155')
    print(g(*Nothing())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class Nothing():
        def __len__(self): return 5
        def __getitem__(self, i):
            if i<3: return i
            else: raise IndexError(i)
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 167')
    print(g(*Nothing())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


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
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 181')
    print(g(*Nothing())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def broken(): raise TypeError("myerror")
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 190')
    print(g(*(broken() for i in range(1)))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 195')
    print(g(*range(1), *(broken() for i in range(1)))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class BrokenIterable1:
        def __iter__(self):
            raise TypeError('myerror')
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 204')
    print(g(*BrokenIterable1())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 209')
    print(g(*range(1), *BrokenIterable1())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class BrokenIterable2:
        def __iter__(self):
            yield 0
            raise TypeError('myerror')
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 219')
    print(g(*BrokenIterable2())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 224')
    print(g(*range(1), *BrokenIterable2())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class BrokenSequence:
        def __getitem__(self, idx):
            raise TypeError('myerror')
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 233')
    print(g(*BrokenSequence())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 238')
    print(g(*range(1), *BrokenSequence())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d = {'a': 1, 'b': 2, 'c': 3}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d2 = d.copy()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 248')
    print(g(1, d=4, **d)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 251')
    print(d == d2
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def saboteur(**kw):
        kw['x'] = 'm'
        return kw
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d = {}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    kw = saboteur(a=1, **d)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 263')
    print(d
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 268')
    print(g(1, 2, 3, **{'x': 4, 'y': 5})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 274')
    print(f(**{1:2})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 280')
    print(h(**{'e': 2})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    # Nuitka: Not following worse error message of Python3.9 here.
    import sys
    if sys.version_info < (3,9):
        print('Line 286')
        print(h(*h)
        )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    # Nuitka: Not following worse error message of Python3.9 here.
    import sys
    if sys.version_info < (3,9):
        print('Line 292')
        print(h(1, *h)
        )

except Exception as __e:
    print("Occurred", type(__e), __e)


# Nuitka: Ignore incompatible error that is complex to solve.
if False:
    try:
        print('Line 298')
        print(h(*[1], *h)
        )

    except Exception as __e:
        print("Occurred", type(__e), __e)


try:
    print('Line 304')
    print(dir(*h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    nothing = None
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 311')
    print(nothing(*h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 317')
    print(h(**h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 323')
    print(h(**[])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 329')
    print(h(a=1, **h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 335')
    print(h(a=1, **[])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 341')
    print(h(**{'a': 1}, **h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 347')
    print(h(**{'a': 1}, **[])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 353')
    print(dir(**h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 359')
    print(nothing(**h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 365')
    print(dir(b=1, **{'b': 1})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    from collections.abc import Mapping
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class MultiDict(Mapping):
        def __init__(self, items):
            self._items = items

        def __iter__(self):
            return (k for k, v in self._items)

        def __getitem__(self, key):
            for k, v in self._items:
                if k == key:
                    return v
            raise KeyError(key)

        def __len__(self):
            return len(self._items)

        def keys(self):
            return [k for k, v in self._items]

        def values(self):
            return [v for k, v in self._items]

        def items(self):
            return [(k, v) for k, v in self._items]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 398')
    print(g(**MultiDict([('x', 1), ('y', 2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 402')
    print(g(**MultiDict([('x', 1), ('x', 2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 408')
    print(g(a=3, **MultiDict([('x', 1), ('x', 2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 414')
    print(g(**MultiDict([('a', 3)]), **MultiDict([('x', 1), ('x', 2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f2(*a, **b):
        return a, b
    #
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d = {}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    for i in range(512):
        key = 'k%d' % i
        d[key] = i
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, b = f2(1, *(2,3), **d)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 431')
    print(len(a), len(b), b == d
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class Foo:
        def method(self, arg1, arg2):
            return arg1+arg2
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    x = Foo()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 440')
    print(Foo.method(*(x, 1, 2))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 443')
    print(Foo.method(x, *(1, 2))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 446')
    print(Foo.method(*(1, 2, 3))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 449')
    print(Foo.method(1, *[2, 3])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    try:
        silence = id(1, *{})
        True
    except:
        False
    # Expected:
    ## True
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 465')
    print(id(1, **{'foo': 1})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


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
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    x = {Name("a"):1, Name("b"):2}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b):
        print(a,b)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 487')
    print(f(**x)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 494')
    print(f(1)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 500')
    print(f(1, 2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b=1): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 506')
    print(f(1, 2, 3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(*, kw): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 512')
    print(f(1, kw=3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(*, kw, b): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 518')
    print(f(1, 2, 3, b=3, kw=3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b=2, *, kw): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 524')
    print(f(2, 3, 4, kw=4)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 533')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 539')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b, c): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 545')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b, c, d, e): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 551')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b=4, c=5, d=5): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 557')
    print(f(c=12, b=9)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(*, w): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 566')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(*, a, b, c, d, e): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 572')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)
