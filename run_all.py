#!/usr/bin/env python3.3

from __future__ import print_function

import os, sys, subprocess

# Go its own directory, to have it easy with path knowledge.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

search_mode = len( sys.argv ) > 1 and sys.argv[1] == "search"

start_at = sys.argv[2] if len( sys.argv ) > 2 else None

if start_at:
    active = False
    start_at = start_at.replace("/", os.path.sep)
else:
    active = True

if "PYTHON" not in os.environ:
    os.environ["PYTHON"] = sys.executable

# Make sure we flush after every print, the "-u" option does more than that
# and this is easy enough.
def my_print(*args, **kwargs):
    print(*args, **kwargs)

    sys.stdout.flush()

def check_output(*popenargs, **kwargs):
    from subprocess import Popen, PIPE, CalledProcessError

    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise CalledProcessError(retcode, cmd, output=output)
    return output

version_output = check_output(
    [os.environ["PYTHON"], "--version"],
    stderr = subprocess.STDOUT
)

python_version = version_output.split()[1]

if sys.version.startswith("3"):
    python_version = python_version.decode()

os.environ["NUITKA_EXTRA_OPTIONS"] = \
  os.environ.get("NUITKA_EXTRA_OPTIONS", "") + \
  " --recurse-none"

my_print("Using concrete python", python_version)

def checkPath(filename, path):
    global active

    extra_flags = [
        "silent",
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # Ignore warnings about missing imports
        "ignore_warnings",
    ]

    # Avoid memory runaway of CPython2.
    if path == "doctest_generated/test_itertools.py" and python_version < "3":
        return

    if path == "test/test_shelve.py":
        extra_flags.append("ignore_stderr")

    if "doctest_generated" in path:
        if python_version >= "3.3":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                my_print("Skipping", path, "not enough memory with 32 bits.")
                return

    # TODO: These don't compile in debug mode yet, due to missing optimization
    if "--debug" in os.environ["NUITKA_EXTRA_OPTIONS"]:
        if filename in ("test_grammar.py", ):
            my_print("Skipped, does not compile in --debug mode without warnings.")
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

        # Gives deprecation warnings, unclear why that can happen. We try and
        # succeed at disabling them (as is Python default), but they seem to
        # be given in this test case anyway.
        if filename == "test_format.py":
            extra_flags.append("ignore_stderr")

    result = subprocess.call(
        "%s %s %s %s" % (
            sys.executable,
            os.path.join("..", "..", "bin", "compare_with_cpython"),
            path,
            " ".join(extra_flags)
        ),
        shell = True
    )

    for scanned in os.listdir("."):
        if scanned.startswith("@test_"):
            assert False, filename

    if result != 0 and search_mode:
        sys.exit(result)


def checkDir(directory):
    global active

    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".py") or not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        path = os.path.join(directory, filename)

        if not active and start_at in (filename, path):
            active = True

        if active:
            checkPath(filename, path)
        else:
            my_print("Skipping", path)

checkDir("test")
checkDir("doctest_generated")
