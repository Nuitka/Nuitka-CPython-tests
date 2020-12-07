#!/usr/bin/env python

""" Runner for CPython 2.6 test suite comparing against Nuitka.

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
    reportSkip,
    setup,
    setupCacheHashSalt,
)


def checkPath(dirname, filename):
    extra_flags = [
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # We mean to compile only that one module
        "recurse_none",
        # Use the original __file__ value, at least one case warns about things
        # with filename included.
        "original_file",
        # Cache the CPython results for re-use, they will normally not change.
        "cpython_cache",
    ]

    if python_version < (2, 7) and filename in ("test_strop.py", "test_cpickle.py"):
        extra_flags.append("ignore_stderr")
    elif python_version >= (2, 7) and filename in (
        "test_xml_etree.py",
        "test_xml_etree_c.py",
        "test_zipfile.py",
    ):
        extra_flags.append("ignore_stderr")
    elif os.name == "nt" and filename in ("test_unicode.py", "test_unicode_file.py"):
        extra_flags.append("ignore_stderr")

    # This crashes CPython2.7.exe on Windows, so avoid it.
    if os.name == "nt" and python_version >= (2, 7) and filename == "test_time.py":
        reportSkip("crashes CPython2.7 on Windows", dirname, filename)

        return

    if python_version >= (2, 7):
        if filename == "test_zip.py":
            reportSkip("Varying error output with newer Python", dirname, filename)

            return

    if "doctest_generated" in dirname and python_version < (3,):
        extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip("memory issue with 32 bits Windows", dirname, filename)

                return

    compareWithCPython(
        dirname=dirname,
        filename=filename,
        extra_flags=extra_flags,
        search_mode=search_mode,
        needs_2to3=python_version >= (3,),
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


python_version = setup(suite="CPython26", needs_io_encoding=True)
setupCacheHashSalt(".")

search_mode = createSearchMode()

addToPythonPath(os.path.abspath("."), in_front=True)

checkDir("test")
checkDir("doctest_generated")

search_mode.finish()
