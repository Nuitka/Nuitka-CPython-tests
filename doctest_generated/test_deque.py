
try:
    from collections import deque
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    d = deque('ghi')                 # make a new deque with three items
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    for elem in d:                   # iterate over the deque's elements
        print elem.upper()
    # Expected:
    ## G
    ## H
    ## I
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 10'
    print d.append('j')                    # add a new entry to the right side
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 11'
    print d.appendleft('f')                # add a new entry to the left side
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 12'
    print d                                # show the representation of the deque
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 15'
    print d.pop()                          # return and remove the rightmost item
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 18'
    print d.popleft()                      # return and remove the leftmost item
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 21'
    print list(d)                          # list the contents of the deque
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 24'
    print d[0]                             # peek at leftmost item
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 27'
    print d[-1]                            # peek at rightmost item
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 30'
    print list(reversed(d))                # list the contents of a deque in reverse
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 33'
    print 'h' in d                         # search the deque
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 36'
    print d.extend('jkl')                  # add multiple elements at once
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 37'
    print d
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 40'
    print d.rotate(1)                      # right rotation
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 41'
    print d
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 44'
    print d.rotate(-1)                     # left rotation
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 45'
    print d
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 48'
    print deque(reversed(d))               # make a new deque in reverse order
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 51'
    print d.clear()                        # empty the deque
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 52'
    print d.pop()                          # cannot pop from an empty deque
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 59'
    print d.extendleft('abc')              # extendleft() reverses the input order
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 60'
    print d
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    def delete_nth(d, n):
        d.rotate(-n)
        d.popleft()
        d.rotate(n)
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    d = deque('abcdef')
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 71'
    print delete_nth(d, 2)   # remove the entry at d[2]
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 72'
    print d
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    def roundrobin(*iterables):
        pending = deque(iter(i) for i in iterables)
        while pending:
            task = pending.popleft()
            try:
                yield task.next()
            except StopIteration:
                continue
            pending.append(task)
    #
    for value in roundrobin('abc', 'd', 'efgh'):
        print value
    # Expected:
    ## a
    ## d
    ## e
    ## b
    ## f
    ## c
    ## g
    ## h
    #
    #
    def maketree(iterable):
        d = deque(iterable)
        while len(d) > 1:
            pair = [d.popleft(), d.popleft()]
            d.append(pair)
        return list(d)
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print maketree('abcdefgh')
except Exception as __e:
    print "Occurred", type(__e), __e
