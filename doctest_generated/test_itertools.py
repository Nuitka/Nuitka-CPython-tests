from itertools import *

try:
    amounts = [120.15, 764.05, 823.14]
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    for checknum, amount in izip(count(1200), amounts):
        print 'Check %d is for $%.2f' % (checknum, amount)
    # Expected:
    ## Check 1200 is for $120.15
    ## Check 1201 is for $764.05
    ## Check 1202 is for $823.14
    #
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    import operator
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    for cube in imap(operator.pow, xrange(1,4), repeat(3)):
       print cube
    # Expected:
    ## 1
    ## 8
    ## 27
    #
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    reportlines = ['EuroPython', 'Roster', '', 'alex', '', 'laura', '', 'martin', '', 'walter', '', 'samuele']
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    for name in islice(reportlines, 3, None, 2):
       print name.title()
    # Expected:
    ## Alex
    ## Laura
    ## Martin
    ## Walter
    ## Samuele
    #
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    from operator import itemgetter
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    di = sorted(sorted(d.iteritems()), key=itemgetter(1))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    for k, g in groupby(di, itemgetter(1)):
        print k, map(itemgetter(0), g)
    # Expected:
    ## 1 ['a', 'c', 'e']
    ## 2 ['b', 'd', 'f']
    ## 3 ['g']
    #
    # # Find runs of consecutive numbers using groupby.  The key to the solution
    # # is differencing with a range so that consecutive numbers all appear in
    # # same group.
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    data = [ 1,  4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    for k, g in groupby(enumerate(data), lambda t:t[0]-t[1]):
        print map(operator.itemgetter(1), g)
    # Expected:
    ## [1]
    ## [4, 5, 6]
    ## [10]
    ## [15, 16, 17, 18]
    ## [22]
    ## [25, 26, 27, 28]
    #
    def take(n, iterable):
        "Return first n items of the iterable as a list"
        return list(islice(iterable, n))
    #
    def enumerate(iterable, start=0):
        return izip(count(start), iterable)
    #
    def tabulate(function, start=0):
        "Return function(0), function(1), ..."
        return imap(function, count(start))
    #
    def nth(iterable, n, default=None):
        "Returns the nth item or a default value"
        return next(islice(iterable, n, None), default)
    #
    def quantify(iterable, pred=bool):
        "Count how many times the predicate is true"
        return sum(imap(pred, iterable))
    #
    def padnone(iterable):
        "Returns the sequence elements and then returns None indefinitely"
        return chain(iterable, repeat(None))
    #
    def ncycles(iterable, n):
        "Returns the seqeuence elements n times"
        return chain(*repeat(iterable, n))
    #
    def dotproduct(vec1, vec2):
        return sum(imap(operator.mul, vec1, vec2))
    #
    def flatten(listOfLists):
        return list(chain.from_iterable(listOfLists))
    #
    def repeatfunc(func, times=None, *args):
        "Repeat calls to func with specified arguments."
        "   Example:  repeatfunc(random.random)"
        if times is None:
            return starmap(func, repeat(args))
        else:
            return starmap(func, repeat(args, times))
    #
    def pairwise(iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = tee(iterable)
        for elem in b:
            break
        return izip(a, b)
    #
    def grouper(n, iterable, fillvalue=None):
        "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return izip_longest(fillvalue=fillvalue, *args)
    #
    def roundrobin(*iterables):
        "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
        # Recipe credited to George Sakkis
        pending = len(iterables)
        nexts = cycle(iter(it).next for it in iterables)
        while pending:
            try:
                for next in nexts:
                    yield next()
            except StopIteration:
                pending -= 1
                nexts = cycle(islice(nexts, pending))
    #
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    #
    def compress(data, selectors):
        "compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F"
        return (d for d, s in izip(data, selectors) if s)
    #
    def combinations_with_replacement(iterable, r):
        "combinations_with_replacement('ABC', 3) --> AA AB AC BB BC CC"
        pool = tuple(iterable)
        n = len(pool)
        if not n and r:
            return
        indices = [0] * r
        yield tuple(pool[i] for i in indices)
        while 1:
            for i in reversed(range(r)):
                if indices[i] != n - 1:
                    break
            else:
                return
            indices[i:] = [indices[i] + 1] * (r - i)
            yield tuple(pool[i] for i in indices)
    #
    def unique_everseen(iterable, key=None):
        "List unique elements, preserving order. Remember all elements ever seen."
        # unique_everseen('AAAABBBCCDAABBB') --> A B C D
        # unique_everseen('ABBCcAD', str.lower) --> A B C D
        seen = set()
        seen_add = seen.add
        if key is None:
            for element in iterable:
                if element not in seen:
                    seen_add(element)
                    yield element
        else:
            for element in iterable:
                k = key(element)
                if k not in seen:
                    seen_add(k)
                    yield element
    #
    def unique_justseen(iterable, key=None):
        "List unique elements, preserving order. Remember only the element just seen."
        # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
        # unique_justseen('ABBCcAD', str.lower) --> A B C A D
        return imap(next, imap(itemgetter(1), groupby(iterable, key)))
    #
    # This is not part of the examples but it tests to make sure the definitions
    # perform as purported.
    #
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 172'
    print take(10, count())
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 176'
    print list(enumerate('abc'))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 180'
    print list(islice(tabulate(lambda x: 2*x), 4))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 184'
    print nth('abcde', 3)
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 188'
    print nth('abcde', 9) is None
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 192'
    print quantify(xrange(99), lambda x: x%2==0)
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a = [[1, 2, 3], [4, 5, 6]]
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 197'
    print flatten(a)
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 201'
    print list(repeatfunc(pow, 5, 2, 3))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    import random
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 206'
    print take(5, imap(int, repeatfunc(random.random)))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 210'
    print list(pairwise('abcd'))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 214'
    print list(pairwise([]))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 218'
    print list(pairwise('a'))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 222'
    print list(islice(padnone('abc'), 0, 6))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 226'
    print list(ncycles('abc', 3))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 230'
    print dotproduct([1,2,3], [4,5,6])
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 234'
    print list(grouper(3, 'abcdefg', 'x'))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 238'
    print list(roundrobin('abc', 'd', 'ef'))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 242'
    print list(powerset([1,2,3]))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 246'
    print list(compress('abcdef', [1,0,1,0,1,1]))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 250'
    print list(combinations_with_replacement('abc', 2))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 254'
    print list(combinations_with_replacement('01', 3))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    def combinations_with_replacement2(iterable, r):
        'Alternate version that filters from product()'
        pool = tuple(iterable)
        n = len(pool)
        for indices in product(range(n), repeat=r):
            if sorted(indices) == list(indices):
                yield tuple(pool[i] for i in indices)
    #
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 266'
    print list(combinations_with_replacement('abc', 2)) == list(combinations_with_replacement2('abc', 2))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 270'
    print list(combinations_with_replacement('01', 3)) == list(combinations_with_replacement2('01', 3))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 274'
    print list(combinations_with_replacement('2310', 6)) == list(combinations_with_replacement2('2310', 6))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 278'
    print list(unique_everseen('AAAABBBCCDAABBB'))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 282'
    print list(unique_everseen('ABBCcAD', str.lower))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 286'
    print list(unique_justseen('AAAABBBCCDAABBB'))
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 290'
    print list(unique_justseen('ABBCcAD', str.lower))
except Exception as __e:
    print "Occurred", type(__e), __e
