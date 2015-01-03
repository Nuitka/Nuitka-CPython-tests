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

    if python_version < b"2.7" and \
       filename in ("test_strop.py", "test_cpickle.py"):
        extra_flags.append("ignore_stderr")
    elif python_version >= b"2.7" and \
         filename in ("test_xml_etree.py", "test_xml_etree_c.py",
                      "test_zipfile.py"):
        extra_flags.append("ignore_stderr")
    elif os.name == "nt" and \
         filename in ("test_unicode.py", "test_unicode_file.py"):
        extra_flags.append("ignore_stderr")

    # This crashes CPython2.7.exe on Windows, so avoid it.
    if os.name == "nt" and \
       python_version >= b"2.7" and \
       filename == "test_time.py":
        my_print("Skipping (crashes CPython2.7 on Windows)", path)

        return

    if "doctest_generated" in path and python_version < b"3":
        extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                my_print("Skipping", path, "not enough memory with 32 bits.")
                return

    compareWithCPython(
        path        = path,
        extra_flags = extra_flags,
        search_mode = search_mode,
        needs_2to3  = python_version >= "3"
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
