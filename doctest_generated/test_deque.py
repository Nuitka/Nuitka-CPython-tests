
try:
    from collections import deque
except Exception as e:
    print( "Occured", type(e), e )


try:
    d = deque('ghi')                 # make a new deque with three items
except Exception as e:
    print( "Occured", type(e), e )


try:
    for elem in d:                   # iterate over the deque's elements
        print(elem.upper())
    # Expected:
    ## G
    ## H
    ## I
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.append('j')                    # add a new entry to the right side
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.appendleft('f')                # add a new entry to the left side
except Exception as e:
    print( "Occured", type(e), e )


try:
    d                                # show the representation of the deque
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.pop()                          # return and remove the rightmost item
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.popleft()                      # return and remove the leftmost item
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(d)                          # list the contents of the deque
except Exception as e:
    print( "Occured", type(e), e )


try:
    d[0]                             # peek at leftmost item
except Exception as e:
    print( "Occured", type(e), e )


try:
    d[-1]                            # peek at rightmost item
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(reversed(d))                # list the contents of a deque in reverse
except Exception as e:
    print( "Occured", type(e), e )


try:
    'h' in d                         # search the deque
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.extend('jkl')                  # add multiple elements at once
except Exception as e:
    print( "Occured", type(e), e )


try:
    d
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.rotate(1)                      # right rotation
except Exception as e:
    print( "Occured", type(e), e )


try:
    d
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.rotate(-1)                     # left rotation
except Exception as e:
    print( "Occured", type(e), e )


try:
    d
except Exception as e:
    print( "Occured", type(e), e )


try:
    deque(reversed(d))               # make a new deque in reverse order
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.clear()                        # empty the deque
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.pop()                          # cannot pop from an empty deque
except Exception as e:
    print( "Occured", type(e), e )


try:
    d.extendleft('abc')              # extendleft() reverses the input order
except Exception as e:
    print( "Occured", type(e), e )


try:
    d
except Exception as e:
    print( "Occured", type(e), e )


try:
    def delete_nth(d, n):
        d.rotate(-n)
        d.popleft()
        d.rotate(n)
except Exception as e:
    print( "Occured", type(e), e )


try:
    d = deque('abcdef')
except Exception as e:
    print( "Occured", type(e), e )


try:
    delete_nth(d, 2)   # remove the entry at d[2]
except Exception as e:
    print( "Occured", type(e), e )


try:
    d
except Exception as e:
    print( "Occured", type(e), e )


try:
    def roundrobin(*iterables):
        pending = deque(iter(i) for i in iterables)
        while pending:
            task = pending.popleft()
            try:
                yield next(task)
            except StopIteration:
                continue
            pending.append(task)
    #
    for value in roundrobin('abc', 'd', 'efgh'):
        print(value)
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
except Exception as e:
    print( "Occured", type(e), e )


try:
    print(maketree('abcdefgh'))
except Exception as e:
    print( "Occured", type(e), e )
