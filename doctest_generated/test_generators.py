from test.test_generators import Knights
################################################################################

try:
    def f():
        yield 1
        return
    #
    def f():
        try:
            yield 1
        finally:
            pass
    #
    def f():
        try:
            try:
                1//0
            except ZeroDivisionError:
                yield 666
            except:
                pass
        finally:
            pass
    #
    def f():
        try:
            try:
                yield 12
                1//0
            except ZeroDivisionError:
                yield 666
            except:
                try:
                    x = 12
                finally:
                    yield 12
        except:
            return
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 63')
    print(list(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
       yield
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 69')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
       if 0:
           yield
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 77')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        if 0:
            yield 1
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 85')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
       if "":
           yield None
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 92')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        return
        try:
            if x==4:
                pass
            elif 0:
                try:
                    1//0
                except SyntaxError:
                    pass
                else:
                    if 0:
                        while 12:
                            x += 1
                            yield 2 # don't blink
                            f(a, b, c, d, e)
            else:
                pass
        except:
            x = 1
        return
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 117')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        if 0:
            def g():
                yield 1
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 125')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        if 0:
            class C:
                def __init__(self):
                    yield 1
                def f(self):
                    yield 2
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 136')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        if 0:
            return
        if 0:
            yield 2
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 145')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        for i in range(3):
            try:
                continue
            finally:
                yield i
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 173')
    print(print(next(g))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 176')
    print(print(next(g))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 179')
    print(print(next(g))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 182')
    print(print(next(g))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        yield 5
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 196')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 199')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
       yield 5
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 213')
    print(g.__name__
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 216')
    print(repr(g)  # doctest: +ELLIPSIS
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    x = lambda: (yield 1)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 223')
    print(list(x())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    x = lambda: ((yield 1), (yield 2))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 228')
    print(list(x())
    )

except Exception as e:
    print("Occurred", type(e), e)

################################################################################

try:
    def firstn(g, n):
        return [next(g) for i in range(n)]
    #
    def intsfrom(i):
        while 1:
            yield i
            i += 1
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 10')
    print(firstn(intsfrom(5), 7)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def exclude_multiples(n, ints):
        for i in ints:
            if i % n:
                yield i
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 19')
    print(firstn(exclude_multiples(3, intsfrom(1)), 6)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def sieve(ints):
        prime = next(ints)
        yield prime
        not_divisible_by_prime = exclude_multiples(prime, ints)
        for p in sieve(not_divisible_by_prime):
            yield p
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    primes = sieve(intsfrom(2))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 31')
    print(firstn(primes, 20)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def times(n, g):
        for i in g:
            yield n * i
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 45')
    print(firstn(times(10, intsfrom(1)), 10)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def merge(g, h):
        ng = next(g)
        nh = next(h)
        while 1:
            if ng < nh:
                yield ng
                ng = next(g)
            elif ng > nh:
                yield nh
                nh = next(h)
            else:
                yield ng
                ng = next(g)
                nh = next(h)
    #
    # The following works, but is doing a whale of a lot of redundant work --
    # it's not clear how to get the internal uses of m235 to share a single
    # generator.  Note that me_times2 (etc) each need to see every element in the
    # result sequence.  So this is an example where lazy lists are more natural
    # (you can look at the head of a lazy list any number of times).
    #
    def m235():
        yield 1
        me_times2 = times(2, m235())
        me_times3 = times(3, m235())
        me_times5 = times(5, m235())
        for i in merge(merge(me_times2,
                             me_times3),
                       me_times5):
            yield i
    #
    # Don't print "too many" of these -- the implementation above is extremely
    # inefficient:  each call of m235() leads to 3 recursive calls, and in
    # turn each of those 3 more, and so on, and so on, until we've descended
    # enough levels to satisfy the print stmts.  Very odd:  when I printed 5
    # lines of results below, this managed to screw up Win98's malloc in "the
    # usual" way, i.e. the heap grew over 4Mb so Win98 started fragmenting
    # address space, and it *looked* like a very slow leak.
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    result = m235()
except Exception as e:
    print("Occurred", type(e), e)


try:
    for i in range(3):
        print(firstn(result, 15))
    # Expected:
    ## [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
    ## [25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80]
    ## [81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192]
    #
    # Heh.  Here's one way to get a shared list, complete with an excruciating
    # namespace renaming trick.  The *pretty* part is that the times() and merge()
    # functions can be reused as-is, because they only assume their stream
    # arguments are iterable -- a LazyList is the same as a generator to times().
    #
    class LazyList:
        def __init__(self, g):
            self.sofar = []
            self.fetch = g.__next__

        def __getitem__(self, i):
            sofar, fetch = self.sofar, self.fetch
            while i >= len(sofar):
                sofar.append(fetch())
            return sofar[i]
    #
    def m235():
        yield 1
        # Gack:  m235 below actually refers to a LazyList.
        me_times2 = times(2, m235)
        me_times3 = times(3, m235)
        me_times5 = times(5, m235)
        for i in merge(merge(me_times2,
                             me_times3),
                       me_times5):
            yield i
    #
    # Print as many of these as you like -- *this* implementation is memory-
    # efficient.
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    m235 = LazyList(m235())
except Exception as e:
    print("Occurred", type(e), e)


try:
    for i in range(5):
        print([m235[j] for j in range(15*i, 15*(i+1))])
    # Expected:
    ## [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
    ## [25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80]
    ## [81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192]
    ## [200, 216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384]
    ## [400, 405, 432, 450, 480, 486, 500, 512, 540, 576, 600, 625, 640, 648, 675]
    #
    # Ye olde Fibonacci generator, LazyList style.
    #
    def fibgen(a, b):

        def sum(g, h):
            while 1:
                yield next(g) + next(h)

        def tail(g):
            next(g)    # throw first away
            for x in g:
                yield x

        yield a
        yield b
        for s in sum(iter(fib),
                     tail(iter(fib))):
            yield s
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    fib = LazyList(fibgen(1, 2))
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 156')
    print(firstn(iter(fib), 17)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    from itertools import tee
except Exception as e:
    print("Occurred", type(e), e)


try:
    def m235():
        def _m235():
            yield 1
            for n in merge(times(2, m2),
                           merge(times(3, m3),
                                 times(5, m5))):
                yield n
        m1 = _m235()
        m2, m3, m5, mRes = tee(m1, 4)
        return mRes
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    it = m235()
except Exception as e:
    print("Occurred", type(e), e)


try:
    for i in range(5):
        print(firstn(it, 15))
    # Expected:
    ## [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
    ## [25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80]
    ## [81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192]
    ## [200, 216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384]
    ## [400, 405, 432, 450, 480, 486, 500, 512, 540, 576, 600, 625, 640, 648, 675]
    #
    # The "tee" function does just what we want. It internally keeps a generated
    # result for as long as it has not been "consumed" from all of the duplicated
    # iterators, whereupon it is deleted. You can therefore print the hamming
    # sequence during hours without increasing memory usage, or very little.
    #
    # The beauty of it is that recursive running-after-their-tail FP algorithms
    # are quite straightforwardly expressed with this Python idiom.
    #
    # Ye olde Fibonacci generator, tee style.
    #
    def fib():

        def _isum(g, h):
            while 1:
                yield next(g) + next(h)

        def _fib():
            yield 1
            yield 2
            next(fibTail) # throw first away
            for res in _isum(fibHead, fibTail):
                yield res

        realfib = _fib()
        fibHead, fibTail, fibRes = tee(realfib, 3)
        return fibRes
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 236')
    print(firstn(fib(), 17)
    )

except Exception as e:
    print("Occurred", type(e), e)

################################################################################

try:
    for c in conjoin([lambda: iter((0, 1))] * 3):
        print(c)
    # Expected:
    ## [0, 0, 0]
    ## [0, 0, 1]
    ## [0, 1, 0]
    ## [0, 1, 1]
    ## [1, 0, 0]
    ## [1, 0, 1]
    ## [1, 1, 0]
    ## [1, 1, 1]
    #
    # For efficiency in typical backtracking apps, conjoin() yields the same list
    # object each time.  So if you want to save away a full account of its
    # generated sequence, you need to copy its results.
    #
    def gencopy(iterator):
        for x in iterator:
            yield x[:]
    #
    for n in range(10):
        all = list(gencopy(conjoin([lambda: iter((0, 1))] * n)))
        print(n, len(all), all[0] == [0] * n, all[-1] == [1] * n)
    # Expected:
    ## 0 1 True True
    ## 1 2 True True
    ## 2 4 True True
    ## 3 8 True True
    ## 4 16 True True
    ## 5 32 True True
    ## 6 64 True True
    ## 7 128 True True
    ## 8 256 True True
    ## 9 512 True True
    #
    # And run an 8-queens solver.
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    q = Queens(8)
except Exception as e:
    print("Occurred", type(e), e)


try:
    LIMIT = 2
except Exception as e:
    print("Occurred", type(e), e)


try:
    count = 0
except Exception as e:
    print("Occurred", type(e), e)


try:
    for row2col in q.solve():
        count += 1
        if count <= LIMIT:
            print("Solution", count)
            q.printsolution(row2col)
    # Expected:
    ## Solution 1
    ## +-+-+-+-+-+-+-+-+
    ## |Q| | | | | | | |
    ## +-+-+-+-+-+-+-+-+
    ## | | | | |Q| | | |
    ## +-+-+-+-+-+-+-+-+
    ## | | | | | | | |Q|
    ## +-+-+-+-+-+-+-+-+
    ## | | | | | |Q| | |
    ## +-+-+-+-+-+-+-+-+
    ## | | |Q| | | | | |
    ## +-+-+-+-+-+-+-+-+
    ## | | | | | | |Q| |
    ## +-+-+-+-+-+-+-+-+
    ## | |Q| | | | | | |
    ## +-+-+-+-+-+-+-+-+
    ## | | | |Q| | | | |
    ## +-+-+-+-+-+-+-+-+
    ## Solution 2
    ## +-+-+-+-+-+-+-+-+
    ## |Q| | | | | | | |
    ## +-+-+-+-+-+-+-+-+
    ## | | | | | |Q| | |
    ## +-+-+-+-+-+-+-+-+
    ## | | | | | | | |Q|
    ## +-+-+-+-+-+-+-+-+
    ## | | |Q| | | | | |
    ## +-+-+-+-+-+-+-+-+
    ## | | | | | | |Q| |
    ## +-+-+-+-+-+-+-+-+
    ## | | | |Q| | | | |
    ## +-+-+-+-+-+-+-+-+
    ## | |Q| | | | | | |
    ## +-+-+-+-+-+-+-+-+
    ## | | | | |Q| | | |
    ## +-+-+-+-+-+-+-+-+
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 86')
    print(print(count, "solutions in all.")
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    k = Knights(10, 10)
except Exception as e:
    print("Occurred", type(e), e)


try:
    LIMIT = 2
except Exception as e:
    print("Occurred", type(e), e)


try:
    count = 0
except Exception as e:
    print("Occurred", type(e), e)

################################################################################

try:
    def g():
        i = next(me)
        yield i
except Exception as e:
    print("Occurred", type(e), e)


try:
    me = g()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 9')
    print(next(me)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f1():
        try:
            return
        except:
           yield 1
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 27')
    print(print(list(f1()))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f2():
        try:
            raise StopIteration
        except:
            yield 42
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 38')
    print(print(list(f2()))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        return 1//0
    def g():
        yield f()  # the zero division exception propagates
        yield 42   # and we'll never get here
except Exception as e:
    print("Occurred", type(e), e)


try:
    k = g()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 53')
    print(next(k)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 60')
    print(next(k)  # and the generator cannot be resumed
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        try:
            yield 1
            try:
                yield 2
                1//0
                yield 3  # never get here
            except ZeroDivisionError:
                yield 4
                yield 5
                raise
            except:
                yield 6
            yield 7     # the "raise" above stops this
        except:
            yield 8
        yield 9
        try:
            x = 12
        finally:
            yield 10
        yield 11
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 90')
    print(print(list(f()))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    class Tree:

        def __init__(self, label, left=None, right=None):
            self.label = label
            self.left = left
            self.right = right

        def __repr__(self, level=0, indent="    "):
            s = level*indent + repr(self.label)
            if self.left:
                s = s + "\n" + self.left.__repr__(level+1, indent)
            if self.right:
                s = s + "\n" + self.right.__repr__(level+1, indent)
            return s

        def __iter__(self):
            return inorder(self)
    #
    def tree(list):
        n = len(list)
        if n == 0:
            return []
        i = n // 2
        return Tree(list[i], tree(list[:i]), tree(list[i+1:]))
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    t = tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
except Exception as e:
    print("Occurred", type(e), e)


try:
    def inorder(t):
        if t:
            for x in inorder(t.left):
                yield x
            yield t.label
            for x in inorder(t.right):
                yield x
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    t = tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
except Exception as e:
    print("Occurred", type(e), e)

################################################################################

try:
    def g():
        for i in range(3):
            yield None
        yield None
        return
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 7')
    print(list(g())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def g():
        yield 1
        try:
            raise StopIteration
        except:
            yield 2
        yield 3
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 21')
    print(list(g())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def gcomb(x, k):
        "Generate all combinations of k elements from list x."

        if k > len(x):
            return
        if k == 0:
            yield []
        else:
            first, rest = x[0], x[1:]
            # A combination does or doesn't contain first.
            # If it does, the remainder is a k-1 comb of rest.
            for c in gcomb(rest, k-1):
                c.insert(0, first)
                yield c
            # If it doesn't contain first, it's a k comb of rest.
            for c in gcomb(rest, k):
                yield c
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    seq = list(range(1, 5))
except Exception as e:
    print("Occurred", type(e), e)


try:
    for k in range(len(seq) + 2):
        print("%d-combs of %s:" % (k, seq))
        for c in gcomb(seq, k):
            print("   ", c)
    # Expected:
    ## 0-combs of [1, 2, 3, 4]:
    ##     []
    ## 1-combs of [1, 2, 3, 4]:
    ##     [1]
    ##     [2]
    ##     [3]
    ##     [4]
    ## 2-combs of [1, 2, 3, 4]:
    ##     [1, 2]
    ##     [1, 3]
    ##     [1, 4]
    ##     [2, 3]
    ##     [2, 4]
    ##     [3, 4]
    ## 3-combs of [1, 2, 3, 4]:
    ##     [1, 2, 3]
    ##     [1, 2, 4]
    ##     [1, 3, 4]
    ##     [2, 3, 4]
    ## 4-combs of [1, 2, 3, 4]:
    ##     [1, 2, 3, 4]
    ## 5-combs of [1, 2, 3, 4]:
    #
    # From the Iterators list, about the types of these things.
    #
    def g():
        yield 1
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 78')
    print(type(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    i = g()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 82')
    print(type(i)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 88')
    print(print(i.__next__.__doc__)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 91')
    print(iter(i) is i
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    import types
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 101')
    print(i.gi_running
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    i.gi_running = 42
except Exception as e:
    print("Occurred", type(e), e)


try:
    def g():
        yield me.gi_running
except Exception as e:
    print("Occurred", type(e), e)


try:
    me = g()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 115')
    print(me.gi_running
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 118')
    print(next(me)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 121')
    print(me.gi_running
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    class disjointSet:
        def __init__(self, name):
            self.name = name
            self.parent = None
            self.generator = self.generate()

        def generate(self):
            while not self.parent:
                yield self
            for x in self.parent.generator:
                yield x

        def find(self):
            return next(self.generator)

        def union(self, parent):
            if self.parent:
                raise ValueError("Sorry, I'm not a root!")
            self.parent = parent

        def __str__(self):
            return self.name
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    names = "ABCDEFGHIJKLM"
except Exception as e:
    print("Occurred", type(e), e)


try:
    sets = [disjointSet(name) for name in names]
except Exception as e:
    print("Occurred", type(e), e)


try:
    roots = sets[:]
except Exception as e:
    print("Occurred", type(e), e)


try:
    import random
except Exception as e:
    print("Occurred", type(e), e)


try:
    gen = random.Random(42)
except Exception as e:
    print("Occurred", type(e), e)

################################################################################

try:
    def f():
       yield 1
       yield 2
    #
    for i in f():
        print(i)
    # Expected:
    ## 1
    ## 2
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 12')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 15')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 21')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        yield 1
        return
        yield 2 # never reached
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 35')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 38')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 44')
    print(next(g) # once stopped, can't be resumed
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        yield 1
        raise StopIteration
        yield 2 # never reached
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 57')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 60')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 65')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def g1():
        try:
            return
        except:
            yield 1
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 78')
    print(list(g1())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def g2():
        try:
            raise StopIteration
        except:
            yield 42
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 87')
    print(print(list(g2()))
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def g3():
        try:
            return
        finally:
            yield 1
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 98')
    print(list(g3())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def yrange(n):
        for i in range(n):
            yield i
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 107')
    print(list(yrange(5))
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
    print('Line 121')
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
    print('Line 134')
    print(list(zrange(5))
    )

except Exception as e:
    print("Occurred", type(e), e)

################################################################################

try:
    import itertools
except Exception as e:
    print("Occurred", type(e), e)


try:
    def leak():
        class gen:
            def __iter__(self):
                return self
            def __next__(self):
                return self.item
        g = gen()
        head, tail = itertools.tee(g)
        g.item = head
        return head
except Exception as e:
    print("Occurred", type(e), e)


try:
    it = leak()
except Exception as e:
    print("Occurred", type(e), e)


try:
    item = next(it)
except Exception as e:
    print("Occurred", type(e), e)


try:
    def leak():
       def gen():
           while True:
               yield g
       g = gen()
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 34')
    print(leak()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    import sys, io
except Exception as e:
    print("Occurred", type(e), e)


try:
    old = sys.stderr
except Exception as e:
    print("Occurred", type(e), e)

################################################################################

try:
    import weakref
except Exception as e:
    print("Occurred", type(e), e)


try:
    def gen():
        yield 'foo!'
except Exception as e:
    print("Occurred", type(e), e)


try:
    wr = weakref.ref(gen)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 6')
    print(wr() is gen
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    p = weakref.proxy(gen)
except Exception as e:
    print("Occurred", type(e), e)


try:
    gi = gen()
except Exception as e:
    print("Occurred", type(e), e)


try:
    wr = weakref.ref(gi)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 15')
    print(wr() is gi
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    p = weakref.proxy(gi)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 19')
    print(list(p)
    )

except Exception as e:
    print("Occurred", type(e), e)

################################################################################

try:
    def f():
        print((yield 1))
        yield 2
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 6')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 9')
    print(g.send(42)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 16')
    print(f().send("foo")
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(): yield
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 26')
    print(list(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(): list(i for i in [(yield 26)])
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 41')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def coroutine(seq):
        count = 0
        while count < 200:
            count += yield
            seq.append(count)
except Exception as e:
    print("Occurred", type(e), e)


try:
    seq = []
except Exception as e:
    print("Occurred", type(e), e)


try:
    c = coroutine(seq)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 55')
    print(next(c)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 56')
    print(print(seq)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 59')
    print(c.send(10)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 60')
    print(print(seq)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 63')
    print(c.send(10)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 64')
    print(print(seq)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 67')
    print(c.send(10)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 68')
    print(print(seq)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        while True:
            try:
                print((yield))
            except ValueError as v:
                print("caught ValueError (%s)" % (v))
except Exception as e:
    print("Occurred", type(e), e)


try:
    import sys
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 116')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 118')
    print(g.throw(ValueError) # type only
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 122')
    print(g.throw(ValueError("xyz"))  # value only
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 126')
    print(g.throw(ValueError, ValueError(1))   # value+matching type
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 130')
    print(g.throw(ValueError, TypeError(1))  # mismatched type, rewrapped
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 134')
    print(g.throw(ValueError, ValueError(1), None)   # explicit None traceback
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 138')
    print(g.throw(ValueError(1), "foo")       # bad args
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 144')
    print(g.throw(ValueError, "foo", 23)      # bad args
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 150')
    print(g.throw("abc")
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 156')
    print(g.throw(0)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 162')
    print(g.throw(list)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def throw(g,exc):
        try:
            raise exc
        except:
            g.throw(*sys.exc_info())
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 173')
    print(throw(g,ValueError) # do it with traceback included
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 177')
    print(g.send(1)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 181')
    print(throw(g,TypeError)  # terminate the generator
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 191')
    print(g.send(2)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 197')
    print(g.throw(ValueError,6)       # throw on closed generator
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 203')
    print(f().throw(ValueError,7)     # throw on just-opened generator
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        try:
            yield
        except:
            raise
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    try:
        1/0
    except ZeroDivisionError as v:
        try:
            g.throw(v)
        except Exception as w:
            tb = w.__traceback__
except Exception as e:
    print("Occurred", type(e), e)


try:
    levels = 0
except Exception as e:
    print("Occurred", type(e), e)


try:
    while tb:
        levels += 1
        tb = tb.tb_next
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 232')
    print(levels >= 2
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        try: yield
        except GeneratorExit:
            print("exiting")
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 244')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 245')
    print(g.close()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 248')
    print(g.close()  # should be no-op now
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 250')
    print(f().close()  # close on just-opened generator should be fine
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(): yield      # an even simpler generator
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 253')
    print(f().close()         # close before opening
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 255')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 256')
    print(g.close()           # close normally
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        try: yield
        finally:
            print("exiting")
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 266')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    del g
except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        try: yield
        except Exception:
            print('except')
        finally:
            print('finally')
    #
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 282')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    del g
except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        try: yield
        except GeneratorExit:
            yield "foo!"
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 295')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 296')
    print(g.close()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 301')
    print(g.close()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    import sys, io
except Exception as e:
    print("Occurred", type(e), e)


try:
    old, sys.stderr = sys.stderr, io.StringIO()
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 309')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    del g
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 311')
    print(sys.stderr.getvalue().startswith("Exception RuntimeError: 'generator ignored GeneratorExit' in ")
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    sys.stderr = old
except Exception as e:
    print("Occurred", type(e), e)


try:
    def f():
        try: yield
        except GeneratorExit:
            raise TypeError("fie!")
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f()
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 324')
    print(next(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 325')
    print(g.close()
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(): x += yield
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 336')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(): x = yield
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 341')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(): lambda x=(yield): 1
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 346')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 351')
    print(type(f())
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    def f(d): d[(yield "a")] = d[(yield "b")] = 27
except Exception as e:
    print("Occurred", type(e), e)


try:
    data = [1,2]
except Exception as e:
    print("Occurred", type(e), e)


try:
    g = f(data)
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 358')
    print(type(g)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 361')
    print(g.send(None)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 364')
    print(data
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 367')
    print(g.send(0)
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 370')
    print(data
    )

except Exception as e:
    print("Occurred", type(e), e)


try:
    try: g.send(1)
    except StopIteration: pass
except Exception as e:
    print("Occurred", type(e), e)


try:
    print('Line 375')
    print(data
    )

except Exception as e:
    print("Occurred", type(e), e)
