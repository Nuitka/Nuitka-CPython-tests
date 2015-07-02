#!/usr/bin/env python

import os, sys

# Find common code relative in file system. Not using packages for test stuff.
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
    my_print,
    setup,
    compareWithCPython,
    reportSkip,
    createSearchMode
)

python_version = setup(needs_io_encoding = True)

search_mode = createSearchMode()


def checkPath(dirname, filename):
    global active

    extra_flags = [
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # We mean to compile only that one module
        "recurse_none",
        # Use the original __file__ value, at least one case warns about things
        # with filename included.
        "original_file"
    ]

    if filename in ("test_import.py", "test_importhooks.py", "test_pkgimport.py", "test_py3kwarn.py", "test_runpy.py", "test_zipimport.py"):
        # These will given the __import__ not resolved warning and there won't
        # be anything to ever change that.
        extra_flags.append("ignore_stderr")
    elif filename in ("test_fork1.py", "test_pyclbr.py", "test_scriptpackages.py", "test_uuid.py", "test_multiprocessing.py"):
        # These will given the __import__ not resolved warning, but they ought
        # to go away.
        extra_flags.append("ignore_stderr")
    elif filename in ("test_unicode_file.py",):
        # Under Windows, stderr shows some Python warning here.
        extra_flags.append("ignore_stderr")
    elif filename in ("test_zipfile.py", ):
        extra_flags.append("ignore_stderr")
    elif filename in ("test_mmap.py",) and os.name == "nt":
        reportSkip("does not work on Windows", dirname, filename)

        return

    if python_version < "2.7":
        if filename == "test_scope.py":
            reportSkip("we do not emulate bugs on old Python", dirname, filename)

            return


    if dirname == "doctest_generated":
        if python_version < "3" and python_version >= "2.7":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip("memory issue with 32 bits Windows", dirname, filename)

                return

    compareWithCPython(
        dirname     = dirname,
        filename    = filename,
        extra_flags = extra_flags,
        search_mode = search_mode,
        needs_2to3  = python_version >= "3"
    )

def checkDir(dirname):
    for filename in sorted(os.listdir(dirname)):
        if not filename.endswith(".py") or not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        active = search_mode.consider(dirname, filename)

        if active:
            checkPath(dirname, filename)
        else:
            my_print("Skipping", os.path.join(dirname, filename))

checkDir("test")
checkDir("doctest_generated")

search_mode.finish()
