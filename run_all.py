#!/usr/bin/env python3.7

import os, sys

# Find nuitka package relative to us.
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
    my_print,
    setup,
    reportSkip,
    compareWithCPython,
    createSearchMode
)

python_version = setup(suite = "CPython37", needs_io_encoding = True)

search_mode = createSearchMode()

def checkPath(dirname, filename):
    global active

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
    ]

    # TODO: Segfaulting due to reference counting issue.
    if filename == "test_asyncgen.py":
        my_print("Skipping (KNOWN BUGGY)", filename)
        return

    # TODO: This deadlocks, likely a threading problem.
    if python_version >= "3.4" and \
       filename == "test_concurrent_futures.py":
        reportSkip("Skipping (due to threading issue)", dirname, filename)
        return

    # TODO: This fails to compile, super is not fully solved.
    if python_version >= "3.4" and \
       filename == "test_super.py":
        my_print("Skipping (due to compilation issue)", filename)
        return

    if dirname == "doctest_generated":
        if python_version >= "3.7":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip("not enough memory with 32 bits on Windows", dirname, filename)

                return

    if filename in ("test_platform.py", "test_dataclasses.py"):
        extra_flags.append("ignore_stderr")

    # TODO: Get it to work!
    if filename == "test_asyncgen.py":
        reportSkip("KNOWN BUGGY", dirname, filename)
        return

    # TODO: Delayed, get it to work.
    if filename == "test_exceptions.py":
        reportSkip("KNOWN BUGGY", dirname, filename)
        return

    if filename == "test_gc.py" and python_version == "3.7.0":
        reportSkip("Bug in CPython 3.7.0 affects gc.", dirname, filename)
        return

    if filename == "test_datetime.py" and python_version == "3.7.0":
        # TODO: Use this for actual coverage.
        extra_flags.append("recurse_to:test.datetimetester")

        reportSkip("Bug in CPython 3.7.0 affects test.", dirname, filename)
        return

    if python_version < "3.7":
        if filename in ("test_abc.py",):
            reportSkip("Not useful with older Python", dirname, filename)
            return

        if filename in ("test_compile.py", "test_codeccallbacks.py",
                        "test_datetime.py"):
            reportSkip("Crashes with older Python", dirname, filename)
            return

        if filename == "test_difflib.py":
            reportSkip("Hangs with older Python", dirname, filename)
            return

        if filename == "test_imp.py":
            reportSkip("Not bug compatible with older Python", dirname, filename)
            return

    compareWithCPython(
        dirname     = dirname,
        filename    = filename,
        extra_flags = extra_flags,
        search_mode = search_mode,
        needs_2to3  = False
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
