#!/usr/bin/env python3.6

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
        # Keep us informed about timing, even if concurrent runs spoil the
        # accuracy.
        "timing",
        # Use the original __file__ value, at least one case warns about things
        # with filename included.
        "original_file"
    ]

    # Avoid memory runaway of CPython2.
    if dirname == "doctest_generated" and \
       filename == "test_itertools.py" and \
       python_version < "3":
        reportSkip("This triggers memory error with CPython2.x", dirname, filename)
        return

    if dirname == "doctest_generated":
        if python_version >= "3.6":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip("not enough memory with 32 bits on Windows", dirname, filename)

                return
    else:
        # TODO: Deprecation warnings for some unknown reason. Need to find
        # out why we don't successfully disable it.
        if filename in ("test_shutil.py", "test_ntpath.py", "test_with.py"):
            extra_flags.append("ignore_stderr")

    if filename == "test_buffer.py":
        extra_flags.append("ignore_warnings")

    # TODO: This deadlocks, likely a threading problem.
    if python_version >= "3.4" and \
       filename == "test_concurrent_futures.py":
        my_print("Skipping (due to threading issue)", filename)
        return

    # TODO: This fails to compiler, super is not fully solved.
    if python_version >= "3.4" and \
       filename == "test_super.py":
        my_print("Skipping (due to compilation issue)", filename)
        return

    # TODO: The output from cgit attempts to access locals not in the frame,
    # probably due to chaining problems from above.
    if filename == "test_cgitb.py":
        my_print("Skipping (due to traceback issue)", filename)
        return

    if python_version < "3.6":
        if filename in ("test_file.py", "test_re.py"):
            my_print("Skipped, gives deprecation warnings with CPython3.5.")
            return

        if filename in ("test_asyncgen.py", "test_collections.py",
                        "test_coroutines.py", "test_fstring.py",
                        "test_functools.py", "test_grammar.py",
                        "test_inspect.py", "test_opcodes.py",
                        "test_traceback.py", "test_unpack.py"):
            my_print("Skipped, gives syntax error with CPython3.5.")
            return

        if filename in ("test_tcl.py", "test_bz2.py"):
            my_print("Skipped, segfaults with CPython3.5.")
            return

        if filename in ("test_aifc.py", "test_binascii.py"):
            my_print("Skipped, fails with non-determistic output with CPython3.5.")
            return

        if filename == "test_contextlib.py":
            my_print("Skipped, hangs with CPython3.5.")
            return

        if filename == "test_hashlib.py":
            extra_flags.append("ignore_warnings")

        if filename == "test_ordered_dict.py":
            my_print("Skipped, fails with random errors before 3.6.")
            return

        if filename == "test_syntax.py":
            my_print("Skipped, not useful with older version.")
            return

    if os.name == "nt":
        if filename in ("test_itertools.py", ):
            my_print("Skipped, CPython on Windows crashes.")
            return

        if filename in ("test_os.py", "test_tarfile.py", ):
            my_print("Skipped, gives deprecation warnings on Windows.")
            return

        if filename in ("test_pathlib.py", ):
            my_print("Skipped, outputs random paths on Windows.")
            return

        if filename == "test_logging.py":
            my_print("Skipped, dead locks on Windows due to races.")
            return
    else:
        if filename in ("test_winconsoleio.py", "test_winreg.py"):
            my_print("Skipping (Windows only)", filename)
            return

    if filename == "test_asyncgen.py":
        my_print("Skipping (KNOWN BUGGY)", filename)
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
