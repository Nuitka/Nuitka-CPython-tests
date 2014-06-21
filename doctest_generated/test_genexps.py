
try:
    sum(i*i for i in range(100) if i&1 == 1)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list((i,j) for i in range(3) for j in range(4) )
except Exception as e:
    print( "Occured", type(e), e )


try:
    list((i,j) for i in range(4) for j in range(i) )
except Exception as e:
    print( "Occured", type(e), e )


try:
    i = 20
except Exception as e:
    print( "Occured", type(e), e )


try:
    sum(i*i for i in range(100))
except Exception as e:
    print( "Occured", type(e), e )


try:
    i
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (i*i for i in range(4))
except Exception as e:
    print( "Occured", type(e), e )


try:
    type(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (i*i for i in range(3))
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    def f(n):
        return (i*i for i in range(n))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(f(10))
except Exception as e:
    print( "Occured", type(e), e )


try:
    def f(n):
        return ((i,j) for i in range(3) for j in range(n))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(f(4))
except Exception as e:
    print( "Occured", type(e), e )


try:
    def f(n):
        return ((i,j) for i in range(3) for j in range(4) if j in range(n))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(f(4))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(f(2))
except Exception as e:
    print( "Occured", type(e), e )


try:
    dict(a = (i for i in range(10))) #doctest: +ELLIPSIS
except Exception as e:
    print( "Occured", type(e), e )


try:
    x=10
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (i*i for i in range(x))
except Exception as e:
    print( "Occured", type(e), e )


try:
    x = 5
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    (i for i in 6)
except Exception as e:
    print( "Occured", type(e), e )


try:
    include = (2,4,6,8)
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (i*i for i in range(10) if i in include)
except Exception as e:
    print( "Occured", type(e), e )


try:
    include = (1,3,5,7,9)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = ((i,j) for i in range(3) for j in range(x))
except Exception as e:
    print( "Occured", type(e), e )


try:
    x = 4
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    tupleids = list(map(id, ((i,i) for i in range(10))))
except Exception as e:
    print( "Occured", type(e), e )


try:
    int(max(tupleids) - min(tupleids))
except Exception as e:
    print( "Occured", type(e), e )


try:
    yrange = lambda n:  (i for i in range(n))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(yrange(10))
except Exception as e:
    print( "Occured", type(e), e )


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
    print( "Occured", type(e), e )


try:
    caller()
except Exception as e:
    print( "Occured", type(e), e )


try:
    def zrange(n):
        for i in yrange(n):
            yield i
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(zrange(5))
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (next(me) for i in range(10))
except Exception as e:
    print( "Occured", type(e), e )


try:
    me = g
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(me)
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (10 // i for i in (5, 0, 2))
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(None for i in range(10))
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (i*i for i in range(3))
except Exception as e:
    print( "Occured", type(e), e )


try:
    expected = set(['gi_frame', 'gi_running'])
except Exception as e:
    print( "Occured", type(e), e )


try:
    from test.support import HAVE_DOCSTRINGS
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(g.__next__.__doc__ if HAVE_DOCSTRINGS else 'Implement next(self).')
except Exception as e:
    print( "Occured", type(e), e )


try:
    import types
except Exception as e:
    print( "Occured", type(e), e )


try:
    iter(g) is g
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (me.gi_running for i in (0,1))
except Exception as e:
    print( "Occured", type(e), e )


try:
    me = g
except Exception as e:
    print( "Occured", type(e), e )


try:
    me.gi_running
except Exception as e:
    print( "Occured", type(e), e )


try:
    next(me)
except Exception as e:
    print( "Occured", type(e), e )


try:
    me.gi_running
except Exception as e:
    print( "Occured", type(e), e )


try:
    import weakref
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = (i*i for i in range(4))
except Exception as e:
    print( "Occured", type(e), e )


try:
    wr = weakref.ref(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    wr() is g
except Exception as e:
    print( "Occured", type(e), e )


try:
    p = weakref.proxy(g)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(p)
except Exception as e:
    print( "Occured", type(e), e )
