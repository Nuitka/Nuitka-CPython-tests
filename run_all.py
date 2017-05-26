#!/usr/bin/env python3.4

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

    if python_version < "3":
        # Order of syntax errors found is not the same. Encoding errors often
        # overtake print function despite it being statement in Python2 errors-
        if filename in ("test_locale.py", "test_xml_etree.py",
                        "test_getpass.py", "test_hash.py",
                        "test_warnings.py", "test_configparser.py"):
            extra_flags.append("ignore_stderr")

    if os.name == "nt" and filename == "test_univnewlines.py":
        reportSkip("this causes MemoryError for unknown reasons.", dirname, filename)
        return

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
        if filename in ("test_shutil.py", "test_ntpath.py", "test_base_events.py"):
            extra_flags.append("ignore_stderr")

    if filename in ("test_buffer.py", "test_base_events.py",
                    "test_tasks.py", "test_unparse.py"):
        extra_flags.append("ignore_warnings")

    # We don't output ignored exception for that test case.
    if filename == "test_locks.py":
        extra_flags.append("ignore_stderr")
    if filename == "test_streams.py":
        extra_flags.append("ignore_stderr")

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
                        "test_exceptions.py", "test_unicode.py",
                        "test_winreg.py"):
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

        if dirname.endswith("test_asyncio"):
            my_print("Skipped, older CPython has no asyncio.")
            return

        if dirname.endswith("test_email"):
            my_print("Skipped, older CPython has different email API.")
            return

        if filename == "test_imp.py":
            my_print("Skipped, fails on Windows for technical reasons.")
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
        if filename in ("test_codeccallbacks.py", "test_xml_etree_c.py"):
            my_print("Skipped, CPython crashes.")
            return

    if python_version >= "3.5":
        if filename == "test_poplib.py":
            my_print("Skipped, newer CPython hangs in test.")
            return

        # TODO: This could be removed, once we have deprecation warnings
        # under control.
        if filename in ("test_re.py", "test_smtpd.py"):
            my_print("Skipped, newer CPython gives deprecation warnings.")
            return

        if dirname.endswith("test_asyncio"):
            my_print("Skipped, older CPython has no asyncio.")
            return

        if filename == "test_buffer.py":
            extra_flags.append("ignore_stderr")

    if os.name != "nt" and "arm" in os.uname().machine:
        if filename == "test_futures.py":
                my_print("Skipped, ARM compiled Nuitka segaults in openssl init.")
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
        if not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        fullname = os.path.join(dirname, filename)
        fullname = os.path.normpath(fullname)

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
        else:
            my_print("Skipping", os.path.join(dirname, filename))

checkDir("test")
checkDir("doctest_generated")
