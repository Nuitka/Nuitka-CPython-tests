from test.test_cmd import samplecmdclass

try:
    mycmd = samplecmdclass()
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.parseline("")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.parseline("?")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.parseline("?help")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.parseline("!")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.parseline("!command")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.parseline("func")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.parseline("func arg1")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.onecmd("")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.onecmd("add 4 5")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.onecmd("")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.onecmd("test")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.emptyline()
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.default("default")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.completedefault()
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.completenames("a")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.completenames("12")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.completenames("help")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.complete_help("a")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.complete_help("he")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.complete_help("12")
except Exception as e:
    print( "Occured", type(e), e )


try:
    sorted(mycmd.complete_help(""))
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.do_help("testet")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.do_help("add")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.onecmd("help add")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.do_help("")
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.print_topics("header", ["command1", "command2"], 2 ,10)
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.columnize([str(i) for i in range(20)])
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.columnize([str(i) for i in range(20)], 10)
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.use_rawinput=0
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.cmdqueue=["", "add", "add 4 5", "help", "help add","exit"]
except Exception as e:
    print( "Occured", type(e), e )


try:
    mycmd.cmdloop()
except Exception as e:
    print( "Occured", type(e), e )
