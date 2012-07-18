
try:
    grades = "FEDCBA"
except Exception as e:
    print( "Occured", type(e), e )


try:
    breakpoints = [30, 44, 66, 75, 85]
except Exception as e:
    print( "Occured", type(e), e )


try:
    from bisect import bisect
except Exception as e:
    print( "Occured", type(e), e )


try:
    def grade(total):
              return grades[bisect(breakpoints, total)]
except Exception as e:
    print( "Occured", type(e), e )


try:
    grade(66)
except Exception as e:
    print( "Occured", type(e), e )


try:
    list(map(grade, [33, 99, 77, 44, 12, 88]))
except Exception as e:
    print( "Occured", type(e), e )
