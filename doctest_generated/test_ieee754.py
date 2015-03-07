
try:
    from sys import float_info as FI
except Exception as e:
    print( "Occured", type(e), e )


try:
    from math import *
except Exception as e:
    print( "Occured", type(e), e )


try:
    PI = pi
except Exception as e:
    print( "Occured", type(e), e )


try:
    E = e
except Exception as e:
    print( "Occured", type(e), e )


try:
    EPS = 1E-15
except Exception as e:
    print( "Occured", type(e), e )


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
except Exception as e:
    print( "Occured", type(e), e )


try:
    INF = float('inf')
except Exception as e:
    print( "Occured", type(e), e )


try:
    NINF = float('-inf')
except Exception as e:
    print( "Occured", type(e), e )


try:
    NAN = float('nan')
except Exception as e:
    print( "Occured", type(e), e )


try:
    INF
except Exception as e:
    print( "Occured", type(e), e )


try:
    NINF
except Exception as e:
    print( "Occured", type(e), e )


try:
    NAN
except Exception as e:
    print( "Occured", type(e), e )


try:
    isinf(INF), isinf(NINF), isnan(NAN)
except Exception as e:
    print( "Occured", type(e), e )


try:
    INF == -NINF
except Exception as e:
    print( "Occured", type(e), e )


try:
    INF * 0
except Exception as e:
    print( "Occured", type(e), e )


try:
    INF - INF
except Exception as e:
    print( "Occured", type(e), e )


try:
    INF / INF
except Exception as e:
    print( "Occured", type(e), e )


try:
    INF * INF
except Exception as e:
    print( "Occured", type(e), e )


try:
    1.5 * INF
except Exception as e:
    print( "Occured", type(e), e )


try:
    0.5 * INF
except Exception as e:
    print( "Occured", type(e), e )


try:
    INF / 1000
except Exception as e:
    print( "Occured", type(e), e )


try:
    NAN == NAN
except Exception as e:
    print( "Occured", type(e), e )


try:
    NAN < 0
except Exception as e:
    print( "Occured", type(e), e )


try:
    NAN >= 0
except Exception as e:
    print( "Occured", type(e), e )


try:
    1 + NAN
except Exception as e:
    print( "Occured", type(e), e )


try:
    1 * NAN
except Exception as e:
    print( "Occured", type(e), e )


try:
    0 * NAN
except Exception as e:
    print( "Occured", type(e), e )


try:
    1 ** NAN
except Exception as e:
    print( "Occured", type(e), e )


try:
    NAN ** 0
except Exception as e:
    print( "Occured", type(e), e )


try:
    0 ** NAN
except Exception as e:
    print( "Occured", type(e), e )


try:
    (1.0 + FI.epsilon) * NAN
except Exception as e:
    print( "Occured", type(e), e )


try:
    pow(1, 0)
except Exception as e:
    print( "Occured", type(e), e )


try:
    pow(1, INF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    pow(1, -INF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    pow(1, NAN)
except Exception as e:
    print( "Occured", type(e), e )


try:
    pow(0, 0)
except Exception as e:
    print( "Occured", type(e), e )


try:
    pow(0, INF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    pow(0, -INF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    0 ** -1
except Exception as e:
    print( "Occured", type(e), e )


try:
    pow(0, NAN)
except Exception as e:
    print( "Occured", type(e), e )


try:
    sin(INF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    sin(NINF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    sin(NAN)
except Exception as e:
    print( "Occured", type(e), e )


try:
    cos(INF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    cos(NINF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    cos(NAN)
except Exception as e:
    print( "Occured", type(e), e )


try:
    tan(INF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    tan(NINF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    tan(NAN)
except Exception as e:
    print( "Occured", type(e), e )


try:
    tan(PI/2) > 1E10
except Exception as e:
    print( "Occured", type(e), e )


try:
    -tan(-PI/2) > 1E10
except Exception as e:
    print( "Occured", type(e), e )


try:
    tan(PI) < 1E-15
except Exception as e:
    print( "Occured", type(e), e )


try:
    asin(NAN), acos(NAN), atan(NAN)
except Exception as e:
    print( "Occured", type(e), e )


try:
    asin(INF), asin(NINF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    acos(INF), acos(NINF)
except Exception as e:
    print( "Occured", type(e), e )


try:
    equal(atan(INF), PI/2), equal(atan(NINF), -PI/2)
except Exception as e:
    print( "Occured", type(e), e )
