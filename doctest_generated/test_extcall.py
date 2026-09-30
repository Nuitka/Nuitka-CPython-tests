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
    from test import support
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
    print('Line 24')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 27')
    print(f(1)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 30')
    print(f(1, 2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 33')
    print(f(1, 2, 3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 36')
    print(f(1, 2, 3, *(4, 5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 39')
    print(f(1, 2, 3, *[4, 5])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 42')
    print(f(*[1, 2, 3], 4, 5)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 45')
    print(f(1, 2, 3, *UserList([4, 5]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 48')
    print(f(1, 2, 3, *[4, 5], *[6, 7])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 51')
    print(f(1, *[2, 3], 4, *[5, 6], 7)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 54')
    print(f(*UserList([1, 2]), *UserList([3, 4]), 5, *UserList([6, 7]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 60')
    print(f(1, 2, 3, **{'a':4, 'b':5})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 63')
    print(f(1, 2, **{'a': -1, 'b': 5}, **{'a': 4, 'c': 6})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 68')
    print(f(1, 2, **{'a': -1, 'b': 5}, a=4, c=6)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 73')
    print(f(1, 2, a=3, **{'a': 4}, **{'a': 5})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 78')
    print(f(1, 2, 3, *[4, 5], **{'a':6, 'b':7})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 81')
    print(f(1, 2, 3, x=4, y=5, *(6, 7), **{'a':8, 'b': 9})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 84')
    print(f(1, 2, 3, *[4, 5], **{'c': 8}, **{'a':6, 'b':7})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 87')
    print(f(1, 2, 3, *(4, 5), x=6, y=7, **{'a':8, 'b': 9})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 91')
    print(f(1, 2, 3, **UserDict(a=4, b=5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 94')
    print(f(1, 2, 3, *(4, 5), **UserDict(a=6, b=7))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 97')
    print(f(1, 2, 3, x=4, y=5, *(6, 7), **UserDict(a=8, b=9))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 100')
    print(f(1, 2, 3, *(4, 5), x=6, y=7, **UserDict(a=8, b=9))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d1 = {'a':1}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d2 = {'c':3}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 110')
    print(f(b=2, **d1, **d2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 114')
    print(f(**d1, b=2, **d2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 118')
    print(f(**d1, **d2, b=2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 122')
    print(f(**d1, b=2, **d2, d=4)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 131')
    print(e(c=4)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 137')
    print(g()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 143')
    print(g(*())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 149')
    print(g(*(), **{})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 155')
    print(g(1)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 158')
    print(g(1, 2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 161')
    print(g(1, 2, 3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 164')
    print(g(1, 2, 3, *(4, 5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class Nothing: pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 169')
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
    print('Line 178')
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
    print('Line 190')
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
    print('Line 204')
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
    print('Line 213')
    print(g(*(broken() for i in range(1)))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 218')
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
    print('Line 227')
    print(g(*BrokenIterable1())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 232')
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
    print('Line 242')
    print(g(*BrokenIterable2())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 247')
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
    print('Line 256')
    print(g(*BrokenSequence())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 261')
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
    print('Line 271')
    print(g(1, d=4, **d)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 274')
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
    print('Line 286')
    print(d
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 291')
    print(g(1, 2, 3, **{'x': 4, 'y': 5})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 297')
    print(f(**{1:2})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 303')
    print(h(**{'e': 2})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 309')
    print(h(*h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 321')
    print(h(*[1], *h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 327')
    print(dir(*h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    nothing = None
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 334')
    print(nothing(*h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 340')
    print(h(**h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 346')
    print(h(**[])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 352')
    print(h(a=1, **h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 358')
    print(h(a=1, **[])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 364')
    print(h(**{'a': 1}, **h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 370')
    print(h(**{'a': 1}, **[])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 376')
    print(dir(**h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 382')
    print(nothing(**h)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 388')
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
    print('Line 421')
    print(g(**MultiDict([('x', 1), ('y', 2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 425')
    print(g(**MultiDict([('x', 1), ('x', 2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 431')
    print(g(a=3, **MultiDict([('x', 1), ('x', 2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 437')
    print(g(**MultiDict([('a', 3)]), **MultiDict([('x', 1), ('x', 2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class MyDict(dict):
        pass
    #
    def s1(**kwargs):
        return kwargs
    def s2(*args, **kwargs):
        return (args, kwargs)
    def s3(*, n, **kwargs):
        return (n, kwargs)
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    md = MyDict({'a': 1, 'b': 2})
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    assert s1(**md) == {'a': 1, 'b': 2}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    assert s2(*(1, 2), **md) == ((1, 2), {'a': 1, 'b': 2})
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    assert s3(**MyDict({'n': 1, 'b': 2})) == (1, {'b': 2})
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 459')
    print(s3(**md)
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
    print('Line 476')
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
    print('Line 485')
    print(Foo.method(*(x, 1, 2))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 488')
    print(Foo.method(x, *(1, 2))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 491')
    print(Foo.method(*(1, 2, 3))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 494')
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
    print('Line 510')
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
    print('Line 532')
    print(f(**x)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 539')
    print(f(1)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 545')
    print(f(1, 2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b=1): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 551')
    print(f(1, 2, 3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(*, kw): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 557')
    print(f(1, kw=3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(*, kw, b): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 563')
    print(f(1, 2, 3, b=3, kw=3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b=2, *, kw): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 569')
    print(f(2, 3, 4, kw=4)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 578')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 584')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b, c): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 590')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b, c, d, e): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 596')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(a, b=4, c=5, d=5): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 602')
    print(f(c=12, b=9)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(*, w): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 611')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(*, a, b, c, d, e): pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 617')
    print(f()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)
