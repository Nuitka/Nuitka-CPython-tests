#!/usr/bin/env python3.3

""" Runner for CPython 3.2 test suite comparing against Nuitka.

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
    # Many cases to deal with, pylint: disable=too-many-branches,too-many-return-statements

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
        # Never use multiprocessing plugin, these are false alarms.
        "plugin_disable:multiprocessing",
    ]

    if dirname == "test" and filename == "test_shelve.py":
        extra_flags.append("ignore_stderr")

    # This imports a file with a syntax error, which Nuitka gives a warning
    # for, which is not an issue of course.
    if filename == "test_pep3120.py":
        extra_flags.append("ignore_warnings")

    # This imports "A" and "B". Not whitelisting that, so allow for warnings
    # for this case.
    if filename == "test_threaded_import.py":
        extra_flags.append("ignore_warnings")

    if python_version < "3" and filename in (
        "test_locale.py",
        "test_nntplib.py",
        "test_sys_settrace.py",
        "test_warnings.py",
        "test_xml_etree.py",
    ):
        extra_flags.append("ignore_stderr")

    # This goes havoc on memory consumption.
    if (
        python_version < "3"
        and dirname == "doctest_generated"
        and filename == "test_itertools.py"
    ):
        reportSkip("bug of Python2 causing it be a memory hog", dirname, filename)
        return

    if os.name == "nt" and filename == "test_univnewlines.py":
        reportSkip("this causes MemoryError for unknown reasons.", dirname, filename)
        return

    # Deprecation warnings on wrong lines.
    if python_version >= "3.3" and filename in ("test_smtpd.py", "test_unicode.py"):
        reportSkip("warning output with wrong line", dirname, filename)
        return

    if python_version >= "3.4" and filename in (
        "test_ast.py",
        "test_base64.py",
        "test_cmd_line_script.py",
    ):
        reportSkip("undocumented reason", dirname, filename)
        return

    if python_version >= "3.3" and filename == "test_shutil.py":
        reportSkip("doesn't work properly with CPython already", dirname, filename)
        return

    if python_version >= "3.3" and filename in ("test_signal.py",):
        reportSkip("Timings are not strictly the same", dirname, filename)
        return

    if python_version >= "3.3" and filename in ("test_pickle.py",):
        reportSkip("Recursion errors are not strictly the same", dirname, filename)
        return

    if dirname == "doctest_generated":
        if python_version >= "3":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip(
                    "not enough memory with 32 bits on Windows", dirname, filename
                )

                return

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

        active = search_mode.consider(dirname, filename)

        if active:
            checkPath(dirname, filename)


python_version = setup(suite="CPython32", needs_io_encoding=True)
setupCacheHashSalt(".")

search_mode = createSearchMode()

addToPythonPath(os.path.abspath("."), in_front=True)

checkDir("test")
checkDir("doctest_generated")
