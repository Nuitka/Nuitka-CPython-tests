
try:
    print('Line 2')
    print(sum(i*i for i in range(100) if i&1 == 1)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 8')
    print(list((i,j) for i in range(3) for j in range(4) )
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 14')
    print(list((i,j) for i in range(4) for j in range(i) )
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 20')
    print(list((j*j for i in range(4) for j in [i+1]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 23')
    print(list((j*k for i in range(4) for j in [i+1] for k in [j+1]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 26')
    print(list((j*k for i in range(4) for j, k in [(i+1, i+2)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 32')
    print(list((i*i for i in [*range(4)]))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 35')
    print(list((i*i for i in (*range(4),)))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    i = 20
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 42')
    print(sum(i*i for i in range(100))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 45')
    print(i
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (i*i for i in range(4))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 52')
    print(type(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 55')
    print(list(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (i*i for i in range(3))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 62')
    print(next(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 65')
    print(next(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 68')
    print(next(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 71')
    print(next(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 80')
    print(next(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 86')
    print(list(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(n):
        return (i*i for i in range(n))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 94')
    print(list(f(10))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(n):
        return ((i,j) for i in range(3) for j in range(n))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 100')
    print(list(f(4))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(n):
        return ((i,j) for i in range(3) for j in range(4) if j in range(n))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 105')
    print(list(f(4))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 108')
    print(list(f(2))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 131')
    print(dict(a = (i for i in range(10))) #doctest: +ELLIPSIS
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    x=10
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (i*i for i in range(x))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    x = 5
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 140')
    print(list(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 147')
    print((i for i in 6)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    include = (2,4,6,8)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (i*i for i in range(10) if i in include)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    include = (1,3,5,7,9)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 159')
    print(list(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = ((i,j) for i in range(3) for j in range(x))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    x = 4
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 167')
    print(list(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    tupleids = list(map(id, ((i,i) for i in range(10))))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 174')
    print(int(max(tupleids) - min(tupleids))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    yrange = lambda n:  (i for i in range(n))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 198')
    print(list(yrange(10))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def creator():
        r = yrange(5)
        print("creator", next(r))
        return r
    def caller():
        r = creator()
        for i in r:
                print("caller", i)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 212')
    print(caller()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def zrange(n):
        for i in yrange(n):
            yield i
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 225')
    print(list(zrange(5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (next(me) for i in range(10))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    me = g
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 234')
    print(next(me)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (10 // i for i in (5, 0, 2))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 246')
    print(next(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 249')
    print(next(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 257')
    print(next(g)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 266')
    print(list(None for i in range(10))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (i*i for i in range(3))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    expected = set(['gi_frame', 'gi_running'])
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    from test.support import HAVE_DOCSTRINGS
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 279')
    print(print(g.__next__.__doc__ if HAVE_DOCSTRINGS else 'Implement next(self).')
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    import types
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 289')
    print(iter(g) is g
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (me.gi_running for i in (0,1))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    me = g
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 297')
    print(me.gi_running
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 300')
    print(next(me)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 303')
    print(me.gi_running
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    import weakref
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    g = (i*i for i in range(4))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    wr = weakref.ref(g)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 312')
    print(wr() is g
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    p = weakref.proxy(g)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 316')
    print(list(p)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)
