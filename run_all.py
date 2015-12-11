#!/usr/bin/env python3.5

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

    if python_version < "3":
        # Order of syntax errors found is not the same. Encoding errors often
        # overtake print function despite it being statement in Python2 errors-
        if filename in ("test_locale.py", "test_xml_etree.py",
                        "test_getpass.py", "test_hash.py",
                        "test_warnings.py", "test_configparser.py"):
            extra_flags.append("ignore_stderr")

    if dirname == "doctest_generated":
        if python_version >= "3.4":
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
        if filename in ("test_shutil.py", "test_ntpath.py"):
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

    if python_version < "3.4":
        if filename in ("test_contextlib.py", "test_format.py",
                        "test_poplib.py", "test_pickle.py",
                        "test_exceptions.py", "test_unicode.py"):
            my_print("Skipped, triggers CPython bug in old versions.")
            return

        if filename == "test_docxmlrpc.py":
            my_print("Skipped, older CPython gives random port outputs.")
            return

        if filename == "test_sched.py":
            my_print("Skipped, older CPython gives random time stamps.")
            return

        if filename == "test_scope.py":
            my_print("Skipped, older CPython fails test that Nuitka passes.")
            return

        if filename == "test_pkg.py":
            my_print("Skipped, older CPython fails test with random output.")
            return

        if filename == "test_urllib.py":
            my_print("Skipped, older CPython fails test with random output.")
            return

        if filename == "test_strftime.py":
            my_print("Skipped, older CPython bug causes crash.")
            return

        if filename == "test_super.py":
            my_print("Skipped, older CPython bug causes crash.")
            return

        if filename == "test_datetime.py":
            my_print("Skipped, older CPython bug causes crash.")
            return

        if filename == "test_descr.py":
            my_print("Skipped, older CPython bug causes crash.")
            return

        if filename == "test_xml_etree_c.py":
            my_print("Skipped, older CPython bug causes crash.")
            return

        if filename == "test_pep277.py":
            my_print("Skipped, older CPython has divergent unicode warning.")
            return

        if filename == "test_fileinput.py":
            my_print("Skipped, older CPython runs into MemoryError.")
            return

        if filename == "test_collections.py":
            my_print("Skipped, older CPython differs in recursion error.")
            return

        if filename == "test_urllib_response.py":
            my_print("Skipped, older CPython differs in error message.")
            return

    if python_version < "3.4.3":
        if filename == "test_multibytecodec.py":
            my_print("Skipped, older CPython runs into MemoryError.")
            return

        if filename == "test_multiprocessing_fork.py":
            my_print("Skipped, older CPython hangs in test.")
            return

        if filename == "test_tempfile.py":
            my_print("Skipped, older CPython has bug.")
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
