#!/usr/bin/env python2.7

# This script should be run each time the CPython test suite is updated. It
# extracts the doctests from the objects specified manually inside this script,
# and converts them into proper statements.

import doctest, os, ast

def _indentedCode( codes, count ):
    return "\n".join( " " * count + line if line else "" for line in codes )

def convertToPython( doctests, line_filter = None ):
    code = doctest.script_from_examples( doctests )

    if code.endswith( "\n" ):
        code +=  "#\n"
    else:
        assert False

    output = []
    inside = False

    def getPrintPrefixed( evaluated ):
        try:
            count = 0

            while evaluated.startswith( " " * count ):
                count += 1

            modified = (count-1) * " " + "print " + evaluated

            compile( modified, "dummy", "exec", ast.PyCF_ONLY_AST )
            return (count-1) * " " + ("print 'Line %d'" % line_number) + "\n" + modified
        except SyntaxError:
            return evaluated

    def getTried( evaluated ):
        return """
try:
%(evaluated)s
except Exception, e:
    print "Occured", type(e), e
""" % { "evaluated" : _indentedCode( getPrintPrefixed( evaluated ).split("\n"), 4 ) }

    def isOpener( evaluated ):
        evaluated = evaluated.lstrip()

        if evaluated == "":
            return False

        if evaluated.split()[0] in ( "def", "class", "for", "while", "try:", "except", "except:", "finally:", "else:" ):
            return True
        else:
            return False

    for line_number, line in enumerate( code.split("\n") ):
        # print "->", inside, line

        if line_filter is not None and line_filter( line ):
            continue

        if inside and len( line ) > 0 and line[0].isalnum() and not isOpener( line ):
            output.append( getTried( "\n".join( chunk ) ) )

            chunk = []
            inside = False

        if inside and not (line.startswith( "#" ) and line.find( "SyntaxError:" ) != -1):
            chunk.append( line )
        elif line.startswith( "#" ):
            if line.find( "SyntaxError:" ) != -1:
                # print "Syntax error detected"

                if inside:
                    # print "Dropping chunk", chunk

                    chunk = []
                    inside = False
                else:
                    del output[-1]
        elif isOpener( line ):
            inside = True
            chunk = [ line ]
        elif line.strip() == "":
            output.append( line )
        else:
            output.append( getTried( line ) )


    return "\n".join( output ).rstrip() + "\n"



import test.test_setcomps
script = convertToPython( test.test_setcomps.doctests )

if not os.path.exists( "doctest_generated" ):
    os.mkdir( "doctest_generated" )

open( "doctest_generated/test_setcomps.py", "w" ).write( script )

import test.test_bisect
script = convertToPython( test.test_bisect.libreftest )
open( "doctest_generated/test_bisect.py", "w" ).write( script )

import test.test_cmd
script = "from test.test_cmd import samplecmdclass\n" + convertToPython( test.test_cmd.samplecmdclass.__doc__ )
open( "doctest_generated/test_cmd.py", "w" ).write( script )

import test.test_deque
script = convertToPython( test.test_deque.libreftest )
open( "doctest_generated/test_deque.py", "w" ).write( script )

import test.test_descrtut

script = "from test.test_descrtut import defaultdict,defaultdict2,sortdict\nimport pprint\n"
for test in test.test_descrtut.__test__.values():
    script += convertToPython( test )
open( "doctest_generated/test_descrtut.py", "w" ).write( script )

import test.test_dictcomps
script = convertToPython( test.test_dictcomps.doctests )
open( "doctest_generated/test_dictcomps.py", "w" ).write( script )

import test.test_extcall
script = "import test.test_support as test_support\n" + convertToPython( test.test_extcall.__doc__ )
open( "doctest_generated/test_extcall.py", "w" ).write( script )

import test.test_generators

def filter_generators( line ):
    if line.find( "(yield 21)" ) != -1:
        return True
    elif line.find( "gi_frame" ) != -1:
        return True
    elif line.find( "gi_code" ) != -1:
        return True
    elif line.find( "dir(i)" ) != -1:
        return True
    elif line.find( "(i for i in (yield) if (yield))" ) != -1:
        return True
    elif line.find( "isinstance(i, types.GeneratorType)" ) != -1:
        return True
    else:
        return False


script = "from test.test_generators import Knights"
for test in test.test_generators.__test__.values():
    script += "\n"
    script += "#" * 80
    script += "\n"
    script += convertToPython( test, filter_generators )

open( "doctest_generated/test_generators.py", "w" ).write( script )

def filter_genexps( line ):
    if line.find( "set(attr for attr in dir(g) if not attr.startswith('__')) >= expected" ) != -1:
        return True
    elif line.find( "isinstance(g, types.GeneratorType)" ) != -1:
        return True
    else:
        return False

import test.test_genexps
script = convertToPython( test.test_genexps.doctests, filter_genexps )
open( "doctest_generated/test_genexps.py", "w" ).write( script )

import test.test_getopt
script = convertToPython( test.test_getopt.GetoptTests.test_libref_examples.im_func.func_code.co_consts[1] )
open( "doctest_generated/test_getopt.py", "w" ).write( script )

import test.test_itertools
script = "from itertools import *\n" + convertToPython( test.test_itertools.libreftest )
open( "doctest_generated/test_itertools.py", "w" ).write( script )

import test.test_unpack
script = convertToPython( test.test_unpack.doctests )
open( "doctest_generated/test_unpack.py", "w" ).write( script )

import test.test_weakref
script = convertToPython( test.test_weakref.libreftest )
open( "doctest_generated/test_weakref.py", "w" ).write( script )

script = convertToPython(open("test/ieee754.txt").read())
open("doctest_generated/test_ieee754.py", "w" ).write(script)
