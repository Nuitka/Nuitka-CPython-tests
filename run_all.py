#!/usr/bin/env python3.11

""" Runner for CPython 3.10 test suite comparing against Nuitka.

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
        # Cache the CPython results for reuse, they will normally not change.
        "cpython_cache",
        # Need to provide version, to know if to disable frozen modules.
        "--python-version=%s" % ".".join(str(d) for d in python_version),
    ]

    # TODO: This deadlocks, likely a threading problem.
    if python_version >= (3, 4) and filename == "test_concurrent_futures.py":
        reportSkip("Skipping (due to threading issue)", dirname, filename)
        return

    # TODO: This is a problem, we are not complete with | assignments yet
    if filename == "test_patma.py":
        my_print("Skipping (due to INCOMPLETE implementation)", filename)
        return

    if dirname == "doctest_generated":
        if python_version >= (3, 11):
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip(
                    "not enough memory with 32 bits on Windows", dirname, filename
                )

                return

    if filename in ("test_platform.py", "test_dataclasses.py", "test_asyncgen.py"):
        extra_flags.append("ignore_stderr")

    # TODO: Delayed, get it to work.
    if filename == "test_exceptions.py":
        reportSkip("KNOWN BUGGY", dirname, filename)
        return

    if filename == "test_datetime.py":
        extra_flags.append("recurse_to:test.datetimetester")

    if filename == "test_contextlib_async.py":
        # Task warnings
        extra_flags.append("ignore_stderr")

    if python_version < (3, 10):
        if filename in (
            "test_embed.py",
            "test_pow.py",
        ):
            reportSkip(
                "Using assignment expressions not supported on older Python",
                dirname,
                filename,
            )
            return

        if filename == "test_genericalias.py":
            reportSkip("Generic alias not supported on older Python", dirname, filename)
            return

    if python_version < (3, 11):
        if filename in (
            "test_abc.py",
            "test_os.py",
            "test_ast.py",
            "test_fstring.py",
            "test_functools.py",
            "test_grammar.py",
            "test_gc.py",
            "test_inspect.py",
            "test_call.py",
            "test_dataclasses.py",
            "test_types.py",
            "test_typing.py",
            # 3.8 only syntax
            "test_positional_only_arg.py",
            # 3.10 only syntax
            "test_named_expressions.py",
            # 3.11 only syntax
            "test_exception_variations.py",
            "test_except_star.py",
            "test_strftime.py",
        ):
            reportSkip("Not useful with older Python", dirname, filename)
            return

        # Outputs dict versions which are different.
        if filename == "test_dict_version.py":
            extra_flags.append("ignore_stderr")
    elif python_version >= (3, 12):
        if filename in (
            "test_ast.py",
            "test_code.py",
            "test_descrtut.py",
            "test_netrc.py",
            "test_ntpath.py",
            "test_reprlib.py",
            "test_tarfile.py",
            "test_tempfile.py",
            "test_threading.py",
            "test_traceback.py",
        ):
            reportSkip("Not useful with newer Python", dirname, filename)
            return
    else:
        # Put 3.11 specific stuff here.
        pass

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

        if active:
            checkPath(dirname, filename)


python_version = setup(suite="CPython310", needs_io_encoding=True)
setupCacheHashSalt(".")

search_mode = createSearchMode()

addToPythonPath(os.path.abspath("."), in_front=True)

checkDir("test")
checkDir("doctest_generated")
