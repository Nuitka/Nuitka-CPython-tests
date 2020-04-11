
try:
    t = (1, 2, 3)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b, c = t
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 4')
    print(a == 1 and b == [2] and c == 3
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    l = [4, 5, 6]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b = l
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 12')
    print(a == 4 and b == [5, 6]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    *a, = 7, 8, 9
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 19')
    print(a == [7, 8, 9]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b = 'one'
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 26')
    print(a == 'o' and b == ['n', 'e']
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, b, c, *d, e, f, g = range(10)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 33')
    print((a, b, c, d, e, f, g) == (0, 1, 2, [3, 4, 5, 6], 7, 8, 9)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b, c = (1, 2)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 40')
    print(a == 1 and c == 2 and b == []
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class Seq:
        def __getitem__(self, i):
            if i >= 0 and i < 3: return i
            raise IndexError
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b = Seq()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 51')
    print(a == 0 and b == [1, 2]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    for a, *b, c in [(1,2,3), (4,5,6,7)]:
        print(a, b, c)
    # Expected:
    ## 1 [2] 3
    ## 4 [5, 6] 7
    #
    # Unpack in list
    #
    [a, *b, c] = range(5)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 66')
    print(a == 0 and b == [1, 2, 3] and c == 4
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b, c = *d, e = range(5)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 73')
    print(a == 0 and b == [1, 2, 3] and c == 4 and d == [0, 1, 2, 3] and e == 4
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, b, *c = range(5)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 80')
    print(a, b, c
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    *a, b, c = a, b, *c
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 84')
    print(a, b, c
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a = [1, 2, 3]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 91')
    print(sorted({1, *a, 0, 4})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 95')
    print({1, *1, 0, 4}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    kwds = {'z': 0, 'w': 12}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 104')
    print(sorted({'x': 1, 'y': 2, **kwds}.items())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 108')
    print(sorted({**{'x': 1}, 'y': 2, **{'z': 3}}.items())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 112')
    print(sorted({**{'x': 1}, 'y': 2, **{'x': 3}}.items())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 116')
    print(sorted({**{'x': 1}, **{'x': 3}, 'x': 4}.items())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 120')
    print({**{}}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a = {}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    {**a}[0] = 1
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 126')
    print(a
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 130')
    print({**1}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 136')
    print({**[]}
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    len(eval("{" + ", ".join("**{{{}: {}}}".format(i, i)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
                             for i in range(1000)) + "}"))
    # Expected:
    ## 1000
    #
    {0:1, **{0:2}, 0:3, 0:4}
    # Expected:
    ## {0: 4}
    #
    # List comprehension element unpacking
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, b, c = [0, 1, 2], 3, 4
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 154')
    print([*a, b, c]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    l = [a, (3, 4), {5}, {6: None}, (i for i in range(7, 10))]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 203')
    print(print(*[1], *[2], 3)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(x, y):
        print(x, y)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    original_dict = {'x': 1}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 212')
    print(f(**original_dict, y=2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 215')
    print(original_dict
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    from collections.abc import MutableMapping
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class CrazyDict(MutableMapping):
        def __init__(self):
            self.d = {}

        def __iter__(self):
            for x in self.d.__iter__():
                if x == 'c':
                    self.d['z'] = 10
                yield x

        def __getitem__(self, k):
            return self.d[k]

        def __len__(self):
            return len(self.d)

        def __setitem__(self, k, v):
            self.d[k] = v

        def __delitem__(self, k):
            del self.d[k]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d = CrazyDict()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d.d = {chr(ord('a') + x): x for x in range(5)}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    e = {**d}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    d.d = {chr(ord('a') + x): x for x in range(5)}
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def f(**kwargs): print(kwargs)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 255')
    print(f(**d)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 263')
    print(f(x=5, **{'x': 3}, y=2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 269')
    print(f(**{'x': 3}, x=5, y=2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 275')
    print(f(**{'x': 3}, **{'x': 5}, y=2)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 281')
    print(f(x=5, **{'x': 3}, **{'x': 2})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 287')
    print(f(**{1: 3}, **{1: 5})
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b = 7
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b, c, d, e = Seq()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, b, c, d, *e = Seq()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class BozoError(Exception):
        pass
    class BadSeq:
        def __getitem__(self, i):
            if i >= 0 and i < 3:
                return i
            elif i == 3:
                raise BozoError
            else:
                raise IndexError
    #
    # Trigger code while not expecting an IndexError (unpack sequence too long, wrong
    # error)
    #
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a, *b, c, d, e = BadSeq()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    s = ", ".join("a%d" % i for i in range(1<<8)) + ", *rest = range(1<<8 + 1)"
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    s = ", ".join("a%d" % i for i in range(1<<8 + 1)) + ", *rest = range(1<<8 + 2)"
except Exception as __e:
    print("Occurred", type(__e), __e)
