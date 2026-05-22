
try:
    print('Line 4')
    print(sum([i*i for i in range(100) if i&1 == 1])
    )

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
    print('Line 22')
    print([j*j for i in range(4) for j in [i+1]]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 25')
    print([j*k for i in range(4) for j in [i+1] for k in [j+1]]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 28')
    print([j*k for i in range(4) for j, k in [(i+1, i+2)]]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 34')
    print([i*i for i in [*range(4)]]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 37')
    print([i*i for i in (*range(4),)]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    i = 20
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 44')
    print(sum([i*i for i in range(100)])
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 48')
    print(i
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def frange(n):
        return [i for i in range(n)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 73')
    print(frange(10)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    lrange = lambda n:  [i for i in range(n)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 80')
    print(lrange(10)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def grange(n):
        for x in [i for i in range(n)]:
            yield x
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 89')
    print(list(grange(5))
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 96')
    print([None for i in range(10)]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = [(lambda i=i: i) for i in range(5)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 105')
    print([x() for x in items]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    items = [(lambda: i) for i in range(5)]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 112')
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
    print('Line 120')
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
    print('Line 128')
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
    print('Line 137')
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
    print('Line 144')
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
    print('Line 152')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def test_func():
        items = [(lambda: y) for i in range(5)]
        y = 2
        return [x() for x in items]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 160')
    print(test_func()
    )

except Exception as __e:
    print("Occurred", type(__e), __e)
