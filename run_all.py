#!/usr/bin/env python3.8

""" Runner for CPython 3.8 test suite comparing against Nuitka.

Not every test of CPython has to pass, but instead it should fail just
the same with Nuitka.

"""

import os
import sys

# Find nuitka package relative to us.
sys.path.insert(
    0,
    os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    ),
)

# isort:start

from nuitka.tools.testing.Common import (
    addToPythonPath,
    compareWithCPython,
    createSearchMode,
    my_print,
    reportSkip,
    setup,
    setupCacheHashSalt,
)


def checkPath(dirname, filename):
    # Complex stuff, pylint: disable=too-many-branches,too-many-return-statements

    extra_flags = [
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # We mean to compile only that one module
        "recurse_none",
        # Keep us informed about timing, even if concurrent runs spoil the
        # accuracy.
        "timing",
        # Use the original __file__ value, at least one case warns about things
        # with filename included.
        "original_file",
        # Cache the CPython results for re-use, they will normally not change.
        "cpython_cache",
        # Never use multiprocessing plugin, these are false alarms.
        "plugin_disable:multiprocessing",
    ]

    # TODO: This deadlocks, likely a threading problem.
    if python_version >= "3.4" and filename == "test_concurrent_futures.py":
        reportSkip("Skipping (due to threading issue)", dirname, filename)
        return

    # TODO: This fails to compile, super is not fully solved.
    if python_version >= "3.4" and filename == "test_super.py":
        my_print("Skipping (due to compilation issue)", filename)
        return

    if dirname == "doctest_generated":
        if python_version >= "3.8":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip(
                    "not enough memory with 32 bits on Windows", dirname, filename
                )

                return

    if filename in ("test_platform.py", "test_dataclasses.py", "test_asyncgen.py"):
        extra_flags.append("ignore_stderr")

    # TODO: Delayed, get it to work.
    if filename == "test_exceptions.py":
        reportSkip("KNOWN BUGGY", dirname, filename)
        return

    if filename == "test_datetime.py":
        extra_flags.append("recurse_to:test.datetimetester")

    if python_version < "3.8":
        if filename in ("test_abc.py", "test_os.py", "test_ast.py"):
            reportSkip("Not useful with older Python", dirname, filename)
            return

        if filename == "test_collections.py":
            reportSkip("Hangs with older Python", dirname, filename)
            return

    else:
        # Put 3.8 specific stuff here.
        pass


    compareWithCPython(
        dirname=dirname,
        filename=filename,
        extra_flags=extra_flags,
        search_mode=search_mode,
        needs_2to3=False,
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


python_version = setup(suite="CPython38", needs_io_encoding=True)
setupCacheHashSalt(".")

search_mode = createSearchMode()

addToPythonPath(os.path.abspath("."), in_front=True)

checkDir("test")
checkDir("doctest_generated")
