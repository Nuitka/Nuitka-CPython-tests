
try:
    grades = "FEDCBA"
except Exception, e:
    print "Occured", type(e), e


try:
    breakpoints = [30, 44, 66, 75, 85]
except Exception, e:
    print "Occured", type(e), e


try:
    from bisect import bisect
except Exception, e:
    print "Occured", type(e), e


try:
    def grade(total):
              return grades[bisect(breakpoints, total)]
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 12'
    print grade(66)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 15'
    print map(grade, [33, 99, 77, 44, 12, 88])
except Exception, e:
    print "Occured", type(e), e
