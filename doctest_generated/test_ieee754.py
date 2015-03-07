
try:
    from sys import float_info as FI
except Exception, e:
    print "Occured", type(e), e


try:
    from math import *
except Exception, e:
    print "Occured", type(e), e


try:
    PI = pi
except Exception, e:
    print "Occured", type(e), e


try:
    E = e
except Exception, e:
    print "Occured", type(e), e


try:
    EPS = 1E-15
except Exception, e:
    print "Occured", type(e), e


try:
    def equal(x, y):
        """Almost equal helper for floats"""
        return abs(x - y) < EPS
    #
    #
    # NaNs and INFs
    # =============
    #
    # In Python 2.6 and newer NaNs (not a number) and infinity can be constructed
    # from the strings 'inf' and 'nan'.
    #
except Exception, e:
    print "Occured", type(e), e


try:
    INF = float('inf')
except Exception, e:
    print "Occured", type(e), e


try:
    NINF = float('-inf')
except Exception, e:
    print "Occured", type(e), e


try:
    NAN = float('nan')
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 28'
    print INF
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 31'
    print NINF
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 34'
    print NAN
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 40'
    print isinf(INF), isinf(NINF), isnan(NAN)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 43'
    print INF == -NINF
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 51'
    print INF * 0
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 54'
    print INF - INF
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 57'
    print INF / INF
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 62'
    print INF * INF
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 65'
    print 1.5 * INF
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 68'
    print 0.5 * INF
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 71'
    print INF / 1000
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 79'
    print NAN == NAN
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 82'
    print NAN < 0
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 85'
    print NAN >= 0
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 90'
    print 1 + NAN
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 93'
    print 1 * NAN
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 96'
    print 0 * NAN
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 99'
    print 1 ** NAN
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 102'
    print NAN ** 0
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 105'
    print 0 ** NAN
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 108'
    print (1.0 + FI.epsilon) * NAN
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 118'
    print pow(1, 0)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 121'
    print pow(1, INF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 124'
    print pow(1, -INF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 127'
    print pow(1, NAN)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 135'
    print pow(0, 0)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 138'
    print pow(0, INF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 141'
    print pow(0, -INF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 146'
    print 0 ** -1
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 151'
    print pow(0, NAN)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 159'
    print sin(INF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 164'
    print sin(NINF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 169'
    print sin(NAN)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 172'
    print cos(INF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 177'
    print cos(NINF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 182'
    print cos(NAN)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 185'
    print tan(INF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 190'
    print tan(NINF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 195'
    print tan(NAN)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 201'
    print tan(PI/2) > 1E10
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 204'
    print -tan(-PI/2) > 1E10
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 207'
    print tan(PI) < 1E-15
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 211'
    print asin(NAN), acos(NAN), atan(NAN)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 214'
    print asin(INF), asin(NINF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 219'
    print acos(INF), acos(NINF)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 224'
    print equal(atan(INF), PI/2), equal(atan(NINF), -PI/2)
except Exception, e:
    print "Occured", type(e), e
