#!/usr/bin/env python3.2

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
    extra_flags = [
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # We mean to compile only that one module
        "recurse_none"
    ]

    if path == "test" + os.path.sep + "test_shelve.py":
        extra_flags.append("ignore_stderr")

    # This imports a file with a syntax error, which Nuitka gives a warning
    # for, which is not an issue of course.
    if filename == "test_pep3120.py":
        extra_flags.append("ignore_warnings")

    # This imports "A" and "B". Not whitelisting that, so allow for warnings
    # for this case.
    if filename == "test_threaded_import.py":
        extra_flags.append("ignore_warnings")

    if python_version < "3" and \
       filename in ("test_locale.py", "test_nntplib.py", \
                    "test_sys_settrace.py", "test_warnings.py",
                    "test_xml_etree.py"):
        extra_flags.append("ignore_stderr")

    # Deprecation warnings on wrong lines.
    if python_version >= "3.3" and \
       filename in ("test_smtpd.py", "test_unicode.py"):
        my_print("Skipping (warning output with wrong line)", path)
        return

    if python_version >= "3.4" and \
       filename in ("test_ast.py", "test_base64.py", "test_cmd_line_script.py"):
        return

    if python_version >= "3.2" and python_version < "3.3" and os.name == "nt":
        if filename in ("test_ast.py", "test_descr.py", "test_imp.py",
                        "test_json.py", "test_os.py", "test_pickle.py",
                        "test_pickletools.py", "test_time.py"):
            my_print("Skipping (crashes CPython on Windows)", path)
            return

        if filename == "test_pep3120.py":
            my_print("Skipping (crashes CPython compiled the file on Windows)", path)
            return

        if filename in ("test_exceptions.py", "test_keywordonlyarg.py",
                        "test_raise.py"):
            my_print("Skipping (the CPython fails more on Windows)", path)
            return

        if filename == "test_range.py":
            my_print("Skipping (crashes for unknown reason on Windows with MSVC only)", path)
            return

    if "doctest_generated" in path:
        if python_version >= "3":
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
        needs_2to3  = False
    )


def checkDir(directory):
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".py") or not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        active = search_mode.consider(directory, filename)

        # This goes havoc on memory consumption.
        if filename == "test_itertools.py" and directory == "doctest_generated" and python_version < "3":
            continue

        path = os.path.join(directory, filename)

        if active:
            checkPath(filename, path)
        else:
            my_print("Skipping", path)

checkDir("test")
checkDir("doctest_generated")
