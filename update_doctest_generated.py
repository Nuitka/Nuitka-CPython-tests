#!/usr/bin/env python3.7

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
            "..",
            ".."
        )
    )
)

from nuitka.tools.testing.Common import (
    convertToPython,
    goMainDir

)
from nuitka.tools.quality.autoformat.Autoformat import (
    cleanupWindowsNewlines,
)

goMainDir()

if not os.path.exists("doctest_generated"):
    os.mkdir("doctest_generated")

def saveAsGeneratedDoctest(name, value, line_filter = None, prefix = ""):
    if prefix:
        prefix = prefix + "\n"

    filename = os.path.join("doctest_generated", name)

    with open(filename, 'w') as output:
        output.write(prefix)

        if type(value) in (tuple, list):
            for value in value:
                output.write('\n')
                output.write('#' * 80)
                output.write('\n')
                output.write(convertToPython(value, line_filter))
        else:
            output.write(convertToPython(value, line_filter))

    cleanupWindowsNewlines(filename)


import test.test_cmd
saveAsGeneratedDoctest("test_cmd.py", test.test_cmd.samplecmdclass.__doc__, prefix = "from test.test_cmd import samplecmdclass") # @UndefinedVariable

import test.test_deque
saveAsGeneratedDoctest("test_deque.py", test.test_deque.libreftest)

import test.test_descrtut
saveAsGeneratedDoctest("test_descrtut.py", tuple(sorted(test.test_descrtut.__test__.values())), prefix = "from test.test_descrtut import defaultdict,defaultdict2,sortdict\nimport pprint")

import test.test_extcall
saveAsGeneratedDoctest("test_extcall.py", test.test_extcall.__doc__, prefix = "import test.support as support") # @UndefinedVariable

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

saveAsGeneratedDoctest("test_generators.py", tuple(sorted(test.test_generators.__test__.values())), line_filter = filter_generators, prefix = "from test.test_generators import Knights")


def filter_genexps(line):
    if line.find("set(attr for attr in dir(g) if not attr.startswith('__')) >= expected") != -1:
        return True
    elif line.find("isinstance(g, types.GeneratorType)") != -1:
        return True
    else:
        return False

import test.test_genexps
saveAsGeneratedDoctest("test_genexps.py", test.test_genexps.doctests, line_filter = filter_genexps)

import test.test_itertools
saveAsGeneratedDoctest("test_itertools.py", test.test_itertools.libreftest, prefix = "from itertools import *")

import test.test_listcomps
saveAsGeneratedDoctest("test_listcomps.py", test.test_listcomps.doctests)

import test.test_setcomps
saveAsGeneratedDoctest("test_setcomps.py", test.test_setcomps.doctests)

import test.test_unpack
saveAsGeneratedDoctest("test_unpack.py", test.test_unpack.doctests)

import test.test_unpack_ex
saveAsGeneratedDoctest("test_unpack_ex.py", test.test_unpack_ex.doctests)

import test.test_weakref
saveAsGeneratedDoctest("test_weakref.py", test.test_weakref.libreftest)

saveAsGeneratedDoctest("test_ieee754.py", open("test/ieee754.txt").read())

import test.test_metaclass
saveAsGeneratedDoctest("test_metaclass.py", test.test_metaclass.doctests)
