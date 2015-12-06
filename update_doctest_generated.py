#!/usr/bin/python2.7

# This script should be run each time the CPython test suite is updated. It
# extracts the doctests from the objects specified manually inside this script,
# and converts them into proper statements.

# Find common code relative in file system. Not using packages for test stuff.
import sys, os
sys.path.insert(
    0,
    os.path.normpath(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            ".."
        )
    )
)
from test_common import (
    convertToPython,
)

import test.test_bisect
script = convertToPython(test.test_bisect.libreftest)
open("doctest_generated/test_bisect.py", 'w').write(script)

import test.test_cmd
script = "from test.test_cmd import samplecmdclass\n" + convertToPython(test.test_cmd.samplecmdclass.__doc__)
open("doctest_generated/test_cmd.py", 'w').write(script)

import test.test_deque
script = convertToPython(test.test_deque.libreftest)
open("doctest_generated/test_deque.py", 'w').write(script)

import test.test_descrtut

script = "from test.test_descrtut import defaultdict,defaultdict2,sortdict\nimport pprint\n"
for test in test.test_descrtut.__test__.values():
    script += convertToPython(test)
open("doctest_generated/test_descrtut.py", 'w').write(script)

import test.test_extcall
script = "import test.test_support as test_support\n" + convertToPython(test.test_extcall.__doc__)
open("doctest_generated/test_extcall.py", 'w').write(script)

import test.test_generators

def filter_generators(line):
    if line.find("(yield 21)") != -1:
        return True
    elif line.find("gi_frame") != -1:
        return True
    elif line.find("gi_code") != -1:
        return True
    elif line.find("dir(i)") != -1:
        return True
    elif line.find("(i for i in (yield) if (yield))") != -1:
        return True
    elif line.find("isinstance(i, types.GeneratorType)") != -1:
        return True
    else:
        return False


script = "from test.test_generators import Knights"
for test in test.test_generators.__test__.values():
    script += '\n'
    script += '#' * 80
    script += '\n'
    script += convertToPython(test, filter_generators)

open("doctest_generated/test_generators.py", 'w').write(script)

def filter_genexps(line):
    if line.find("set(attr for attr in dir(g) if not attr.startswith('__')) >= expected") != -1:
        return True
    elif line.find("isinstance(g, types.GeneratorType)") != -1:
        return True
    else:
        return False

import test.test_genexps
script = convertToPython(test.test_genexps.doctests, filter_genexps)
open("doctest_generated/test_genexps.py", 'w').write(script)

import test.test_getopt
script = convertToPython(test.test_getopt.GetoptTests.test_libref_examples.im_func.func_code.co_consts[1])
open("doctest_generated/test_getopt.py", 'w').write(script)

import test.test_itertools
script = "from itertools import *\n" + convertToPython(test.test_itertools.libreftest)
open("doctest_generated/test_itertools.py", 'w').write(script)

import test.test_unpack
script = convertToPython(test.test_unpack.doctests)
open("doctest_generated/test_unpack.py", 'w').write(script)

import test.test_weakref
script = convertToPython(test.test_weakref.libreftest)
open("doctest_generated/test_weakref.py", 'w').write(script)

script = convertToPython(open("test/ieee754.txt").read())
open("doctest_generated/test_ieee754.py", 'w').write(script)
