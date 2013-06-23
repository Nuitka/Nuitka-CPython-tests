
try:
    import getopt
except Exception, e:
    print "Occured", type(e), e


try:
    args = '-a -b -cfoo -d bar a1 a2'.split()
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 7'
    print args
except Exception, e:
    print "Occured", type(e), e


try:
    optlist, args = getopt.getopt(args, 'abc:d:')
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 11'
    print optlist
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 14'
    print args
except Exception, e:
    print "Occured", type(e), e


try:
    s = '--condition=foo --testing --output-file abc.def -x a1 a2'
except Exception, e:
    print "Occured", type(e), e


try:
    args = s.split()
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 23'
    print args
except Exception, e:
    print "Occured", type(e), e


try:
    optlist, args = getopt.getopt(args, 'x', [ 'condition=', 'output-file=', 'testing'])
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 27'
    print optlist
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 30'
    print args
except Exception, e:
    print "Occured", type(e), e
