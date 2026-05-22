
try:
    print('Line 4')
    print(sum({i*i for i in range(100) if i&1 == 1})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 10')
    print({2*y + x + 1 for x in (0,) for y in (1,)}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 16')
    print(list(sorted({(i,j) for i in range(3) for j in range(4)}))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 22')
    print(list(sorted({(i,j) for i in range(4) for j in range(i)}))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 28')
    print(sorted({j*j for i in range(4) for j in [i+1]})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 31')
    print(sorted({j*k for i in range(4) for j in [i+1] for k in [j+1]})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 34')
    print(sorted({j*k for i in range(4) for j, k in [(i+1, i+2)]})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 40')
    print(sorted({i*i for i in [*range(4)]})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 43')
    print(sorted({i*i for i in (*range(4),)})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    i = 20
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 50')
    print(sum({i*i for i in range(100)})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 54')
    print(i
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def srange(n):
        return {i for i in range(n)}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 77')
    print(list(sorted(srange(10)))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    lrange = lambda n:  {i for i in range(n)}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 84')
    print(list(sorted(lrange(10)))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def grange(n):
        for x in {i for i in range(n)}:
            yield x
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 93')
    print(list(sorted(grange(5)))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 100')
    print({None for i in range(10)}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = {(lambda i=i: i) for i in range(5)}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 109')
    print({x() for x in items} == set(range(5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = {(lambda: i) for i in range(5)}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 116')
    print({x() for x in items}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = {(lambda: i) for i in range(5)}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    i = 20
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 124')
    print({x() for x in items}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = {(lambda: y) for i in range(5)}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    y = 2
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 132')
    print({x() for x in items}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = {(lambda i=i: i) for i in range(5)}
        return {x() for x in items}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 141')
    print(test_func() == set(range(5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = {(lambda: i) for i in range(5)}
        return {x() for x in items}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 148')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = {(lambda: i) for i in range(5)}
        i = 20
        return {x() for x in items}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 156')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = {(lambda: y) for i in range(5)}
        y = 2
        return {x() for x in items}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 164')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)
