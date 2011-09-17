from test.test_cmd import samplecmdclass

try:
    mycmd = samplecmdclass()
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 4'
    print mycmd.parseline("")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 7'
    print mycmd.parseline("?")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 10'
    print mycmd.parseline("?help")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 13'
    print mycmd.parseline("!")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 16'
    print mycmd.parseline("!command")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 19'
    print mycmd.parseline("func")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 22'
    print mycmd.parseline("func arg1")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 28'
    print mycmd.onecmd("")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 29'
    print mycmd.onecmd("add 4 5")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 32'
    print mycmd.onecmd("")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 35'
    print mycmd.onecmd("test")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 40'
    print mycmd.emptyline()
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 45'
    print mycmd.default("default")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 50'
    print mycmd.completedefault()
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 53'
    print mycmd.completenames("a")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 58'
    print mycmd.completenames("12")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 61'
    print mycmd.completenames("help")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 66'
    print mycmd.complete_help("a")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 69'
    print mycmd.complete_help("he")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 72'
    print mycmd.complete_help("12")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 77'
    print mycmd.do_help("testet")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 80'
    print mycmd.do_help("add")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 83'
    print mycmd.onecmd("help add")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 86'
    print mycmd.do_help("")
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 99'
    print mycmd.print_topics("header", ["command1", "command2"], 2 ,10)
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 108'
    print mycmd.columnize([str(i) for i in xrange(20)])
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 111'
    print mycmd.columnize([str(i) for i in xrange(20)], 10)
except Exception, e:
    print "Occured", type(e), e


try:
    mycmd.use_rawinput=0
except Exception, e:
    print "Occured", type(e), e


try:
    mycmd.cmdqueue=["", "add", "add 4 5", "help", "help add","exit"]
except Exception, e:
    print "Occured", type(e), e


try:
    print 'Line 127'
    print mycmd.cmdloop()
except Exception, e:
    print "Occured", type(e), e
