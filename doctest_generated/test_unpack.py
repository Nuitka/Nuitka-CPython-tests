
try:
    t = (1, 2, 3)
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b, c = t
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 4'
    print a == 1 and b == 2 and c == 3
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    l = [4, 5, 6]
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b, c = l
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 12'
    print a == 4 and b == 5 and c == 6
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b, c = 7, 8, 9
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 19'
    print a == 7 and b == 8 and c == 9
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b, c = 'one'
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 26'
    print a == 'o' and b == 'n' and c == 'e'
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    class Seq:
        def __getitem__(self, i):
            if i >= 0 and i < 3: return i
            raise IndexError
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b, c = Seq()
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 37'
    print a == 0 and b == 1 and c == 2
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    st = (99,)
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    sl = [100]
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, = st
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 46'
    print a
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    b, = sl
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 50'
    print b
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b, c = 7
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b = t
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b = l
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b, c, d = Seq()
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b = Seq()
except Exception as __e:
    print "Occurred", type(__e), __e


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
    print "Occurred", type(__e), __e


try:
    a, b, c, d, e = BadSeq()
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    a, b, c = BadSeq()
except Exception as __e:
    print "Occurred", type(__e), __e
