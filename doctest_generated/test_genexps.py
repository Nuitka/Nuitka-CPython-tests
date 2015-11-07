
try:
    print('Line 2')
    print(sum(i*i for i in range(100) if i&1 == 1)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 8')
    print(list((i,j) for i in range(3) for j in range(4) )
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 14')
    print(list((i,j) for i in range(4) for j in range(i) )
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    i = 20
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 21')
    print(sum(i*i for i in range(100))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 24')
    print(i
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (i*i for i in range(4))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 31')
    print(type(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 34')
    print(list(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (i*i for i in range(3))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 41')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 44')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 47')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 50')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 59')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 65')
    print(list(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(n):
        return (i*i for i in range(n))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 73')
    print(list(f(10))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(n):
        return ((i,j) for i in range(3) for j in range(n))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 79')
    print(list(f(4))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(n):
        return ((i,j) for i in range(3) for j in range(4) if j in range(n))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 84')
    print(list(f(4))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 87')
    print(list(f(2))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 110')
    print(dict(a = (i for i in range(10))) #doctest: +ELLIPSIS
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    x=10
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (i*i for i in range(x))
except Exception as e:
    print("Occurred", type(e), e)


try:
    x = 5
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 119')
    print(list(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 126')
    print((i for i in 6)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    include = (2,4,6,8)
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (i*i for i in range(10) if i in include)
except Exception as e:
    print("Occurred", type(e), e)


try:
    include = (1,3,5,7,9)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 138')
    print(list(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    g = ((i,j) for i in range(3) for j in range(x))
except Exception as e:
    print("Occurred", type(e), e)


try:
    x = 4
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 146')
    print(list(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    tupleids = list(map(id, ((i,i) for i in range(10))))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 153')
    print(int(max(tupleids) - min(tupleids))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    yrange = lambda n:  (i for i in range(n))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 177')
    print(list(yrange(10))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def creator():
        r = yrange(5)
        print("creator", next(r))
        return r
    def caller():
        r = creator()
        for i in r:
                print("caller", i)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 191')
    print(caller()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def zrange(n):
        for i in yrange(n):
            yield i
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 204')
    print(list(zrange(5))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (next(me) for i in range(10))
except Exception as e:
    print("Occurred", type(e), e)


try:
    me = g
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 213')
    print(next(me)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (10 // i for i in (5, 0, 2))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 225')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 228')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 236')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 245')
    print(list(None for i in range(10))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (i*i for i in range(3))
except Exception as e:
    print("Occurred", type(e), e)


try:
    expected = set(['gi_frame', 'gi_running'])
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 257')
    print(print(g.__next__.__doc__)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    import types
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 267')
    print(iter(g) is g
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (me.gi_running for i in (0,1))
except Exception as e:
    print("Occurred", type(e), e)


try:
    me = g
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 275')
    print(me.gi_running
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 278')
    print(next(me)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 281')
    print(me.gi_running
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    import weakref
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = (i*i for i in range(4))
except Exception as e:
    print("Occurred", type(e), e)


try:
    wr = weakref.ref(g)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 290')
    print(wr() is g
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    p = weakref.proxy(g)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 294')
    print(list(p)
    )

except Exception as e:
    print("Occurred", type(e), e)
