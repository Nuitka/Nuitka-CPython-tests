#!/usr/bin/env python3.10

""" This script should be run each time the CPython test suite is updated.

It extracts the doctests from the objects specified manually inside this script,
and converts them into proper statements that then can be subject to real tests
with Nuitka compilation.

"""

# Find common code relative in file system. Not using packages for test stuff.
import os
import sys

sys.path.insert(
    0,
    os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    ),
)

# isort:start
import test.test_cmd
import test.test_deque
import test.test_descrtut
import test.test_extcall
import test.test_generators
import test.test_genexps
import test.test_itertools
import test.test_listcomps
import test.test_metaclass
import test.test_setcomps
import test.test_unpack
import test.test_unpack_ex
import test.test_weakref

from nuitka.tools.quality.autoformat.Autoformat import cleanupWindowsNewlines
from nuitka.tools.testing.Common import convertToPython, goMainDir

goMainDir()

if not os.path.exists("doctest_generated"):
    os.mkdir("doctest_generated")


def saveAsGeneratedDoctest(name, value, line_filter=None, prefix=""):
    if prefix:
        prefix = prefix + "\n"

    filename = os.path.join("doctest_generated", name)

    with open(filename, "w") as output:
        output.write(prefix)

        if type(value) in (tuple, list):
            for val in value:
                output.write("\n")
                output.write("#" * 80)
                output.write("\n")
                output.write(convertToPython(val, line_filter))
        else:
            output.write(convertToPython(value, line_filter))

    cleanupWindowsNewlines(filename)


saveAsGeneratedDoctest(
    "test_cmd.py",
    test.test_cmd.samplecmdclass.__doc__,
    prefix="from test.test_cmd import samplecmdclass",
)


saveAsGeneratedDoctest("test_deque.py", test.test_deque.libreftest)


saveAsGeneratedDoctest(
    "test_descrtut.py",
    tuple(sorted(test.test_descrtut.__test__.values())),
    prefix="from test.test_descrtut import defaultdict,defaultdict2,sortdict\nimport pprint",
)


saveAsGeneratedDoctest(
    "test_extcall.py",
    test.test_extcall.__doc__,
    prefix="import test.support as support",
)


def filter_generators(line):
    # Driven by returns, pylint: disable=too-many-return-statements

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


saveAsGeneratedDoctest(
    "test_generators.py",
    tuple(sorted(test.test_generators.__test__.values())),
    line_filter=filter_generators,
    prefix="from test.test_generators import Knights",
)


def filter_genexps(line):
    if (
        line.find(
            "set(attr for attr in dir(g) if not attr.startswith('__')) >= expected"
        )
        != -1
    ):
        return True
    elif line.find("isinstance(g, types.GeneratorType)") != -1:
        return True
    else:
        return False


saveAsGeneratedDoctest(
    "test_genexps.py", test.test_genexps.doctests, line_filter=filter_genexps
)


saveAsGeneratedDoctest(
    "test_itertools.py",
    test.test_itertools.libreftest,
    prefix="from itertools import *",
)


saveAsGeneratedDoctest("test_listcomps.py", test.test_listcomps.doctests)


saveAsGeneratedDoctest("test_setcomps.py", test.test_setcomps.doctests)


saveAsGeneratedDoctest("test_unpack.py", test.test_unpack.doctests)


saveAsGeneratedDoctest("test_unpack_ex.py", test.test_unpack_ex.doctests)


saveAsGeneratedDoctest("test_weakref.py", test.test_weakref.libreftest)

saveAsGeneratedDoctest("test_ieee754.py", open("test/ieee754.txt").read())


saveAsGeneratedDoctest("test_metaclass.py", test.test_metaclass.doctests)
