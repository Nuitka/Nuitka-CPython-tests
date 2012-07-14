
try:
    k = "old value"
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 1'
    print { k: None for k in range(10) }
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 4'
    print k
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 8'
    print { k: k+10 for k in range(10) }
except Exception, e:
    print "Occured", type(e), e


try:
    g = "Global variable"
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 13'
    print { k: g for k in range(10) }
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 17'
    print { k: v for k in range(10) for v in range(10) if k == v }
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 21'
    print { k: v for v in range(10) for k in range(v*9, v*10) }
except Exception, e:
    print "Occured", type(e), e
