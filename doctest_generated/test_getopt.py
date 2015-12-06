
try:
    import getopt
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    args = '-a -b -cfoo -d bar a1 a2'.split()
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 7'
    print args
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    optlist, args = getopt.getopt(args, 'abc:d:')
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 11'
    print optlist
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 14'
    print args
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    s = '--condition=foo --testing --output-file abc.def -x a1 a2'
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    args = s.split()
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 23'
    print args
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    optlist, args = getopt.getopt(args, 'x', [ 'condition=', 'output-file=', 'testing'])
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 27'
    print optlist
except Exception as __e:
    print "Occurred", type(__e), __e


try:
    print 'Line 30'
    print args
except Exception as __e:
    print "Occurred", type(__e), __e
