#!/usr/bin/env python3.3

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
    decideFilenameVersionSkip,
    compareWithCPython,
    hasDebugPython,
    createSearchMode
)

python_version = setup(needs_io_encoding = True)

search_mode = createSearchMode()

def checkPath(filename, path):
    global active

    extra_flags = [
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # We mean to compile only that one module
        "recurse_none"
    ]

    # Avoid memory runaway of CPython2.
    if path == "doctest_generated/test_itertools.py" and python_version < "3":
        return

    if filename == "test_buffer.py":
        extra_flags.append("ignore_stderr")

    # Imports a module with syntax errors.
    if filename == "test_pep3120.py":
        extra_flags.append("ignore_warnings")

    # Imports missing packages we cannot whitelist.
    if filename in ("test_pkgutil.py", "test_threaded_import.py"):
        extra_flags.append("ignore_warnings")

    if "doctest_generated" in path:
        if python_version >= "3.3":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                my_print("Skipping", path, "not enough memory with 32 bits.")
                return

    if python_version >= "3.4":
        if filename == "test_argparse.py":
            my_print("Skipped, compilation takes too long for unknown reasons.")
            return

        if filename == "test_codecs.py":
            my_print("Skipped, due to hard to disable deprecation warning.")
            return

        if filename == "test_pep263.py":
            my_print("Skipped, CPython refuses to decode for no apparent reason.")
            return

        if filename == "test_pkg.py":
            my_print("Skipped, CPython fails with random output.")
            return


        # Gives deprecation warnings, unclear why that can happen. We try and
        # succeed at disabling them (as is Python default), but they seem to
        # be given in this test case anyway.
        if filename in ("test_format.py", "test_unicode.py",
                        "test_userstring.py", "test_ntpath.py"):
            extra_flags.append("ignore_stderr")

    compareWithCPython(
        path        = path,
        extra_flags = extra_flags,
        search_mode = search_mode,
        needs_2to3  = False
    )


def checkDir(directory):
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".py") or not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        active = search_mode.consider(directory, filename)

        path = os.path.join(directory, filename)


        if active:
            checkPath(filename, path)
        else:
            my_print("Skipping", path)

checkDir("test")
checkDir("doctest_generated")
