
try:
    k = "old value"
except Exception as e:
    print( "Occured", type(e), e )


try:
    { k: None for k in range(10) }
except Exception as e:
    print( "Occured", type(e), e )


try:
    k
except Exception as e:
    print( "Occured", type(e), e )


try:
    { k: k+10 for k in range(10) }
except Exception as e:
    print( "Occured", type(e), e )


try:
    g = "Global variable"
except Exception as e:
    print( "Occured", type(e), e )


try:
    { k: g for k in range(10) }
except Exception as e:
    print( "Occured", type(e), e )


try:
    { k: v for k in range(10) for v in range(10) if k == v }
except Exception as e:
    print( "Occured", type(e), e )


try:
    { k: v for v in range(10) for k in range(v*9, v*10) }
except Exception as e:
    print( "Occured", type(e), e )
