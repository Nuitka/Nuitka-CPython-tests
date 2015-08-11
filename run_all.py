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
    reportSkip,
    compareWithCPython,
    createSearchMode
)

python_version = setup(needs_io_encoding = True)

search_mode = createSearchMode()

def checkPath(dirname, filename):
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

    if python_version < "3" and \
       filename in ("test_locale.py", "test_nntplib.py", \
                    "test_sys_settrace.py", "test_warnings.py",
                    "test_xml_etree.py"):
        extra_flags.append("ignore_stderr")

    # This goes havoc on memory consumption.
    if python_version < "3" and \
       dirname == "doctest_generated" and \
       filename == "test_itertools.py":
        reportSkip("bug of Python2 causing it be a memory hog", dirname, filename)
        return

    # Deprecation warnings on wrong lines.
    if python_version >= "3.3" and \
       filename in ("test_smtpd.py", "test_unicode.py"):
        reportSkip("warning output with wrong line", dirname, filename)
        return

    if python_version >= "3.4" and \
       filename in ("test_ast.py", "test_base64.py", "test_cmd_line_script.py"):
        reportSkip("undocumented reason", dirname, filename)
        return

    if python_version >= "3.3" and filename == "test_shutil.py":
        reportSkip("doesn't work properly with CPython already", dirname, filename)
        return

    if python_version >= "3.2" and python_version < "3.3" and os.name == "nt":
        if filename in ("test_ast.py", "test_descr.py", "test_imp.py",
                        "test_json.py", "test_os.py", "test_pickle.py",
                        "test_pickletools.py", "test_time.py"):
            reportSkip("crashes CPython on Windows", dirname, filename)
            return

        if filename == "test_pep3120.py":
            reportSkip("crashes CPython on Windows", dirname, filename)
            return

        if filename in ("test_exceptions.py", "test_keywordonlyarg.py",
                        "test_raise.py"):
            reportSkip("CPython fails more on Windows", dirname, filename)
            return

        if filename == "test_range.py":
            reportSkip("crashes for unknown reason on Windows with MSVC only", dirname, filename)
            return

    if dirname == "doctest_generated":
        if python_version >= "3":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip("not enough memory with 32 bits on Windows", dirname, filename)

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

        active = search_mode.consider(dirname, filename)

        if active:
            checkPath(dirname, filename)
        else:
            my_print("Skipping", os.path.join(dirname, filename))

checkDir("test")
checkDir("doctest_generated")
