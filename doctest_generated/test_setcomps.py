
try:
    sum({i*i for i in range(100) if i&1 == 1})
except Exception as e:
    print( "Occured", type(e), e )


try:
    {2*y + x + 1 for x in (0,) for y in (1,)}
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(sorted({(i,j) for i in range(3) for j in range(4)}))
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(sorted({(i,j) for i in range(4) for j in range(i)}))
except Exception as e:
    print( "Occured", type(e), e )


try:
    i = 20
except Exception as e:
    print( "Occured", type(e), e )


try:
    sum({i*i for i in range(100)})
except Exception as e:
    print( "Occured", type(e), e )


try:
    i
except Exception as e:
    print( "Occured", type(e), e )


try:
    def srange(n):
        return {i for i in range(n)}
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(sorted(srange(10)))
except Exception as e:
    print( "Occured", type(e), e )


try:
    lrange = lambda n:  {i for i in range(n)}
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(sorted(lrange(10)))
except Exception as e:
    print( "Occured", type(e), e )


try:
    def grange(n):
        for x in {i for i in range(n)}:
            yield x
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(sorted(grange(5)))
except Exception as e:
    print( "Occured", type(e), e )


try:
    {None for i in range(10)}
except Exception as e:
    print( "Occured", type(e), e )


try:
    items = {(lambda i=i: i) for i in range(5)}
except Exception as e:
    print( "Occured", type(e), e )


try:
    {x() for x in items} == set(range(5))
except Exception as e:
    print( "Occured", type(e), e )


try:
    items = {(lambda: i) for i in range(5)}
except Exception as e:
    print( "Occured", type(e), e )


try:
    {x() for x in items}
except Exception as e:
    print( "Occured", type(e), e )


try:
    items = {(lambda: i) for i in range(5)}
except Exception as e:
    print( "Occured", type(e), e )


try:
    i = 20
except Exception as e:
    print( "Occured", type(e), e )


try:
    {x() for x in items}
except Exception as e:
    print( "Occured", type(e), e )


try:
    items = {(lambda: y) for i in range(5)}
except Exception as e:
    print( "Occured", type(e), e )


try:
    y = 2
except Exception as e:
    print( "Occured", type(e), e )


try:
    {x() for x in items}
except Exception as e:
    print( "Occured", type(e), e )


try:
    def test_func():
        items = {(lambda i=i: i) for i in range(5)}
        return {x() for x in items}
except Exception as e:
    print( "Occured", type(e), e )


try:
    test_func() == set(range(5))
except Exception as e:
    print( "Occured", type(e), e )


try:
    def test_func():
        items = {(lambda: i) for i in range(5)}
        return {x() for x in items}
except Exception as e:
    print( "Occured", type(e), e )


try:
    test_func()
except Exception as e:
    print( "Occured", type(e), e )


try:
    def test_func():
        items = {(lambda: i) for i in range(5)}
        i = 20
        return {x() for x in items}
except Exception as e:
    print( "Occured", type(e), e )


try:
    test_func()
except Exception as e:
    print( "Occured", type(e), e )


try:
    def test_func():
        items = {(lambda: y) for i in range(5)}
        y = 2
        return {x() for x in items}
except Exception as e:
    print( "Occured", type(e), e )


try:
    test_func()
except Exception as e:
    print( "Occured", type(e), e )
