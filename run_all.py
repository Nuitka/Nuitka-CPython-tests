#!/usr/bin/env python3.3

""" Runner for CPython 3.3 test suite comparing against Nuitka.

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

    # Avoid memory runaway of CPython2.
    if (
        dirname == "doctest_generated"
        and filename == "test_itertools.py"
        and python_version < (3,)
    ):
        reportSkip("This triggers memory error with CPython2.x", dirname, filename)
        return

    if python_version < (3,):
        # Order of syntax errors found is not the same. Encoding errors often
        # overtake print function despite it being statement in Python2 errors-
        if filename in ("test_locale.py", "test_xml_etree.py"):
            extra_flags.append("ignore_stderr")

    if filename == "test_buffer.py":
        extra_flags.append("ignore_stderr")

    # Imports a module with syntax errors.
    if filename == "test_pep3120.py":
        extra_flags.append("ignore_warnings")

    # Imports missing packages we cannot whitelist.
    if filename in ("test_pkgutil.py", "test_threaded_import.py"):
        extra_flags.append("ignore_warnings")

    if filename in ("test_concurrent_futures.py", "test_logging"):
        # Plugins not needed.
        extra_flags.append("ignore_warnings")

    if os.name == "nt" and filename == "test_univnewlines.py":
        reportSkip("this causes MemoryError for unknown reasons.", dirname, filename)
        return

    if dirname == "doctest_generated":
        if python_version >= (3, 3):
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip(
                    "not enough memory with 32 bits on Windows", dirname, filename
                )

                return

    if python_version >= (3, 4):
        if filename == "test_argparse.py":
            my_print("Skipped, compilation takes too long for unknown reasons.")
            return

        if filename == "test_pep263.py":
            my_print("Skipped, CPython refuses to decode for no apparent reason.")
            return

        if filename == "test_pkg.py":
            my_print("Skipped, CPython fails with random output.")
            return

        if filename == "test_gettext.py":
            my_print("Skipped, older CPython fails to remove files after test.")
            return

    if python_version < (3, 3):
        # Can output warnings in debug mode on older CPython at least.
        if filename == "test_sax.py":
            extra_flags.append("ignore_stderr")

    if python_version < (2, 7):
        # Different syntax errors are OK.
        if filename == "test_configparser.py":
            extra_flags.append("ignore_stderr")

    compareWithCPython(
        dirname=dirname,
        filename=filename,
        extra_flags=extra_flags,
        search_mode=search_mode,
        needs_2to3=False,
    )


def checkDir(dirname):
    for filename in sorted(os.listdir(dirname)):
        if not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        fullname = os.path.join(dirname, filename)

        if os.path.isfile(fullname):
            if not filename.endswith(".py"):
                continue
        else:
            if not os.path.isfile(os.path.join(fullname, "__main__.py")):
                continue

            checkDir(fullname)
            continue

        active = search_mode.consider(dirname, filename)

        if active:
            checkPath(dirname, filename)


python_version = setup(suite="CPython33", needs_io_encoding=True)
setupCacheHashSalt(".")

search_mode = createSearchMode()

addToPythonPath(os.path.abspath("."), in_front=True)

checkDir("test")
checkDir("doctest_generated")
