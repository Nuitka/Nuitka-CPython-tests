
try:
    print('Line 4')
    print(sum(i*i for i in range(100) if i&1 == 1))

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 10')
    print([(i,j) for i in range(3) for j in range(4)]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 16')
    print([(i,j) for i in range(4) for j in range(i)]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    i = 20
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 23')
    print(sum(i**2 for i in range(100)))

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 27')
    print(i
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def frange(n):
        return list(range(n))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 52')
    print(frange(10)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    lrange = lambda n:  [i for i in range(n)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 59')
    print(lrange(10)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def grange(n):
        yield from list(range(n))
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 68')
    print(list(grange(5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 75')
    print([None for i in range(10)]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = [(lambda i=i: i) for i in range(5)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 84')
    print([x() for x in items]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = [(lambda: i) for i in range(5)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 91')
    print([x() for x in items]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = [(lambda: i) for i in range(5)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    i = 20
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 99')
    print([x() for x in items]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = [(lambda: y) for i in range(5)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    y = 2
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 107')
    print([x() for x in items]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = [(lambda i=i: i) for i in range(5)]
        return [x() for x in items]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 116')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = [(lambda: i) for i in range(5)]
        return [x() for x in items]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 123')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = [(lambda: i) for i in range(5)]
        i = 20
        return [x() for x in items]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 131')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = [lambda: y for _ in range(5)]
        y = 2
        return [x() for x in items]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 139')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)
